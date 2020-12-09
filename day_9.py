def validate_sequence(input_list):
    invalid_val = 0
    for index in range(25, len(input_list)):
        valid_list = input_list[index-25:index]
        value_to_check = input_list[index]
        is_valid = False
        for val in valid_list:
            diff = int(value_to_check) - int(val)
            if str(diff) in valid_list:
                is_valid = True
                break
        if not is_valid:
            invalid_val += int(value_to_check)
    return invalid_val


def find_contiguous_sum(input_list, invalid_val):
    valid_sum = 0
    for jump_size in range(10, 20):
        for index in range(jump_size, len(input_list)):
            valid_list = input_list[index - jump_size:index]
            int_list = [int(v) for v in valid_list]
            if sum(int_list) == invalid_val:
                valid_sum += min(int_list) + max(int_list)
                break
    return valid_sum





if __name__ == '__main__':
    input_path = "/Users/sophia/advent_2020/input_9.txt"
    input_txt = open(input_path, "r").read().strip()
    input_list = input_txt.split("\n")
    invalid_val = validate_sequence(input_list)
    weakness = find_contiguous_sum(input_list, invalid_val)
    print(weakness)