import time

# ver: 1
start_time = time.time()
time.sleep(3)
print(f'Прошло {time.time() - start_time}')

# ver: 2 better
start_time = time.monotonic()
time.sleep(3)
print(f'Прошло {time.monotonic() - start_time}')
