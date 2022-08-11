#!/usr/bin/env python3
import subprocess, yaml, os, sys, requests, getopt
from datetime import datetime

nmp_time = 'T3'
verbose = False
tlgrm = True
tries = 1

def help():
    print ('Usage ckonline -T <TIME> -v <Verbose On> -h <HELP!> --notelegram <NO Telegram MSG> -t <Tries>',f"\n")
    print ("-T:\nT0 = Insane\nT1 = Agressive\nT2 = Gentle\nT3 = Default")
    sys.exit(0)

try:
    opts, args = getopt.getopt(sys.argv[1:], "t:T:hv", ["help", "notelegram"])
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)
output = None
verbose = False

for o, a in opts:
    if o == "-v":
        verbose = True
    elif o in ("-h", "--help"):
        help()
    elif o == "-T":
        nmp_time = a
    elif o == "-t":
        tries = int(a)
    elif o == "--notelegram":
        tlgrm = False

dfile = os.path.dirname(os.path.realpath(__file__))
escfile = f"{dfile}/esc_file.yml"
botfile = f"{dfile}/bot_file.yml"

with open(escfile, 'r') as f: esc = yaml.safe_load(f)
with open(botfile, 'r') as f: bot = yaml.safe_load(f)


def sndtgrm(msg: str):
       agora = datetime.now()
       hoje = agora.strftime("%d/%m/%Y - %H:%M:%S")
       if tlgrm: requests.get(
           f"https://api.telegram.org/bot{bot['botok']}/sendMessage?chat_id={bot['chatid']}&text={msg} @ {hoje}")
       print(f"{msg} @ {hoje}")


if __name__ == '__main__':

       for i in range(len(esc)):
              portck = subprocess.getoutput(f"nmap -{nmp_time} -Pn -p {esc[i][2]} {esc[i][1]}|egrep -o -i 'open'")
              if portck == 'open':
                     if verbose: sndtgrm(f"{esc[i][0]} - OnLine")
                     if esc[i][3] == -1:
                            esc[i][3] = 0
                            with open(escfile, 'w') as f: yaml.dump(esc, f)
                            if not verbose: sndtgrm(f"{esc[i][0]} - OnLine")
              else:
                    if verbose: sndtgrm(f"{esc[i][0]} - OffLine")
                    if esc[i][3] >= 0:
                        if (esc[i][3] + 1) >= tries:
                            esc[i][3] = -1
                            if not verbose: sndtgrm(f"{esc[i][0]} - OffLine")
                        else:
                            if not esc[i][3] == -1:
                                esc[i][3] += 1
                    with open(escfile, 'w') as f: yaml.dump(esc, f)
