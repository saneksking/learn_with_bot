import random
import string


"""Saneks's pass gen - приложжение для генерации сложных паролей"""


class CreatePass:
    letters = string.ascii_letters

    def __init__(self, password_len):
        self.password_len = password_len

    def create_pass(self, cls):
        return ''.join((random.choice(cls.letters) for _ in range(self.password_len)))


print("Saneks's pass gen - приложжение для генерации сложных паролей")
print('*' * 80)
while 1:
    try:
        def menu():
            print('1 - Получить пароль; 2 - Сгенерировать пароль; 3 - Выйти')
            choice = int(input('Выберете то, что вы хотите сделать: '))
            if choice == 1:
                pass
            elif choice == 2:
                return choice
            else:
                pass


        if menu() == 1:
            pass
        elif menu() == 2:
            pass_len = input('Введите длину пароля: ')
            create = CreatePass(pass_len)
            print(create.create_pass())


        elif menu() == 3:
            pass

    except ValueError:
        continue
