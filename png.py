#!/usr/bin/env python3
# png.py
# Phone Number Generator [phone numbers like in Russia]
import random as r
import sys, os
cut='''
=========================
'''
numbers='1234567890'
def cl():
    os.system('cls'if os.name=='nt'else'clear')
def main():
    t=1
    while True:
        cl()
        try:
            while True:
                usr_nmb=int(input(f'Enter the NUMBER of PhoneNumber(s) [1-9999]: '))
                print(cut)
                if usr_nmb==0 or usr_nmb>9999:
                    cl()
                    continue
                else:
                    pass
                for count in range(usr_nmb):
                    a=r.choice(numbers)
                    b=r.choice(numbers)
                    c=r.choice(numbers)
                    d=r.choice(numbers)
                    e=r.choice(numbers)
                    f=r.choice(numbers)
                    g=r.choice(numbers)
                    h=r.choice(numbers)
                    i=r.choice(numbers)
                    pn=f'[{t}] +7-9{a}{b}-{c}{d}{e}-{f}{g}-{h}{i}'
                    t+=1
                    print(pn)
                print(cut)
                usr_cnt=input(f'[A]gain / [Q]uit ? ').strip().lower()
                if usr_cnt=='a':
                    cl()
                    t=1
                    break
                else:
                    sys.exit()
        except KeyboardInterrupt:
            print(cut)
            print(f'\nPNG has been stopped... ')
            sys.exit()
        except ValueError:
            cl()
            continue
        except Exception as e:
            print(f'\n[ERROR] -> {e} ')
main()
