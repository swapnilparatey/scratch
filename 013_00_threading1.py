# Extremely basic threading example
import threading

number_of_threads = 9
x = []

def poorly_written_function():
    print("What the fuck is this")

for i in range(number_of_threads):
    x.append(threading.Thread(target=poorly_written_function, args=()))
    x[i].start()
    x[i].join()

print("Work is finished hahaha")
print(x)
