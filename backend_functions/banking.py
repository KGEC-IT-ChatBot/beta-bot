import csv
import sys
import datetime
names=list()
usernames=list()
passwords=list()
acc_ids=list()
balances=list()
def readcsv():
    with open('data/credentials.csv','rb') as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        for row in reader:
            names.append(row[0])
            usernames.append(row[1])
            passwords.append(row[2])
            acc_ids.append(row[3])
            balances.append(row[4])
def writecsv():
    with open('data/credentials.csv','wb') as csvfile:
        writer=csv.writer(csvfile,delimiter=',')
        writer.writerow(['names']+['username']+['password']+['account_id']+['balance'])
        for i in range(len(names)):
            writer.writerow([name[i]]+[usernames[i]]+[passwords[i]]+[acc_ids[i]]+[balances[i]])
def transaction(from_id,to_id,amount):
    for i in range(len(acc_ids)):
        if acc_ids[i]==from_id:
            balances[i]=str(int(balances[i])-int(amount))
        if acc_ids[i]==to_id:
            balances[i]=str(int(balances[i])+int(amount))
def record(acc_id_from,acc_id_to,amount):
    s=str(datetime.datetime.now())
    fp=s.split(" ")[0].split("-")
    sp = s.split(" ")[1].split(":")
    lp1,lp2=sp[2].split(".")
    id=fp[0]+fp[1]+fp[2]+sp[0]+sp[1]+lp1+lp2
    with open('data/transactions.csv','ab') as csvfile:
        writer=csv.writer(csvfile,delimiter=',')
        writer.writerow([id]+[acc_id_from]+[acc_id_to]+[amount]+[datetime.datetime.now()])
def if __name__ == '__main__':
    args=sys.argv[1:]
    if(args[0]=='transaction'):
        readcsv()
        transaction(argv[1],argv[2],argv[3])
        record(argv[1],argv[2],argv[3])
        writecsv()


