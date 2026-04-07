import asyncio


# Example of Coroutine
async def my_coroutine():
    print("Start of coroutine")
    await asyncio.sleep(1)   # Pause of coroutine for 1 second
    print("End of coroutine")

# Make task from coroutine
async def main():
    task = asyncio.create_task(my_coroutine())
    await task

# Start of event loop
asyncio.run(main())