"""Main module for the program."""

from data import Data, START_END
from model import BigramLanguageModel
from trainer import Trainer


DATA_FILE = "names.txt"
NUM_ITERATIONS = 101
NUM_NAMES = 10


def main():
    """main function"""
    data = Data(DATA_FILE)
    model = BigramLanguageModel(data.vocab_size)

    trainer = Trainer(data, model)
    trainer.train(NUM_ITERATIONS)
    model.generate_names(NUM_NAMES, data.int_to_char, START_END)


if __name__ == "__main__":
    main()
