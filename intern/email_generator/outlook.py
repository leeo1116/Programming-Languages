__author__ = 'liangl2'
def send(subject, to, cc, body, bcc=None, *attachment):
    """
    Send email by outlook account
    :param subject: subject
    :param to: send to
    :param cc: copy to
    :param bcc: blind copy to
    :param body: body
    :param attachment: attachments paths
    """
    import win32com.client
    outlook_obj = win32com.client.Dispatch("Outlook.Application")
    mail = outlook_obj.CreateItem(0x0)
    mail.Subject = subject
    mail.Body = body
    mail.To = to
    mail.CC = cc
    mail.BCC = bcc
    for a in attachment:
        mail.Attachments.Add(a)
    mail.display()
    #mail.Send()

def smtp_send(user, password, send_from, send_to, subject, body):
    """
    :param user: leeo1116@gmail.com
    :param password: :)
    :param send_from: leeo1116@gmail.com
    :param send_to: must be a list
    :param subject:
    :param body:
    :return:
    """
    import smtplib
    #  Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (send_from, ", ".join(send_to), subject, body)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(user, password)
        server.sendmail(send_from, send_to, message)
        server.close()
        print("Send email successfully!")
    except:
        print("SMTP server setup error!")
        raise

