from datetime import datetime

# Use "python gen_killswitch.py > files/killswitch.txt" to replace killswitch.
# example datetime: 2022-04-13T00:36:00
print(datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S"))
