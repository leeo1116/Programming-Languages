__author__ = 'liangl2'
import datetime
# SMTP server initialization

# Email header: send to, cc, bcc, subject
send_to = "timesheet@infoyogi.com"
cc = ["msapozhn@cisco.com", "rao@BBITechnologies.com"]
manager_info = "Manager Name : Mike Sapozhnikov\nCan you please approve my timesheet for "

workdays = 7
date_format = "%m/%d/%Y"
today = datetime.date.today()
start_day = (today-datetime.timedelta(days=workdays)).strftime(date_format)  # 7 days ago
end_day = (today-datetime.timedelta(days=1)).strftime(date_format)  # until yesterday
duration_info = start_day+" -- "+end_day+":\n\n"
week_info = "Week: "+duration_info[:-1] +'-'*31+'\n'
week_info_width = int(week_info.__len__()/2)
start_day_info_width = int(start_day.__len__())


# Email body
with open('email_preview.txt', 'w+') as file:
    file.write(manager_info)
    file.write(duration_info)
    file.write(week_info)
    for day_num in range(1, workdays+1, 1):
        days = datetime.timedelta(days=day_num)
        previous_date = today-days
        if previous_date is
        workday_info = previous_date.strftime(date_format)+\
                       "{0:{fill}{align}{width}}".format(str("-- ", hours, " Hrs"), fill=' ', align='>', \
                                                         width=week_info_width-start_day_info_width)+'\n'
        file.write(workday_info)
    file.seek(0)
    read_data = file.read()
    print(read_data)

# Fixed text
# Dynamic date



str("--", 12, 'asd')

# Send