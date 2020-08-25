#!/usr/bin/python
#Spammer-Pesan Banyak
#tools ini hanya percobaan.
#yang menggunakan di tanggung sendiri !!!


import os
import smtplib
import getpass
import sys

print ("\n")
print ("Welcome To")
print ( " _____  ____  _____      _____      ____  ____  ____  _      _      _____ ____  ")
print ( "/__ __\/  _ \/__ __\    /  __/     / ___\/  __\/  _ \/ \__/|/ \__/|/  __//  __\ ")
print ( "  / \  | / \|  / \_____ |  \ _____ |    \|  \/|| / \|| |\/||| |\/|||  \  |  \/| ")
print ( "  | |  | \_/|  | |\____\|  /_\____\\___ ||  __/| |-||| |  ||| |  |||  /_ |    / ")
print ( "  \_/  \____/  \_/      \____\     \____/\_/   \_/ \|\_/  \|\_/  \|\____\\_/\_\ ")
print ( "                                                                                ")
print ("https://gagaltotal.github.io/")
print ("\n")

server = raw_input ('[Pilih Server Gmail/Yahoo]: ')
username = raw_input('[Masukan Email Anda]: ')
passwd = getpass.getpass('[Masukan Password Anda]: ')


send = raw_input('\n[email korban]: ')
#subject = raw_input('Subject: ')
body = raw_input('[Pesan email]: ')
total = input('[jumlah angka yang di kirim]: ')

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print 'Applies only to gmail and yahoo.'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(username,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rE-mails sent: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Done !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] Nama pengguna atau kata sandi yang Anda masukkan salah.'
    sys.exit()
