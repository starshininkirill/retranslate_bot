import datetime
import time
from datetime import *
from datetime import time, datetime
from django.core.management.base import BaseCommand
# from ...models import *


# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         chanels = Chanel.objects.filter(type='dependent', active=True)
#         for chanel in chanels:
#             start_time = chanel.start_time
#             end_time = chanel.end_time
#             now = datetime.now()
#             now = now.time()
#             print(start_time < now < end_time)

# print(time.localtime())
# print(datetime.now() + timedelta(hours=3))

# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         named_tuple = time.localtime()
#         start_time = '00:00:00'
#         end_time = '23:30:00'
#         now = time.strftime("%H:%M:%S", time.localtime())
#         print(f'start: {start_time}, end: {end_time}, now:{now}')
#


now = datetime.now() + timedelta(hours=3)
now = datetime.now()
now = now.strftime("%H:%M:%S")
start_time = '08:00:00'
end_time = '01:09:00'
print(now)

def check_time(now_time, start_time, end_time):
    res = []
    if start_time > end_time:
        for i in range(0, 24):
            if int(end_time[3:5]) == 0:
                if i < int(end_time[0:2]):
                    res.append(i)
            else:
                if i <= int(end_time[0:2]):
                    res.append(i)

            if i >= int(start_time[0:2]):
                res.append(i)

    else:
        for i in range(0, 24):
            if int(end_time[3:5]) != 0:
                if i >= int(start_time[0:2]) and i <= int(end_time[0:2]):
                    res.append(i)
            else:
                if i >= int(start_time[0:2]) and i < int(end_time[0:2]):
                    res.append(i)
    if int(now[0:2]) in res:
        now_min = int(now[3:5])
        start_min = int(start_time[3:5])
        end_min = int(end_time[3:5])
        if now_min > start_min or start_min == 0:
            if now_min < end_min or int(end_min) == 0:
                return True

    return False
# check_time(now, start_time, end_time)
print(check_time(now, start_time, end_time))
# if int(now[0:2]) in res:
#     now_min = int(now[3:5])
#     start_min = int(start_time[3:5])
#     end_min = int(end_time[3:5])
#     if now_min > start_min:
#         print('Норм')
#     elif now_min < end_min:
#         print('Норм')
#     else:
#         print('Хуйня')
    # print(start_min, end_min)
    # if start_time > end_time:
    #     for i in range(0, 60):
    #         if i >= int(start_time[3:5]):
    #             min.append(i)
    #         if i < int(end_time[3:5]):
    #             min.append(i)
    # else:
    #     for i in range(0, 24):
    #         if i >= int(start_time[0:2]) and i < int(end_time[0:2]):
    #             res.append(i)
#     print('В диапозоне')
# else:
#     print('Вне диапазона')
# def check_time(start, end, now):
#     if start > end:
#         if start < now > end:
#             print('true')
#             return True
#         else:
#             print('false')
#             return False
#     else:
#         if start < now < end:
#             return True
#         else:
#             return False

# print(check_time(start_time, end_time, now))


