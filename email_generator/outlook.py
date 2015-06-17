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