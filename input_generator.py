import random

CHUNK_SIZE = 10000
DUPLICATION_FACTOR = 10


if __name__ == '__main__':
    array = list(range(CHUNK_SIZE)) * DUPLICATION_FACTOR
    random.shuffle(array)

    with open('input.txt', 'w') as fp:
        fp.write(
            ' '.join(map(str, array))
        )
