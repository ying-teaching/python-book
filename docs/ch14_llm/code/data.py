"""module to handle the data"""

import torch

READ_MODE = "r"
ENCODING = "utf-8"

START_END = "."


class Data:
    """class to handle the data"""

    def __init__(self, file_name):
        self.file_name = file_name
        self.names = self._read_file()
        self.char_to_int, self.int_to_char, self.vocab_size = self._build_vocab()

    def _read_file(self):
        """read the file"""
        with open(self.file_name, READ_MODE, encoding=ENCODING) as file:
            return file.read().splitlines()

    def _build_vocab(self):
        """build the vocabulary"""
        chars = sorted(list(set("".join(self.names))))
        char_to_int = {char: index + 1 for index, char in enumerate(chars)}
        char_to_int[START_END] = 0
        int_to_char = {index: char for char, index in char_to_int.items()}
        vocab_size = len(char_to_int)

        return char_to_int, int_to_char, vocab_size

    def get_training_data(self):
        """get the training data"""
        first_indexes, next_indexes = [], []

        for name in self.names:
            chars = ["."] + list(name) + ["."]
            for first_char, next_char in zip(chars, chars[1:]):
                first_index = self.char_to_int[first_char]
                next_index = self.char_to_int[next_char]
                first_indexes.append(first_index)
                next_indexes.append(next_index)

        first_indexes = torch.tensor(first_indexes)
        next_indexes = torch.tensor(next_indexes)
        return first_indexes, next_indexes
