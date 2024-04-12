# import contextlib
#
#
# @contextlib.contextmanager
# def my_context():
#     print('Welcome!')
#     yield
#     print('Bye!')
#
#
# with my_context() as ctx:
#     print('I am always executed before the yield keyword\n')
# print('I am always executed after the yield keyword')
import time
import contextlib


# @contextlib.contextmanager
# def timer():
#     # Start the timer
#     start = time.time()
#     # context breakdown
#     yield
#     # End the timer
#     end = time.time()
#     # Tell the user how much time elapsed
#     print(f'This code block executed in {end - start} seconds.')
#
#
# with timer():
#     for i in range(10):
#         time.sleep(0.1)
# print('Done!')
# @contextlib.contextmanager
# def read_only(path_to_file):
#     # Open the file
#     file = open(path_to_file, 'r')
#     # Context breakdwon
#     yield file
#     # Close the file
#     file.close()
#
#
# with read_only('file.py') as file:
#     print('Printing the contents of the file\n')
#     print(file.read())


@contextlib.contextmanager
def add_one(number: int):
    num = number + 1
    yield num


with add_one(2) as n:
    print(n)


# @contextlib.contextmanager
# async def add_two(number: int):
#     yield number + 2
#
#
# async def add():
#     async with add_two(2) as added:
#         print(added)
#
#
#
# import asyncio
# asyncio.run(add)
