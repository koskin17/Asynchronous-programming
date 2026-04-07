# Await используется:
# 
# 1 Когда нужно дождаться завершения асинхронной операции (чтений / запись в сеть или в файл или другие длительные операции)

import aiohttp
import asyncio


async def fetch_data(url): # This function is an asynchronous function that takes a URL as an argument and fetches data from that URL using the aiohttp library. It creates an asynchronous HTTP session, sends a GET request to the specified URL, and returns the response text.
    async with aiohttp.ClientSession() as session:  # Making asynchronous session to send HTTP requests and with optimal resource management. The session will be automatically closed after the block is executed.
        async with session.get(url) as response:    # Making asynchronous GET request to the specified URL. The response is awaited, meaning the function will pause until the response is received and don't block the event loop while waiting.
            return await response.text()    # Return text answer after receiving all data from the response. The await keyword is used to wait for the response text to be fully received before returning it.
        
async def main():
    data = await fetch_data("http://python.org")  # Calling the fetch_data function with the URL "http://python.org" and awaiting its result. The main function will pause until the data is fetched before proceeding.
    print(data)  # Print the fetched data to the console.

asyncio.run(main())

# 2. Когда нужно дождаться выполнения асинхронной функции, которая возвращает объект, который можно ожидать или которая вызывается внутри другой асинхронной функции.
async def cook_pasta():
    print("Start cooking pasta...")
    await asyncio.sleep(1)
    print(1)
    await asyncio.sleep(1)
    print(2)
    await asyncio.sleep(1)
    print(3)
    await asyncio.sleep(1)
    print(4)
    print("Cooking of pasta is done!")
    print()

async def main():
    await cook_pasta()

asyncio.run(main())

# 3. Когда нужно ждать завршения асинхронной функции, которая вызывается с помощью asyncio.ensure_future() или asyncio.create_task().
# Это аналогичный пример предыдущего, только вместо корутины создаётся задача, которая выполняется в фоновом режиме, и мы можем ожидать её завершения с помощью await.
async def cook_pasta():
    print("Start cooking pasta...")
    await asyncio.sleep(5)
    print("Cooking of pasta is done!")

async def main():
    task = asyncio.create_task(cook_pasta())
    await task

asyncio.run(main())

#4. Когда ожидается завершение нескольких асинхронных операций с помощью asyncio.gather(*aws).
async def cook_pasta():
    print("Start cooking pasta...")
    print(1)
    await asyncio.sleep(1)
    print(2)
    await asyncio.sleep(1)
    print(3)
    await asyncio.sleep(1)
    print(4)
    await asyncio.sleep(1)
    print(5)
    await asyncio.sleep(1)
    print("Cooking of pasta is done!")
    print()

async def cook_sauce():
    print("Start cooking sauce...")
    print(1)
    await asyncio.sleep(1)
    print(2)
    await asyncio.sleep(1)
    print(3)
    await asyncio.sleep(1)
    print("Cooking of sauce is done!")
    print()

async def main():
    await asyncio.gather(cook_pasta(), cook_sauce())

asyncio.run(main())

# 5. Когда ожидается завершение асинхронного контекстного менеджера async with
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    data = await fetch_data('http://python.org')
    print(data)

asyncio.run(main())