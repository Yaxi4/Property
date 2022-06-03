class AlfaBank:  # Обьявили класс
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # работать с balance можно будет только внутри класса

    def get_balance(self):  # при вызове данной функции мы получим значение в атрибуте __balance
        return self.__balance

    def set_balance(self, value):  # через set будем устанавливать значения в атрибут __balance
        if not isinstance(value, (int, float)):  # проверка того, что значение в __balane только число
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):  # функция по удалению атрибута __balance
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance,
                       fdel=delete_balance)  # дает упрощение для вышеобозначенных функций
a= AlfaBank('Яхия', 500) # создали экземпляр а, и присвоили значения 'Яхия' и 500 атрибутам name и __balance соответственно
del a.balance # удалили __balance
a.balance=450 # присвоили (и автоматом создали, т.к. __balance удалялся, атрибут __balance) значение 450 атрибуту __balance
print(a.balance) # вывод значение в атрибуте __balance