import multiprocessing, time

ret = [1,2,3]

def worker(queue):
    while True:
        ret = queue.get(block=False)
        ret[1] += 1
        queue.put(ret, block=False)
        time.sleep(1)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    queue.put(ret, block=False)
    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()
    while True:
        time.sleep(2)
        print(queue.get(block=False)) 


# from random import random
# from time import sleep
# from multiprocessing import Value
# from multiprocessing import Process
 
# def task(variable):
#     while True:
#         variable.value += 1
#         sleep(1)
 
# if __name__ == '__main__':
#     variable = Value('f', 0.0)
#     process = Process(target=task, args=(variable,))
#     process.start()
#     while True:
#         print(f'Returned: {variable.value}')
#         sleep(2)