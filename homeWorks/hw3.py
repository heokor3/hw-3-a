class Bank:
    def __init__(self, name, balanse):
        self._name = name
        self._balanse = balanse

    def moneyX(self):
        add = int(input('Введите сумму которую хотите добавить на свой счёт: '))
        self._balanse += add
        print(f'Счёт пополнен на: {self._balanse}')

    def kill(self):
        return self._balanse - self._balanse

    def __jackpot(self):
        self._balanse *= 10

    def __str__(self):
        return f'Имя: {self._name}\n' \
               f'Баланс: {self._balanse}'

    def __unite_balanse(self, other):
        self._balanse += other.balanse


me = Bank(name="Daniel", balanse=100)
you = Bank(name="Eldar", balanse=100)

print(me._balanse)
print(you._balanse)


class Gs(Bank):
    def __init__(self, name, balanse):
        super().__init__(name, balanse)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_balanse(self):
        return self._balanse

    def set_balanse(self, balanse):
        self._balanse = balanse


class Lambada(Bank):
    def __init__(self, name, balanse):
        super().__init__(name, balanse)

    @property
    def gotname(self):
        return f"I'm {self._name} "

    @property
    def gotbalanse(self):
        return f'balanse: {self._balanse}'


a = Lambada("Victor", 200)
b = Gs("igor", 100)
print(a.gotbalanse)
print(a.gotname)
print(b.kill())
print(b.set_balanse(120))
