
def split_front(list, index):
    return list[:index]


def split_back(list, index):
    return list[index:]


def get_row_value(input_list):
    row_list = []
    for value in input_list:
        updated_val = list(range(128))
        index = 64
        for i in range(0,7): 
            if value[i] == "F":
                updated_val = split_front(updated_val, index)
            if value[i] == "B":
                updated_val = split_back(updated_val, index)
            index = int(index / 2)
        row_list.append(updated_val[0])
    return row_list


def get_seat_value(input_list):
    seat_list = []
    for value in input_list:
        updated_val = list(range(8))
        index = 4
        for i in range(7,10):
            if value[i] == "L":
                updated_val = split_front(updated_val, index)
            if value[i] == "R":
                updated_val = split_back(updated_val, index)
            index = int(index / 2)
        seat_list.append(updated_val[0])
    return seat_list


def calculate_id_vals(row_list, seat_list):
    id_vals = []
    for i in range(len(row_list)):
        id_val = row_list[i] * 8 + seat_list[i]
        id_vals.append(id_val)
    return id_vals


def find_seat(id_vals):
    sort_ids = sorted(id_vals)
    lower_seat = 0
    upper_seat = 0
    for i in range(len(sort_ids[:-1])):
        if sort_ids[i] - sort_ids[i - 1] > 1:
            lower_seat = sort_ids[i-1]
            upper_seat = sort_ids[i]
            break
    return int((upper_seat + lower_seat) / 2)



if __name__ == '__main__':
    input_path = "/Users/sophia/advent_2020/input_5.txt"
    input_txt = open(input_path, "r").read().strip()
    input_list = input_txt.split("\n")
    row_list = get_row_value(input_list)
    seat_list = get_seat_value(input_list)
    id_vals = calculate_id_vals(row_list, seat_list)
    max_id = max(id_vals)
    my_seat = find_seat(id_vals)
    print(max_id)
    print(my_seat)
