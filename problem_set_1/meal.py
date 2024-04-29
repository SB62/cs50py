def main():
    hungry = input('What time is it? ')
    bld = convert(hungry)

    print(mealtime(bld))

def mealtime(meal):
    match meal:
        case meal if 7 <= meal <= 8:
            return ("breakfast time")
        case meal if 12 <= meal <= 13:
            return ("lunch time")
        case meal if 18 <= meal <=19:
            return ("dinner time")

def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)

    if 'a.m.' in minute or 'p.m.' in minute:
        minute, tod = minute.split(" ")

        if tod == 'p.m.' and hour < 12:
            hour = hour + 12

    if float(minute)/60:
        minute = float(minute)/60
    else:
        minute = 0

    rel_time = hour + minute
    return rel_time


if __name__ == "__main__":
    main()
