import datetime as dt

NON_WORK_DATE = [
    dt.date(2015,1,1),
    dt.date(2015,1,2),
    dt.date(2015,1,5),
    dt.date(2015,1,6),
    dt.date(2015,1,7),
    dt.date(2015,1,8),
    dt.date(2015,1,9),
    dt.date(2015,2,23),
    dt.date(2015,3,9),
    dt.date(2015,5,1),
    dt.date(2015,5,4),
    dt.date(2015,5,11),
    dt.date(2015,6,12),
    dt.date(2015,11,4),
    dt.date(2016,1,1),
    dt.date(2016,1,4),
    dt.date(2016,1,5),
    dt.date(2016,1,6),
    dt.date(2016,1,7),
    dt.date(2016,1,8),
    dt.date(2016,2,22),
    dt.date(2016,2,23),
    dt.date(2016,3,7),
    dt.date(2016,3,8),
    dt.date(2016,5,2),
    dt.date(2016,5,3),
    dt.date(2016,5,9),
    dt.date(2016,6,13),
    dt.date(2016,11,4),
    dt.date(2017,1,2),
    dt.date(2017,1,3),
    dt.date(2017,1,4),
    dt.date(2017,1,5),
    dt.date(2017,1,6),
    dt.date(2017,2,23),
    dt.date(2017,2,24),
    dt.date(2017,3,8),
    dt.date(2017,5,1),
    dt.date(2017,5,8),
    dt.date(2017,5,9),
    dt.date(2017,6,12),
    dt.date(2017,11,6),
    dt.date(2018,1,1),
    dt.date(2018,1,2),
    dt.date(2018,1,3),
    dt.date(2018,1,4),
    dt.date(2018,1,5),
    dt.date(2018,1,8),
    dt.date(2018,2,23),
    dt.date(2018,3,8),
    dt.date(2018,3,9),
    dt.date(2018,5,1),
    dt.date(2018,5,2),
    dt.date(2018,5,9),
    dt.date(2018,6,11),
    dt.date(2018,6,12),
    dt.date(2018,11,5),
    dt.date(2019,1,1),
    dt.date(2019,1,2),
    dt.date(2019,1,3),
    dt.date(2019,1,4),
    dt.date(2019,1,7),
    dt.date(2019,1,8),
    dt.date(2019,3,8),
    dt.date(2019,5,1),
    dt.date(2019,5,2),
    dt.date(2019,5,3),
    dt.date(2019,5,9),
    dt.date(2019,5,10),
    dt.date(2019,6,12),
    dt.date(2019,11,4),
    dt.date(2020,1,1),
    dt.date(2020,1,2),
    dt.date(2020,1,3),
    dt.date(2020,1,6),
    dt.date(2020,1,7),
    dt.date(2020,1,8),
    dt.date(2020,2,24),
    dt.date(2020,3,9),
    dt.date(2020,5,1),
    dt.date(2020,5,4),
    dt.date(2020,5,5),
    dt.date(2020,5,11),
    dt.date(2020,6,12),
    dt.date(2020,11,4),
    dt.date(2021,1,1),
    dt.date(2021,1,4),
    dt.date(2021,1,5),
    dt.date(2021,1,6),
    dt.date(2021,1,7),
    dt.date(2021,1,8),
    dt.date(2021,2,22),
    dt.date(2021,2,23),
    dt.date(2021,3,8),
    dt.date(2021,5,3),
    dt.date(2021,5,10),
    dt.date(2021,6,14),
    dt.date(2021,11,4),
    dt.date(2021,11,5),
    dt.date(2021,12,31),
    dt.date(2022,1,3),
    dt.date(2022,1,4),
    dt.date(2022,1,5),
    dt.date(2022,1,6),
    dt.date(2022,1,7),
    dt.date(2022,2,23),
    dt.date(2022,3,7),
    dt.date(2022,3,8),
    dt.date(2022,5,2),
    dt.date(2022,5,3),
    dt.date(2022,5,9),
    dt.date(2022,5,10),
    dt.date(2022,6,13),
    dt.date(2022,11,4),
    dt.date(2022,12,31)
]

WORK_DATE  = [
    dt.date(2016,2,20),
    dt.date(2018,4,28),
    dt.date(2018,6,9),
    dt.date(2018,12,29),
    dt.date(2021,2,20),
    dt.date(2022,3,5)
]


def get_type_day(check_date):
    if isinstance(check_date, dt.date):
        if check_date.weekday() < 5:
            if check_date in NON_WORK_DATE:
                result = "выходной"
            else:
                result = "рабочий"
        else:
            if check_date in WORK_DATE:
                result = "рабочий"
            else:
                result = "выходной"  
        return result
    else:
        raise Exception("Неверное значение. Нужна дата.")
        
def next_work_date(check_date):
    if isinstance(check_date, dt.date):
        if get_type_day(check_date) == "рабочий":
            result = check_date
        else:
            i = 1
            while get_type_day(check_date + dt.timedelta(days = i)) != "рабочий":
                i += 1
            result = check_date + dt.timedelta(days = i)
        return result    
    else:
        raise Exception("Неверное значение. Нужна дата.")
        
def get_weekday_name(check_date):
    if isinstance(check_date, dt.date):
        days_name = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'восресенье']
        return days_name[check_date.weekday()]
    else:
        raise Exception("Неверное значение. Нужна дата.")
        
# test drive
test_date = dt.date(2021,9,6)
if next_work_date(test_date) == test_date:
    next_workdate = "сегодня"
else:
    next_workdate = next_work_date(test_date).strftime("%Y-%m-%d")

print(f"""
{test_date.strftime("%Y-%m-%d")}:
 - {get_type_day(test_date)} день
 - {get_weekday_name(test_date)}
 - ближайший рабочий день: {next_workdate}
""")
