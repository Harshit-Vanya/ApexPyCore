# For all exercises use Queue class implemented in main tutorial.

# Design a food ordering system where your python program will run two threads,

# Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
# Use this video to get yourself familiar with multithreading in python

# Pass following list as an argument to place order thread,

# orders = ['pizza','samosa','pasta','biryani','burger']
# This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.

# from collections import deque
# import time
# import threading

# class Queue:
    
#     def __init__(self):
#         self.buffer = deque()
    
#     def enqueue(self, val):
#         self.buffer.appendleft(val)
        
#     def dequeue(self):
#         return self.buffer.pop()
    
#     def is_empty(self):
#         return len(self.buffer)==0
    
#     def size(self):
#         return len(self.buffer)
    
# Orderlist = Queue()   

# def Place_order(orders):
#     for i in orders:
#         time.sleep(0.5)
#         Orderlist.enqueue(i)

    
        
# def Serve_order():
#     time.sleep(1.0)
#     count = Orderlist.size()
#     for i in range(count):
#         time.sleep(2.0)
#         Orderlist.dequeue()
#     return "All orders are being served!!"

# if __name__ == '__main__':
    
#     orders = ['pizza','samosa','pasta','biryani','burger']
#     t1 = threading.Thread(target=Place_order,args=(orders,))
#     t2 = threading.Thread(target=Serve_order)
    
#     t = time.time()
#     t1.start()
#     t2.start()
    
#     t1.join()
#     t2.join()
#     # t = time.time()
#     # count = Place_order(orders)
#     # print(Serve_order(count))
    
    
#     print("taken :",time.time() -t,"sec")
    
    
# Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,

#     1
#     10
#     11
#     100
#     101
#     110
#     111
#     1000
#     1001
#     1010
    
    
    
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")
        print("   ", front)
        numbers_queue.dequeue()


if __name__ == '__main__':
    produce_binary_numbers(10)
    
    
    
    
    
    
    