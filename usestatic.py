class Methods:
    def imeth(self, x): # Нормальный метод экземпляра 
        print([self, x])
    def smeth(x): # Статический метод: экземпляр не передается
        print([x])
    def cmeth(cls, x): # Метод класса: получает класс, а не экземпляр
        print([cls,x])

smeth = staticmethod(smeth) # Делает smeth статическим методом(или @: впереди)
cmeth = classmethod(cmeth) # Делает smeth методом класса (или @: впереди)

obj = Methods() # Допускает вызов через экземпляр или класс
obj.imeth(1)
Methods.imeth(obj, 2)

Methods.smeth(3) # Статический метод: вызов через класс
# [3] # Экземпляр не передается и не ожидается
obj.smeth(4) # Статический метод: вызов через экземпялр 
# 4 # Экзмепляр не передается
Methods.cmeth(5) # Метод класса: вызывается через класс
# Превращается в cmeth(Methods, 5)
obj.cmeth(6) # Метод класса: вызывается через экземпляр
# Превращается в cmeth(Methods, 6)
