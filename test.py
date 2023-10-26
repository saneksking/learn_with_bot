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
    def save_password(secret, password):
        passwords = {}
        passwords[secret] = password
        return passwords


class GetPassword(CreatePass):
    @staticmethod
    def get_pass(secret):
        secret_words = input('Введите секретную фразу: ')
        # for key in :


print("Saneks's pass gen - приложение для генерации сложных паролей")
print('*' * 80)
while 1:
    menu = int(input('Что вы собираетесь сделать: \b 1 - Создать пароль, 2 - Получить пароль: '))
    if menu == 1:
        pass_len = int(input('Введите длину пароля: '))
        create = CreatePass(password_len=pass_len)
        secret_word = CreatePass.create_secret_word()
        save = CreatePass.save_password(secret=secret_word, password=create.create_password())
    elif menu == 2:
        pass
    break






