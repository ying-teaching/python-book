"""Trainer class for training the model."""

import torch


class Trainer:
    """Trainer class"""

    def __init__(self, data, model):
        self.data = data
        self.model = model

    def train(self, num_iterations):
        """train the model"""

        for iteration in range(num_iterations):
            first_indexes, next_indexes = self.data.get_training_data()
            probabilities = self.model(first_indexes)

            num_inputs = len(first_indexes)
            # nlls = torch.zeros(num_inputs)

            # for index in range(num_inputs):
            #     first_index = first_indexes[index].item()
            #     next_index = next_indexes[index].item()
            #     # print(f"bigram: {itos[x]}{itos[y]}, index: {x}, {y}")
            #     nlls[index] = -torch.log(probabilities[first_index, next_index])

            # print(f"average negative log likelihood, i.e. loss =  {nlls.mean().item():.4f}")

            loss = -probabilities[torch.arange(num_inputs), next_indexes].log().mean()

            if iteration % 1000 == 0:
                print(f"Iteration {iteration} loss =  {loss.item():.6f}")
                print(self.model.weights[0, :5].data)

            # backward pass
            self.model.weights.grad = None
            loss.backward()

            # update the weights
            self.model.weights.data -= 50 * self.model.weights.grad
