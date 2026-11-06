import threading
import time


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


def calculate_fibonacci(n, results):
    results[n] = fibonacci(n)


results = {}
multiThreadTime = []
normalTime = []

for i in range(10):
    thread1 = threading.Thread(target=calculate_fibonacci, args=(35, results))
    thread2 = threading.Thread(target=calculate_fibonacci, args=(38, results))
    thread3 = threading.Thread(target=calculate_fibonacci, args=(40, results))
    Start_Time_Of_Thread_That_Started_First = time.perf_counter_ns()

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    End_Time_Of_Thread_Finished_Last = time.perf_counter_ns()

    Time_Elapsed = End_Time_Of_Thread_Finished_Last - Start_Time_Of_Thread_That_Started_First
    multiThreadTime.append(Time_Elapsed)

print(f"=== Fibonacci Computation (With Multithreading) ===")
for i in range(3):
    print(f"Round {i+1} : Fib(35)={results[35]}, Fib(38)={results[38]}, Fib(40)={results[40]} | T = {multiThreadTime[i]} ns")
print(f"...")
print(f"Round 10 : Fib(35)={results[35]}, Fib(38)={results[38]}, Fib(40)={results[40]} | T = {multiThreadTime[9]} ns")

total = 0
for x in multiThreadTime:
    total += x
print(f"Average T (With Multithreading)\t\t: {total/10} ns")

for i in range(10):
    Start_Time_Of_First = time.perf_counter_ns()

    calculate_fibonacci(35, results)
    calculate_fibonacci(38, results)
    calculate_fibonacci(40, results)

    End_Time_Last = time.perf_counter_ns()

    Time_Elapsed = End_Time_Last - Start_Time_Of_First
    normalTime.append(Time_Elapsed)

print(f"\n=== Fibonacci Computation (Without Multithreading) ===")
for i in range(3):
    print(f"Round {i+1} : Fib(35)={results[35]}, Fib(38)={results[38]}, Fib(40)={results[40]} | T = {normalTime[i]} ns")
print(f"...")
print(f"Round 10 : Fib(35)={results[35]}, Fib(38)={results[38]}, Fib(40)={results[40]} | T = {normalTime[9]} ns")

normalTotal = 0
for x in normalTime:
    normalTotal += x
print(f"Average T (Without Multithreading)\t: {normalTotal/10} ns")
