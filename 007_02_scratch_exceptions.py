x = 10

try:
    x = x / 0
except Exception as e:
    print(e.args)
