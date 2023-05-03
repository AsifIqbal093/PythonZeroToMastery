import smtplib


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:  
            email_address = 'im.asif093@gmail.com'
            email_password = 'exudbtzredlvjwlr'
            connection.login(email_address, email_password )
            connection.sendmail(
                from_addr=email_address, to_addrs='im.asif093@gmail.com', 
                msg='Hello Boy'
            )