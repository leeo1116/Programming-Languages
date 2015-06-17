__author__ = 'liangl2'
import datetime
import holidays
from email_generator import outlook

subject = "Timesheet"
# to = "timesheet@infoyogi.com"
# cc = "msapozhn@cisco.com; rao@BBITechnologies.com"
to = "leeo1116@gmail.com"
cc = ""
# cc = "leeo1116@gmail.com"

manager_info = "Manager Name : Mike Sapozhnikov\nCan you please approve my timesheet for "
workdays = 7
weekend = set([5, 6])
date_format = "%m/%d/%Y"  # http://strftime.org/
today = datetime.date.today()
start_day = (today-datetime.timedelta(days=workdays)).strftime(date_format)  # 7 days ago
end_day = (today-datetime.timedelta(days=1)).strftime(date_format)  # until yesterday
duration_info = start_day+" -- "+end_day+":\n\n"
week_info = "Week: "+duration_info[:-1]
dash = '-'*46+'\n'
week_info_width = int(week_info.__len__())
start_day_info_width = int(start_day.__len__())

# Email body
with open('email_preview.txt', 'w+') as file:
    file.write(manager_info)
    file.write(duration_info)
    file.write(week_info)
    file.write(dash)
    total_hours = 0
    for day_num in range(1, workdays+1, 1):
        days = datetime.timedelta(days=day_num)
        previous_date = today-days
        hours = 8
        if previous_date.weekday() in weekend or previous_date in holidays.US():  # https://pypi.python.org/pypi/holidays
            hours = 0
        workday_info = previous_date.strftime(date_format)+\
                       "{0:{fill}{align}{width}}".format("-- "+str(hours)+" Hrs", fill=' ', align='>', \
                                                         width=len(dash)-5-start_day_info_width)+'\n'  # alternative: rjust()
        file.write(workday_info)
        total_hours += hours
    file.write(dash)
    file.write("Total"+"{0:{fill}{align}{width}}".format("--"+str(total_hours)+" Hrs", fill=' ', \
                                                         align='>', width=len(dash)-len("total"))+'\n')
    file.write(dash)
    file.seek(0)
    body = file.read()
    print(body)
outlook.send(subject, to, cc, body, bcc="")