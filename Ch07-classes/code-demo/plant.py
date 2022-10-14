"""An OO programming demo
Your garden may have plants and some flowers. 
A plant has a name and a cost.
A flower si a plant with an extra color attribute.
Both plant and flower have a print_info method that prints their attributes.

The application asks a user to input a plant or a flower and 
its attributtes, adds it to my_garden.
When the user inputs 'done', print the attributes of each plant/flower
and exit.
"""


class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print('Plant Information:')
        print('   Plant name:', self.plant_name)
        print('   Cost:', self.plant_cost)


class Flower(Plant):
    def __init__(self, plant_name, plant_cost, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        super().print_info()
        print('   Color of flowers:', self.color_of_flowers)


def print_list(my_garden):
    for i in range(len(my_garden)):
        my_garden[i].print_info()
        print()


if __name__ == "__main__":
    my_garden = []
    user_select = input(
        'Please input plant or flower, or done to complete: ')
    while user_select != 'done':
        if user_select == 'plant':
            user_string = input('Please input name cost: ')
            tokens = user_string.split()
            name = tokens[0]
            cost = tokens[1]
            my_plant = Plant(name, cost)
            my_garden.append(my_plant)
        elif user_select == 'flower':
            user_string = input('Please input name cost color: ')
            tokens = user_string.split()
            name = tokens[0]
            cost = tokens[1]
            color = tokens[2]
            my_flower = Flower(name, cost, color)
            my_garden.append(my_flower)

        user_select = input(
            'Please input plant or flower, or done to complete: ')

    print_list(my_garden)
