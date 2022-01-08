#! python3

import shelve,sys,pyperclip

shelfFile=shelve.open('passwordkeeper')

try:
    PASSWORDS=shelfFile['passwords']
except KeyError:
    shelfFile["passwords"]={}

if len(sys.argv)<2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    newaccount=input('would you like to make a new account?')
    if newaccount == 'y' or newaccount =='yes':
        while True:
            newpassword=input('what is the password with this new account?')
            correct=input('you inputed %s, is this correct?'%(newpassword))
            if correct== 'y' or 'yes':
                break
        PASSWORDS[account]=newpassword
    else:
        pass
shelfFile['passwords']=PASSWORDS
shelfFile.close()