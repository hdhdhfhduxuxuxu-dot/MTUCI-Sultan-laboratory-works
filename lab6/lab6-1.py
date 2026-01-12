class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        return "Пароль изменен"

    def check_password(self, unpass):
        if unpass == self.__password:
            return True
        else:
            return False


userAccount1 = UserAccount("Vlad", "BlackGrow@gmail.com", "12345")

newpass = input("Новый пароль: ")
userAccount1.set_password(newpass)

trypass = input("Введите пароль: ")
print(userAccount1.check_password(trypass))
