import numpy as np


def create_terrain(input_list):
    list_lists = []
    for row in input_list:
        row_list = [i for i in row]
        list_lists.append(row_list)
    terrain = np.array(list_lists)
    return terrain


def count_trees(terrain):
    part_1 = 0
    part_2 = 1
    descent_list = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    for vals in descent_list:
        col_mult, row_desc = vals
        num_trees = 0
        for row_index in range(0, terrain.shape[0], row_desc):
            column_index = int((row_index * col_mult / row_desc) % terrain.shape[1])
            landing_spot = terrain[row_index][column_index]
            if landing_spot == "#":
                num_trees += 1
        if vals == [3,1]:
            part_1 += num_trees
        part_2 *= num_trees
    return part_1, part_2


if __name__ == '__main__':
    input_path = "/Users/sophia/advent_2020/input_3.txt"
    input_txt = open(input_path, "r").read().strip()
    input_list = input_txt.split("\n")
    terrain = create_terrain(input_list)
    part_1, part_2 = count_trees(terrain)
    print(f"part 1: {part_1}, part 2: {part_2}")