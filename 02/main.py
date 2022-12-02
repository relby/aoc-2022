from types import MappingProxyType
from typing import Final

POINTS: Final = MappingProxyType({
    'A': 1,
    'B': 2,
    'C': 3,
})
WIN_CONDITIONS: Final = MappingProxyType({
    'A': 'C',
    'B': 'A',
    'C': 'B',
})
CRYPT_DIFFERENCE: Final = ord('X') - ord('A')


def decrypt(letter: str) -> str:
    return chr(ord(letter) - CRYPT_DIFFERENCE)


def part1(lines: list[str]) -> int:
    points = 0
    for line in lines:
        left, right = line.strip().split()
        decrypted_right = decrypt(right)

        if decrypted_right == left:
            points += 3
        elif WIN_CONDITIONS[decrypted_right] == left:
            points += 6
        points += POINTS[decrypted_right]
    return points


def part2(lines: list[str]) -> int:
    points = 0
    for line in lines:
        left, right = line.strip().split()
        match right:
            case 'X':  # lose
                points += POINTS[WIN_CONDITIONS[left]]
            case 'Y':  # draw
                points += 3 + POINTS[left]
            case 'Z':  # win
                points += 6 + POINTS[
                    list(WIN_CONDITIONS.keys())[
                        list(WIN_CONDITIONS.values()).index(left)
                    ]  # gets a key by value
                ]
    return points


def main() -> None:
    with open('input.txt') as input_file:
        lines = input_file.readlines()
    print('Part 1: {0}'.format(part1(lines)))
    print('Part 2: {0}'.format(part2(lines)))


if __name__ == '__main__':
    main()
