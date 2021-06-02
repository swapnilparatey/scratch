import re

google_api_stonk_commands = []

file = open("stonks.txt",'r')
for line in file:
    command = '=index(GOOGLEFINANCE(\"' + line.strip('\n') + '\","price",A8),2,2)'
    google_api_stonk_commands.append(command)
    print(command)
