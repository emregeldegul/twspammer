#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mechanize import Browser
from urllib import urlencode
from re import findall
from time import ctime
from json import load
from ragent import ph
from os import system

bold = "\033[1m"
underline = "\033[4m"
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"
red = "\033[91m"
endcolor = "\033[0m"

twitterLogin = "https://mobile.twitter.com/login"
twitterLoginCheck = "https://mobile.twitter.com/settings"
twitterActionLink = "https://mobile.twitter.com/{}/actions"
twitterLogout = "https://mobile.twitter.com/logout"
totalSpam = 0

br = Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', "Mozilla/5.0 (Android; Linux armv7l; rv:9.0) Gecko/20111216 Firefox/9.0 Fennec/9.0")]

with open("accounts.json") as accounts:
    data = load(accounts)

def logo():
    system("clear")
    print bold+yellow+"--==[ Twitter Spammer"+endcolor
    print bold+green+"--==[ Yunus Emre Geldegül"+endcolor
    print bold+blue+"--==[ www.emregeldegul.net"+endcolor
    print bold+"--------------------------\n"+endcolor
    
def help():
    logo()
    print bold+red+"Twitter Spammer Kullanımı"+endcolor
    print bold+green+"Spam İşlemleri"+endcolor
    print bold+green+"~$"+endcolor+" spam [hedefKullaniciAdi]"
    print bold+green+"Proxy İşlemleri"+endcolor
    print bold+green+"~$"+endcolor+" update proxy"+endcolor
    print ""
    print bold+yellow+"Not:"+endcolor+" Proxy listesini güncellemeden spam işlemini başlatmayın."
    print "-"*50

def spam(target, first, second):
    global totalSpam
    for i in range(int(first), int(second)):
        br.set_proxies({"http://": ph("rp")})
        br.open(twitterLogin)
        br.select_form(nr=0)
        br["session[username_or_email]"] = data["accounts"][i]["name"]
        br["session[password]"] = data["accounts"][i]["password"]
        br.submit()
        loginText = br.open(twitterLoginCheck).read()
        if data["accounts"][i]["name"].encode("utf-8") in loginText:
            br.open(twitterActionLink.format(target))
            say = 0
            for form in br.forms():
                if "spam" in form.action:
                    break
                else:
                    say+=1
            br.select_form(nr=say)
            message = br.submit().read()
            if '<div class="message">' in message:
                print bold+green+"[+] {} Giriş Başarılı, Spam Başarılı: ".format(ctime())+data["accounts"][i]["name"].encode("utf-8")+endcolor
                totalSpam += 1
            else:
                print bold+green+"[+] {} Giriş Başarılı, Spam Başarısız: ".format(ctime())+data["accounts"][i]["name"].encode("utf-8")+endcolor
            br.open(twitterLogout)
            br.select_form(nr=0)
            br.submit()
            print bold+green+"[+] {} Çıkış Başarılı: ".format(ctime())+data["accounts"][i]["name"].encode("utf-8")+endcolor
        else:
            print bold+red+"[-] {} Giriş Başarısız: ".format(ctime())+data["accounts"][i]["name"].encode("utf-8")+endcolor
    print bold+yellow+"Spam İşlemi Bitti, Toplam Spam: "+str(totalSpam)

logo()
while True:
    command = raw_input(bold+green+"es@coderlab"+" "+blue+"~$ "+endcolor)
    if command == "q" or command == "quit":
        exit(1)
    elif command.startswith("help"):
        help()
    elif command.startswith("update"):
        if command[7:] == "proxy":
            if ph("update") == 1:
                print bold+yellow+"[+] Proxy Güncellendi"+endcolor
            else:
                print bold+red+"[-] Proxy Güncellenemedi"+endcolor
        else:
            print command[7:]+"[-] Parametresi Bulunamadı"+endcolor
    elif command.startswith("spam"):
        target = command[5:]
        between = raw_input(bold+yellow+"ID Aralık (ex: 0:8): "+endcolor).partition(":")
        first, nul, second = between
        spam(target, first, second)
