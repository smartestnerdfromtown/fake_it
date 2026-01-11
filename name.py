import random as rn

names = [
    "Alexander",
    "Dmitry",
    "Sergey",
    "Mikhail",
    "Andrey",
    "Nikolay",
    "Vladimir",
    "Pavel",
    "Ivan",
    "Roman",
]

surnames = [
    "Ivanov",
    "Petrov",
    "Smirnov",
    "Kuznetsov",
    "Popov",
    "Sokolov",
    "Lebedev",
    "Kozlov",
    "Novikov",
    "Morozov",
    "Volkov",
    "Fedorov",
    "Mikhailov",
    "Belov",
    "Tarasov",
    "Orlov",
    "Gusev",
    "Karpov",
    "Zaitsev",
    "Solovyov"
]

def generate_name() -> str:
    name = rn.choice(seq=names)
    return name

def generate_surname() -> str:
    surname = rn.choice(seq=surnames)
    return surname

def generate_fullname() -> str:
    return f"{generate_name()} {generate_surname()}"
