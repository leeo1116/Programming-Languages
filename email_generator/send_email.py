import smtplib

gmail_user = "liangli@gmail.com"
gmail_pwd = "pwd"
FROM = 'liangli@gmail.com'
TO = ['leeo1116@gmail.com'] #must be a list
SUBJECT = "Testing sending using gmail"
TEXT = "Testing sending mail using gmail servers"

# Prepare actual message
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

#server = smtplib.SMTP(SERVER)
server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
server.sendmail(FROM, TO, message)
#server.quit()
server.close()
print('successfully sent the mail')

