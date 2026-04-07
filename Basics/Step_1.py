# Пример асихронной функции, которая выводит "Hello...", затем ждет 1 секунду и выводит "World!".

import asyncio


async def mail():
    print('Hello...')
    await asyncio.sleep(1)
    print('World!')

asyncio.run(mail())