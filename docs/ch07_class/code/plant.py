"""An OO programming demo
Your garden may have plants and some flowers. 
A plant has a name and a cost.
A flower si a plant with an extra color attribute.
Both plant and flower have a print_info method that prints their attributes.

The application asks a user to input a plant or a flower and 
its attributes, adds it to my_garden.
When the user inputs 'done', print the attributes of each plant/flower
and exit.
"""


class Plant:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def print_info(self):
        print("Information:")
        print(f"    name: {self.name}")
        print(f"    cost: {self.cost}")


class Flower(Plant):
    def __init__(self, name, cost, color):
        super().__init__(name, cost)
        self.color = color

    def print_info(self):
        # super().print_info()
        print("Information:")
        print(f"    name: {self.name}")
        print(f"    cost: {self.cost}")
        print(f"    color: {self.color}")


# my_garden is list of plants/flowers


def print_list(my_garden):
    for element in my_garden:
        element.print_info()
        print("-" * 20)


if __name__ == "__main__":
    my_garden = []

    plant_prompt = "Please input plant or flower, or done to complete: "
    user_select = input(plant_prompt)

    while user_select != "done":
        if user_select == "plant":
            # input plant and add to my_garden
            user_input = input("Please input name cost: ")
            tokens = user_input.split()
            name = tokens[0]
            cost = tokens[1]
            plant = Plant(name, cost)
            my_garden.append(plant)

        elif user_select == "flower":
            # input flower and add to my_garden
            user_input = input("Please input name cost color: ")
            tokens = user_input.split()
            name = tokens[0]
            cost = tokens[1]
            color = tokens[2]
            flower = Flower(name, cost, color)
            my_garden.append(flower)

        else:
            print("wrong input, try again")

        user_select = input(plant_prompt)

    print_list(my_garden)
