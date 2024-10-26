"""Main module for the program."""

from data import Data
from model import BigramLanguageModel
from trainer import Trainer

DATA_FILE = "names.txt"


def main():
    """main function"""
    data = Data(DATA_FILE)
    model = BigramLanguageModel(data.vocab_size)
    trainer = Trainer(data, model)
    trainer.train(5001)
    model.generate_names(10, data.int_to_char)


if __name__ == "__main__":
    main()
