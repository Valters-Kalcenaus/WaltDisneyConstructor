import os
COUNTER_PATH = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + 'scriptUseCounter.txt'


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