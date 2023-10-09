import random
import string

for i in str(range(10)):
    x = ''.join(random.choice('\n!@#$%^&*()_+{}:"><,.;=-"№;:?'))
    print(x)


class RandomStringMaster:
    letters = string.ascii_letters

    @classmethod
    def get(cls, length=10):
        return ''.join((random.choice(cls.letters) for _ in range(length)))


x = RandomStringMaster.get()
print(x)