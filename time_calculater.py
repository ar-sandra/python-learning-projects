def switch_m(am_or_pm):          
   
    if am_or_pm == 'AM':
        return 'PM'
    else:
        return 'AM'
    return 'AM' if am_or_pm=='PM' else 'PM'


def split_time(time):
    a,b=time.split(':')
    return int(a),int(b)


days={'0':'Noday','1':'Monday','2':'Tuesday','3':'Wednesday','4':'Thursday','5':'Friday','6':'Saturday','7':'Sunday'}


def find_day(d,day='Noday'):
    for key, value in d.items():
        if value == day:
            return int(key)

def add_time(start, duration, day='Noday'):

    start_time, m = start.split()
    start_hr,start_mn = split_time(start_time)

    add_hr,add_mn = split_time(duration)

    final_min = (start_mn + add_mn) % 60
    total_hr = start_hr + add_hr + (start_mn + add_mn)//60
    final_hr = total_hr % 12

    if m == 'AM':
        hr_format = total_hr % 24
        n_days = total_hr // 24
    else:
        hr_format = (total_hr + 12) % 24
        n_days = (total_hr+12) // 24

    if (total_hr // 12) % 2 == 0:
        new_m = m
    else:
        new_m = switch_m(m)

    day_num = find_day(days,day.capitalize())
    today = n_days 

    if final_hr == 0:
        final_hr = 12

    new_time = f'{final_hr}:{final_min:02} {new_m}'

    day_name = (day_num + today) 
    if day_name > 7:
        day_name = day_name % 7
        if day_name == 0:
            day_name = 7

    if day!='Noday':
        new_time += f', {days[str(day_name)]}'

    if today > 0:
        if today == 1:
            new_time += " (next day)"
        else:
            new_time += f' ({today} days later)'


    return new_time


print(add_time('2:59 AM', '24:00', 'saturDay'))