import os

with os.scandir('samples/') as entries:
    for entry in entries:
        print(entry.name)
