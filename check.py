#!/usr/bin/python

import requests
import smtplib
import socket

def checkWebsites():
    print "Checking websites"
    sites = ['http://psywerx.net', 'http://gitlab.psywerx.net', 'http://stejem.psywerx.net/',
             'http://vodim.si', 'http://slabefotke.com', 'http://slabescene.com/', 
             'http://siviljstvo-alenka.com', 'http://vezenje-kranj.com', 'http://maleficusangelus.com',
             'http://mavricnistumfki.net', 'http://scoreboards.psywerx.net']

    for s in sites:
        try:
            r = requests.get(s)
            if r.status_code != 200:
                print "  [%s] %s" % (red(r.status_code), s)
            else:
                print "  [%s] %s" % (green(r.status_code), s)
        except requests.exceptions.ConnectionError:
                print s, "connection error"

def checkServices():
    print "Checking services"
    
    services = [
        ('smotko ssh', 'zidar.me', 11022),
        ('mail', 'mail.psywerx.net', 25),
        ('minecraft ssh', 'zidar.me', 12022),
        ('minecraft', 'minecraft.psywerx.net', 25565),
        
    ]

    for name, address, port in services:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((address, port))
        if(result != 0):
            print "  [%s] %s (%s)" % (red("down"), name, port)
        else:
            print "  [%s] %s (%s)" % (green("up"), name, port)

def checkSendMail():
    print "Sending test email"
    try:
       smtpObj = smtplib.SMTP('mail.psywerx.net')
       smtpObj.sendmail("smotko@psywerx.net", "test@smotko.si", "Test")         
       print "  [%s] mail sent " % green("ok")
    except smtplib.SMTPException:
       print "  [%s] mail not sent" % red("fail")

def red(s):
    return '\033[91m%s\033[0m' % s    
def green(s):
    return '\033[92m%s\033[0m' % s
if __name__ == "__main__":
    checkWebsites()
    checkServices()
    checkSendMail()
