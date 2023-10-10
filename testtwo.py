import random
import string

x = ''.join(random.choice('\n!@#$%^&*()_+{}:"><,.;=-"№;:?') for _ in range(1, 10))
print(x)


class RandomStringMaster:
    letters = string.ascii_letters


    @classmethod
    def get(cls, length=10):
        return ''.join((random.choice(cls.letters) for _ in range(length)))


x = RandomStringMaster.get()
print(x)
