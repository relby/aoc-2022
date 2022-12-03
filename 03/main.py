from string import ascii_lowercase, ascii_uppercase


def priority(item: str):
    if item in ascii_lowercase:
        return ord(item) - ord('a') + 1
    if item in ascii_uppercase:
        return ord(item) - ord('A') + 27
    raise ValueError('Unexpected item')


def part1(rucksacks: list[str]) -> int:
    items: list[str] = []
    for rucksack in rucksacks:
        middle = len(rucksack)//2
        left_compartments = set(rucksack[:middle])
        right_compartments = set(rucksack[middle:])
        items.append(
            tuple(left_compartments & right_compartments)[0],
        )
    return sum(priority(item) for item in items)


def part1_functional(rucksacks: list[str]) -> int:
    def get_common(rucksack: str):
        middle = len(rucksack)//2
        left_compartments = set(rucksack[:middle])
        right_compartments = set(rucksack[middle:])
        return tuple(left_compartments & right_compartments)[0]
    return sum(priority(get_common(rucksack)) for rucksack in rucksacks)


def main() -> None:
    with open('input.txt') as input_file:
        rucksacks = input_file.readlines()
    print('Part 1:', part1(rucksacks))


if __name__ == '__main__':
    main()
