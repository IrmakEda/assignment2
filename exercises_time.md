#Exercises with time
##1
def print_time(time):
    print("%.2d:%.2d:%.2d" % (time.hour, time.minutes, time.seconds))

##2
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.seconds
    return seconds

##3
def int_to_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    time = Time()
    time.hour = hours
    time.minute = minutes
    time.second = seconds
    return time

##4
def is_after(t1, t2):
    return time_to_int(t1) > time_to_int(t2)
