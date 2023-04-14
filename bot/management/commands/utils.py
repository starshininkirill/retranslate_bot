import datetime as dt


def check_time(now, start_time, end_time):
    t_subzero = dt.time(hour=23, minute=59, second=59)
    t_zero = dt.time(hour=0, minute=0, second=0)
    if start_time > end_time:
        if t_subzero > now > start_time or t_zero < now < end_time:
            return True
    else:
        if start_time < now < end_time:
            return True
    return False

translate_dict = {
    'ru': {'up': 'вверх', 'down': 'вниз', 'm': 'м'},
    # 'en': {'вверх': 'up', 'вниз': 'down', 'м': 'm'}
}


def translate(text, source_lang, chanel_lang):
    res_text = []

    if text == '':
        return text

    if source_lang == chanel_lang:
        return text

    elif source_lang == 'en':
        text = text.split()
        for word in text:
            if word[0] == 'm':
                word = translate_dict[chanel_lang][word[0]] + word[1:]
                res_text.append(word)
            elif word == 'up' or word == 'down':
                res_text.append(translate_dict[chanel_lang][word])
            else:
                res_text.append(word)
        return ' '.join(res_text)


# now = dt.time(hour=23, minute=59, second=00)
# start_time = dt.time(hour=7, minute=10, second=0)
# end_time = dt.time(hour=4, minute=0, second=0)
# print(now < d_zero)
#
#
# check_time(now, start_time, end_time)


# def check_time(now, start_time, end_time):
#     res = []
#     if start_time > end_time:
#         for i in range(0, 24):
#             if int(end_time[3:5]) == 0:
#                 if i < int(end_time[0:2]):
#                     res.append(i)
#             else:
#                 if i <= int(end_time[0:2]):
#                     res.append(i)
#
#             if i >= int(start_time[0:2]):
#                 res.append(i)
#     else:
#         for i in range(0, 24):
#             if int(end_time[3:5]) != 0:
#                 if i >= int(start_time[0:2]) and i <= int(end_time[0:2]):
#                     res.append(i)
#             else:
#                 if i >= int(start_time[0:2]) and i < int(end_time[0:2]):
#                     res.append(i)
#     if int(now[0:2]) in res:
#         now_min = int(now[3:5])
#         start_min = int(start_time[3:5])
#         end_min = int(end_time[3:5])
#         if int(now[0:2]) == res[0]:
#             if now_min > start_min or start_min == 0:
#                 return True
#         elif int(now[0:2]) == res[-1]:
#             if now_min < end_min or end_time == 0:
#                 return True
#         else:
#             return True
#     return False