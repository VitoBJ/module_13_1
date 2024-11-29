import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for i in range(1, 6):

        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар.')

    print(f'Силач {name} закончил соревнования.')

async def start_tournament():

    tasks = [
        start_strongman("Иван", 10),
        start_strongman("Петр", 20),
        start_strongman("Сергей", 15)
    ]


    await asyncio.gather(*tasks)


asyncio.run(start_tournament())