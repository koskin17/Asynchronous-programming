import asyncio
# Defining an asynchronous function (coroutine) cook_dish(n), which simulates a cook preparing a dish
# Coroutines are used to run multiple "cooks" simultaneously and use the waiting time (cooking) efficiently.

async def cook_dish(n):
    print(f"Cook {n} starts cooking.") # The cook starts cooking.
    await asyncio.sleep(n) # The cook prepares the dish in n seconds. asyncio.sleep(n)  #used to simulate the delay required to cook a dish.
    print(f"Cook {n} finished cooking") # Cook finished cooking
    
    return f"Chef's special {n}" # Returns a string indicating that chef n's dish is ready.

# Create tasks from coroutines that represent the preparation of a dish by each chef
async def main():
    tasks = [asyncio.create_task(cook_dish(n)) for n in range(1, 4)] # Tasks are created for each cook (1 to 3). Create_task is used to start the coroutine.
    print(await asyncio.gather(*tasks)) # Waits for all tasks to complete, then prints the result. asyncio.gather is used to wait for all coroutines, then collects their results into a list.

# Starting the main coroutine
asyncio.run(main())