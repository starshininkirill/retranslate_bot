import time
# from datetime import *
#
# print(datetime.now())

named_tuple = time.localtime()
start_time = '00:00:00'
end_time = '23:30:00'
now = time.strftime("%H:%M:%S", time.localtime())

if start_time <= now <= end_time:
    print('Время в диапазоне')
elif start_time == end_time:
    print('Работает круглосуточно')
else:
    print('Время вне диапазона')