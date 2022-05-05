import time
import matplotlib.pyplot as plt
import math
from multiprocessing import Process
import random

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    for i in range(len(arr)) :
        min_index = i
        for j in range(i+1, len(arr)) :
            if array[min_index] > arr[j] :
                min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

def shell_sort(arr):
    N = len(arr)
    h = N // 2
    while h > 0:
        for i in range(h, N):
            temp = arr[i]
            j = i - h
            while j >= 0 and arr[j] > temp:
                arr[j + h] = arr[j]
                j -= h
            arr[j + h] = temp
        h //= 2

def heap_sort(arr):
    heap = []
    for i in arr:
        heapq.heappush(heap, i)
    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

arr_data = []

bubble_t = []
select_t = []
insert_t = []
shell_t = []
heap_t = []
quick_t = []

n = int(math.pow(2,17))
array = []

for i in range(n):
    number = random.randrange(n)
    array.append(number)
   

for i in range(5, 17):
    n = int(math.pow(2,i))
    arr_data.append(n)
       
def fcn1(arr):
    for i in range(5,17):
        m = int(math.pow(2,i))
        
        t1 = time.time()
        bubble_sort(array[0:m])
        t2 = time.time()

        arr.append(t2-t1)
        print(i)

def fcn2(arr):
    for i in range(5,17):
        m = int(math.pow(2,i))
        
        t1 = time.time()
        selection_sort(array[0:m])
        t2 = time.time()
        arr.append(t2-t1)
        print(i)


def fcn3(arr):
    for i in range(5,17):
        m = int(math.pow(2,i))
        
        t1 = time.time()
        insertion_sort(array[0:m])
        t2 = time.time()
        arr.append(t2-t1)

def fcn4(arr):
    for i in range(5,17):
        m = int(math.pow(2,i))
        
        t1 = time.time()
        shell_sort(array[0:m])
        t2 = time.time()
        arr.append(t2-t1)

def fcn5(arr):
    for i in range(5,17):
        m = int(math.pow(2,i))
        
        t1 = time.time()
        heap_sort(array[0:m])
        t2 = time.time()
        arr.append(t2-t1)

def fcn6(arr):
    for i in range(5,17):
        m = int(math.pow(2,i))
        
        t1 = time.time()
        quick_sort(array[0:m])
        t2 = time.time()
        arr.append(t2-t1)

if __name__ == '__main__':
    start = time.time()
    p1 = Process(target = fcn1(bubble_t))
    p2 = Process(target = fcn2(select_t))
    p3 = Process(target = fcn3(insert_t))
    p4 = Process(target = fcn4(shell_t))
    p5 = Process(target = fcn5(heap_t))
    p6 = Process(target = fcn6(quick_t))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    end = time.time()

print(bubble_t)
print(select_t)
print(insert_t)
print(shell_t)
print(heap_t)
print(quick_t)
print(end-start)

plt.plot(arr_data, bubble_t)
plt.plot(arr_data, select_t)
plt.plot(arr_data, insert_t)
plt.plot(arr_data, shell_t)
plt.plot(arr_data, heap_t)
plt.plot(arr_data, quick_t)
plt.title('Random')
plt.xlabel("data") 
plt.ylabel("time")
plt.show()
   






