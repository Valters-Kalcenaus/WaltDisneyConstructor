import os
from typing import Counter
COUNTER_PATH = os.path.expanduser("~/my_secret_files") + "/scriptUseCounter.txt"
print (COUNTER_PATH)


def operation_counter():
  if os.path.exists(COUNTER_PATH):
    with open(COUNTER_PATH, 'r+') as f:
      count = int(f.read())
      f.seek(0)
      count += 1
      f.write(str(count))
      f.truncate()
  else:
    with open(COUNTER_PATH, 'w') as f:
      f.write('1')

operation_counter()