data = input()

hour = int(data.split()[0])
minute = int(data.split()[1])

minus = 45


def calculate_alarm_time(hour:int, minute:int) -> str :
    minute -= minus
    if minute < 0:
        minute += 60
        hour -= 1
        if hour < 0:
            hour = 23

    return f"{hour} {minute}"


print(calculate_alarm_time(hour, minute))