"""module of Bigram language model."""

import torch
import torch.nn.functional as F

MANUAL_SEED = 2147483647


class BigramLanguageModel:
    """Bigram language model."""

    def __init__(self, vacab_size):
        self.vacab_size = vacab_size
        generator = torch.Generator().manual_seed(MANUAL_SEED)
        self.weights = torch.randn(
            (vacab_size, vacab_size), generator=generator, requires_grad=True
        )

    def __call__(self, first_indexes):
        first_encodings = F.one_hot(first_indexes, self.vacab_size).float()
        logits = first_encodings @ self.weights
        counts = logits.exp()
        probabilities = counts / counts.sum(dim=1, keepdim=True)
        return probabilities

    def generate_names(self, num_names, int_to_char):
        generator = torch.Generator().manual_seed(MANUAL_SEED)
        for _ in range(num_names):

            new_name = []
            index = 0

            while True:
                first_encoding = F.one_hot(
                    torch.tensor([index]), num_classes=self.vacab_size
                ).float()

                logits = first_encoding @ self.weights  # predict log-counts
                counts = logits.exp()  # counts, equivalent to N

                # probabilities for next character
                probabilities = counts / counts.sum(1, keepdims=True)
                # ----------

                index = torch.multinomial(
                    probabilities,
                    num_samples=1,
                    replacement=True,
                    generator=generator,
                ).item()

                new_name.append(int_to_char[index])
                if index == 0:
                    break

            print("".join(new_name))
