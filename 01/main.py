def part1(text: str) -> int:
    elf_calories = (
        sum(map(int, elf.split()))
        for elf in text.split('\n\n')
    )
    return max(elf_calories)


def part2(text: str) -> int:
    elf_calories = (
        sum(map(int, elf.split()))
        for elf in text.split('\n\n')
    )
    return sum(sorted(elf_calories, reverse=True)[:3])


def main() -> None:
    with open('input.txt') as input_file:
        text = input_file.read()
    print('Part 1: {0}'.format(part1(text)))
    print('Part 2: {0}'.format(part2(text)))


if __name__ == '__main__':
    main()
