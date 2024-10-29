"""
the best model for the bigram prediction
"""

# pylint: disable=C0103 # constant variable name is in upper case

import torch
from matplotlib import pyplot as plt

DATA_FILE = "names.txt"
READ_MODE = "r"
ENCODING = "utf-8"

START_END = "."


def read_file(file_name):
    """read the file"""
    with open(file_name, READ_MODE, encoding=ENCODING) as file:
        return file.read().splitlines()


def build_vocab(names):
    """build the vocabulary"""
    chars = sorted(list(set("".join(names))))
    char_to_int = {char: index + 1 for index, char in enumerate(chars)}
    char_to_int[START_END] = 0
    int_to_char = {index: char for char, index in char_to_int.items()}
    vocab_size = len(char_to_int)

    return char_to_int, int_to_char, vocab_size


def build_bigram_freq(names, char_to_int, vocab_size):
    """build the bigram frequency"""
    bigram_freq = torch.zeros((vocab_size, vocab_size), dtype=torch.int32)

    for name in names:
        chars = [START_END] + list(name) + [START_END]
        for first, next_char in zip(chars, chars[1:]):
            first_index = char_to_int[first]
            next_index = char_to_int[next_char]
            bigram_freq[first_index, next_index] += 1

    return bigram_freq


def plot_bigram(bigram_freq, int_to_char):
    """plot the bigram frequency matrix"""

    plt.figure(figsize=(16, 16))
    plt.imshow(bigram_freq, cmap="Blues")
    for row in range(27):
        for column in range(27):
            chstr = int_to_char[row] + int_to_char[column]
            plt.text(column, row, chstr, ha="center", va="bottom", color="gray")
            plt.text(
                column,
                row,
                bigram_freq[row, column].item(),
                ha="center",
                va="top",
                color="gray",
            )
    plt.axis("off")
    plt.show()


def build_bigram_prob(bigram_freq):
    """build the bigram probability"""
    # add 1 to each frequency to avoid zero probability
    bigram_freq = (bigram_freq + 1).float()

    # for each row, create a probability distribution based on the frequency
    # the sum of probability of each row should be 1
    # the sum dim=1 means sum along the row, keepdim=True means keep the dimension
    # it is very important to keep the dimension, otherwise the division will not work
    # check PyTorch Broadcasting semantics https://pytorch.org/docs/stable/notes/broadcasting.html
    row_sum = bigram_freq.sum(dim=1, keepdim=True)
    bigram_prob = bigram_freq / row_sum
    print(f"bigram prob row 0: {bigram_prob[0]}")
    print(f"row 0 Sum: {bigram_prob[0].sum()}")

    return bigram_prob


# generate names based on the bigram probability
NUM_NAMES = 10
MANUAL_SEED = 2147483647


def generate_names(bigram_prob, int_to_char):
    """generate names based on the bigram probability"""

    generator = torch.Generator().manual_seed(MANUAL_SEED)

    for _ in range(NUM_NAMES):
        out = []
        index = 0
        while True:
            index = torch.multinomial(bigram_prob[index], 1, generator=generator).item()
            next_char = int_to_char[index]
            out.append(next_char)
            if next_char == START_END:
                break

        print("".join(out))


def eval_model(bigram_prob, names, char_to_int):
    """the model quality
    The likelihood is the product of probabilities of each pair.
    The likelihood of the entire data set is the measured quality of the training model.
    Higher is better.

    The real probability for each pair is typically small, for example,
    the average should be `1/27 = 0.037`. Thus, `logprob` is used.
    The range of `logprob` is from `-infinity` (when `p = 0`) to `0` (when `p=1`).
    The likelihood for `logprob` is the sum of the `logprob`.

    To make it a loss function (smaller is btter),
    use `nll` (negative log likelihood) that is the average negative log likilihood of each pair.
    The lowest `nll` value is `0`.

    Thus. to maximize the likelihood is to minimize the `nll`.
    """
    num_pairs = 0
    nll = 0
    for name in names:
        chars = [START_END] + list(name) + [START_END]
        for first, next in zip(chars, chars[1:]):
            first = char_to_int[first]
            next = char_to_int[next]
            nll += -torch.log(bigram_prob[first, next])
            num_pairs += 1

    return nll / num_pairs


def main():
    """main function"""
    names = read_file(DATA_FILE)
    char_to_int, int_to_char, vocab_size = build_vocab(names)

    bigram_freq = build_bigram_freq(names, char_to_int, vocab_size)
    # plot_bigram(bigram_freq, int_to_char)

    bigram_prob = build_bigram_prob(bigram_freq)
    generate_names(bigram_prob, int_to_char)

    loss = eval_model(bigram_prob, names, char_to_int)
    print(f"Loss: {loss}")


if __name__ == "__main__":
    main()
