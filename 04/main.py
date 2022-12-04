def part1(pairs: list[str]) -> int:
    count = 0
    for pair in pairs:
        left, right = (tuple(map(int, x.split('-'))) for x in pair.split(','))
        if left[0] <= right[0] and left[1] >= right[1]:
            count += 1
        elif right[0] <= left[0] and right[1] >= left[1]:
            count += 1
    return count


def part2(pairs: list[str]) -> int:
    count = 0
    for pair in pairs:
        left, right = sorted(
            tuple(map(int, x.split('-')))
            for x in pair.split(',')
        )
        if left[1] >= right[0]:
            count += 1
    return count


def main() -> None:
    with open('input.txt') as input_file:
        pairs = [line.strip() for line in input_file.readlines()]
    print('Part 1:', part1(pairs))
    print('Part 2:', part2(pairs))


if __name__ == '__main__':
    main()
