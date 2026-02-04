# import asyncio
# import time

# async def fetch_data(id, delay):
#     print(f"Task {id}: Starting (will take {delay}s)...")
#     # cedes control to event loop
#     await asyncio.sleep(delay) 
#     print(f"Task {id}: Finished!")
#     return f"Data {id}"

# async def main():
#     start_time = time.perf_counter()
    
#     # asyncio.gather schedules both tasks concurrently
#     print("Main: Starting concurrent tasks...")
#     results = await asyncio.gather(
#         fetch_data(1, 3),
#         fetch_data(2, 4)
#     )
    
#     end_time = time.perf_counter()
#     print(f"Results: {results}")
#     print(f"Total time elapsed: {end_time - start_time:.2f} seconds")

# # asyncio.run handles the event loop setup and teardown
# asyncio.run(main())



# from tqdm import tqdm
# import time

# my_list = [1, 2, 3, 4, 5]

# # Wrap the iterable with tqdm()
# for item in tqdm(my_list, desc="Processing items"):
#     # Simulate some work
#     time.sleep(0.5)
#     # Your code here
#     pass

from calculator import functions
print(functions.add(2,4))
print(functions.subtract(4,3))
print(functions.divide(10,2))



print("Done processing.")
