import csv
import sys
import datetime
import speech
names=list()
usernames=list()
passwords=list()
acc_ids=list()
balances=list()
def readcsv():
    with open('data/credential.csv','rb') as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        for row in reader:
            names.append(row[0])
            usernames.append(row[1])
            passwords.append(row[2])
            acc_ids.append(row[3])
            balances.append(row[4])
def writecsv():
    with open('data/credential.csv','wb') as csvfile:
        writer=csv.writer(csvfile,delimiter=',')
        writer.writerow(['names']+['username']+['password']+['account_id']+['balance'])
        for i in range(1,len(names)):
            writer.writerow([names[i]]+[usernames[i]]+[passwords[i]]+[acc_ids[i]]+[balances[i]])
def transaction(from_id,to_id,amount):
    if from_id=="" or to_id=="":
        speech.say("Check Username")
        print("Agent : Check username")
        return -1
    for i in range(1,len(acc_ids)):
        if acc_ids[i]==from_id:
            if int(balances[i]) >= int(amount):
                balances[i]=str(int(balances[i])-int(amount))
            else:
                speech.say("Amount not sufficient")
                print("Agent : Amount not sufficient")
                return -1
        if acc_ids[i]==to_id:
            balances[i]=str(int(balances[i])+int(amount))
    return 0
def record(acc_id_from,acc_id_to,amount):
    s=str(datetime.datetime.now())
    fp=s.split(" ")[0].split("-")
    sp = s.split(" ")[1].split(":")
    lp1,lp2=sp[2].split(".")
    id=fp[0]+fp[1]+fp[2]+sp[0]+sp[1]+lp1+lp2
    with open('data/transaction.csv','ab') as csvfile:
        writer=csv.writer(csvfile,delimiter=',')
        writer.writerow([id]+[acc_id_from]+[acc_id_to]+[amount]+[datetime.datetime.now()])
    print("Transaction Complete!!")
def balance(acc_id):
    for i in range(len(acc_ids)):
        if acc_ids[i]==acc_id:
            return balances[i]

args=sys.argv[1:]
if(args[0]=='transaction'):
    readcsv()
    to_id=''
    print (args[2])
    for i in range(1,len(acc_ids)):
        if (args[2].upper()) in (names[i].upper()) and args[2].upper()!="" :
            to_id=acc_ids[i]
            break
    if (to_id==""):
        speech.say("User not found. Enter Account ID")
        to_id=raw_input("Agent : User not found. Enter Account ID")
    x=transaction(args[1],to_id,args[3])
    if(x==-1):
        exit()
    record(args[1],to_id,args[3])
    writecsv()
    speech.say(args[3]+" has been deducted from your account. Your balance is "+balance(args[1]))
    print("Agent : "+args[3]+" has been deducted from your account. Your balance is "+balance(args[1]))
elif(args[0]=='balance'):
    id=args[1]
    readcsv()
    speech.say ("Your balance is "+balance(args[1]))
    print("Agent : Your balance is "+balance(args[1]))


