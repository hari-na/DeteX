import smtplib, ssl

ssl_context = ssl.create_default_context()
service = smtplib.SMTP_SSL("smtp.gmail.com",  465, context = ssl_context)
service.login('~~~~~', '~~~~~')
result = service.sendmail('SendersEmailAddress', 'RecepientsEmailAddress', f"Subject: ALERT!\nYour system is near failure. Rectify ASAP.")
service.quit()