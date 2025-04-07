class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    # Геттеры
    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory

    # Сеттеры
    def set_cpu(self, cpu):
        self.__cpu = cpu

    def set_memory(self, memory):
        self.__memory = memory

    # Метод вычислений
    def make_computations(self):
        return {
            "sum": self.__cpu + self.__memory,
            "difference": self.__cpu - self.__memory,
            "product": self.__cpu * self.__memory,
            "division": self.__cpu / self.__memory if self.__memory != 0 else None
        }

    # __str__ метод
    def __str__(self):
        return f"Computer(cpu={self.__cpu}, memory={self.__memory})"

    # Магические методы сравнения по memory
    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # Геттер и сеттер
    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # Метод call
    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_name = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_name}")
        else:
            print("Неверный номер сим-карты.")

    # __str__ метод
    def __str__(self):
        return f"Phone(sim_cards_list={self.__sim_cards_list})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    # Метод GPS
    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    # __str__ метод
    def __str__(self):
        return f"SmartPhone(cpu={self.get_cpu()}, memory={self.get_memory()}, sim_cards={self.get_sim_cards_list()})"


# Создание объектов
computer = Computer(cpu=4, memory=16)
phone = Phone(sim_cards_list=["Beeline", "O!"])
smartphone1 = SmartPhone(cpu=8, memory=32, sim_cards_list=["Megacom", "Beeline"])
smartphone2 = SmartPhone(cpu=6, memory=32, sim_cards_list=["O!", "Tele2"])

# Печать информации
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Использование методов
print("\n-- Метод make_computations у компьютера --")
print(computer.make_computations())

print("\n-- Метод call у телефона --")
phone.call(1, "+996 777 99 88 11")

print("\n-- Метод call и use_gps у смартфона --")
smartphone1.call(2, "+996 700 123 456")
smartphone1.use_gps("Ош")

# Проверка магических методов сравнения
print("\n-- Сравнение компьютеров по памяти --")
print("smartphone1 == smartphone2:", smartphone1 == smartphone2)
print("smartphone1 > smartphone2:", smartphone1 > smartphone2)
print("smartphone1 < smartphone2:", smartphone1 < smartphone2)
