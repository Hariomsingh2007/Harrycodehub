#this code only works if we turn on the below link
#https://www.google.com/settings/security/lesssecureapps

import smtplib
fromadd='hariomsingh@gmail.com'
toadd='xyz@gmail.com'
msg='Hello Friend'
for i in range(1,100):
  mail = smtplib.SMTP('smtp.gmail.com', 587)
  mail.ehlo()
  mail.starttls()
  mail.login('hariomsingh@gmail.com', 'password')
  mail.sendmail(fromadd, toadd, msg)
  mail.quit()
