
def cal_weeks(date1, date2):
    timedelta1 = date2 - date1
    return (timedelta1.days // 7, timedelta1.days % 7)