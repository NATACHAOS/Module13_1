import asyncio

"""Необходимо сделать имитацию соревнований по поднятию шаров Атласа.
Напишите асинхронную функцию start_strongman(name, power), где name - имя силача, power - его подъёмная мощность. 
Реализуйте следующую логику в функции:
В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>' 
с задержкой обратно пропорциональной его силе power. Для каждого участника количество шаров одинаковое - 5.
В конце поднятия всех шаров должна выводится строка 'Силач <имя силача> закончил соревнования.'
Также напишите асинхронную функцию start_tournament, в которой создаются 3 задачи для функций start_strongman. 
Имена(name) и силу(power) для вызовов функции start_strongman можете выбрать самостоятельно.
После поставьте каждую задачу в ожидание (await).
Запустите асинхронную функцию start_tournament методом run."""


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования")
    for i in range(5):
        numglob = i + 1
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {numglob} шар")
    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 4))
    task2 = asyncio.create_task(start_strongman('Denis', 6))
    task3 = asyncio.create_task(start_strongman('Apollon', 8))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
