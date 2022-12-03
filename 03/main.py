from string import ascii_lowercase, ascii_uppercase


# Part 1
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


# Part 2
def chunks(lst: list, n: int) -> list[list]:
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def part2(rucksacks: list[str]) -> int:
    items: list[str] = []
    for group in chunks(rucksacks, 3):
        items.append(
            tuple(set(group[0])
                  & set(group[1])
                  & set(group[2]))[0]
        )
    return sum(priority(item) for item in items)


def main() -> None:
    with open('input.txt') as input_file:
        rucksacks = [line.strip() for line in input_file.readlines()]
    print('Part 1:', part1(rucksacks))
    print('Part 2:', part2(rucksacks))


if __name__ == '__main__':
    main()
