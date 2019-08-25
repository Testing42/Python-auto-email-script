import smtplib

gmail_user = 'seikukenbankai95@gmail.com'
gmail_password = 'Idrinkmilk42!'

sent_from = 'Keybank'
to = ['email', 'email']
subject = 'Important credit card info'
body = 'Senorita ,\n\nYou have unusual activity on your account please contact us as soon as possible\n\nThank you.'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" %(sent_from, ", ".join(to), subject, body)


try:
    conn_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    conn_ssl.ehlo()
    conn_ssl.login(gmail_user, gmail_password)
    conn_ssl.sendmail(gmail_user, to, email_text)
    conn_ssl.close()

    print('Email sent!')
except:  
    print('Something went wrong...')
