from datetime import datetime, timedelta

now = datetime.now()

print("now =", now)
task_time = int(input("Enter how long the task will take: "))
after = now + timedelta(minutes=task_time)
print("after =", after)
