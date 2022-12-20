
def get_lines(filename: str) -> list:
    input_file = open(filename, "r")
    lines = input_file.readlines()
    return [line.strip() for line in lines]

def calculate_max_calories(lines: list) -> list:
    elfs_calories = 0
    elf_calorie_list = []

    for line in lines: 
        if line != '':
            elfs_calories += int(line)
        else:
            elf_calorie_list.append(elfs_calories)
            elfs_calories = 0
    return elf_calorie_list

if __name__ == "__main__":
    lines = get_lines("input.txt")
    print(max(calculate_max_calories(lines)))
    print(sum(sorted(calculate_max_calories(lines))[-3:]))