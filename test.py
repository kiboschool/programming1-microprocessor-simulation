import os
entries = os.scandir('check_dir/')
print(entries)

with os.scandir('check_dir/') as entries:
    for entry in entries:
        print(entry.name)