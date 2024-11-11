from datetime import datetime

birae = ["05:50", "06:25", "06:55", "07:25", "08:00", "08:34", "09:08", "09:44", "10:20",
         "10:56", "11:32", "12:08", "12:45", "13:22", "13:59", "14:36", "15:12", "15:47",
         "16:20", "16:53", "17:26", "18:00", "18:34", "19:08", "19:42", "20:16", "20:50",
         "21:24", "21:57", "22:30"]

panam = ["05:50", "06:20", "06:51", "07:25", "07:55", "08:25", "08:59", "09:33", "10:06",
         "10:42", "11:18", "11:54", "12:30", "13:06", "13:43", "14:20", "14:57", "15:34",
         "16:10", "16:46", "17:20", "17:54", "18:28", "19:04", "19:39", "20:14", "20:48",
         "21:22", "21:56", "22:30"]

"""def current_time_str():
    return current_time.strftime("%H:%M")

current_time = datetime.now().time()"""

def current_time():
    return datetime.now().time()

def current_time_str():
    return datetime.now().time().strftime("%H:%M")


def find_next_time(time_list):
    for time_str in time_list:
        time_obj = datetime.strptime(time_str, "%H:%M").time()
        if time_obj > current_time():
            return time_str
    return None

def find_previous_time(time_list):
    for time_str in reversed(time_list):
        time_obj = datetime.strptime(time_str, "%H:%M").time()
        if time_obj < current_time():
            return time_str
    return None

def next_birae_time():
    return find_next_time(birae)

def previous_birae_time():
    return find_previous_time(birae)

def next_panam_time():
    return find_next_time(panam)

def previous_panam_time():
    return find_previous_time(panam)
