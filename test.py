import random
from smartrandom.random_master import RandomMaster


"""Saneks's pass gen - приложжение для генерации сложных паролей"""


class CreatePass:
    def __init__(self, password_len):
        self.password_len = password_len

    def create_password(self):
        chars = ''.join(random.choice('\n!@#$%^&*()_+{}:"><,.;=-"№;:?') for _ in range(self.password_len))
        letters = RandomMaster.string.get(length=self.password_len)
        numbers = str(RandomMaster.number.get(length=self.password_len))
        return ''.join(random.choice(chars + letters + numbers) for _ in range(self.password_len))

    @staticmethod
    def create_secret_word():
        return input('Введите секретную фразу: ')

    @staticmethod
    def get_password(password):
        for keys, values in password:
            if password == keys:
                print(values)
            else:
                print('Неверная секретная фраза, попробуйте ещё раз!')
                continue

    @staticmethod
    def save_password(secret, password):
        passwords = {secret: password}
        return passwords




print("Saneks's pass gen - приложжение для генерации сложных паролей")
print('*' * 80)
print('1 - Получить пароль; 2 - Сгенерировать пароль; 3 - Выйти')
choice = int(input('Выберете то, что вы хотите сделать: '))
while 1:
    def menu():
        if choice == 1:
            pass
        elif choice == 2:
            return choice

    if menu() == 1:
        get = CreatePass.get_password(password=CreatePass.save_password())
    elif menu() == 2:
        choice1 = int(input('Выберете что вы хотите сделать: \b 1 - Получить пароль 2 - Создать пароль: \b'))
        if choice1 == 1:
            pass
        elif choice1 == 2:
            pass_len = int(input('Введите длину пароля: '))
            create = CreatePass(password_len=pass_len)
            secret_word = CreatePass.create_secret_word()
            print(f'Ваш пароль: {create.create_password()}')
            break
    else:
        break



