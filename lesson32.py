import random


def get_random_string(length: int) -> str:
    my_str = ''

    for _ in range(length):
        rand_ascii = random.randint(48, 122)
        while not (48 <= rand_ascii <= 57 or 65 <= rand_ascii <= 90 or 97 <= rand_ascii <= 122):
            rand_ascii = random.randint(48, 122)
        my_str += chr(rand_ascii)

    return my_str


print(get_random_string(10))
