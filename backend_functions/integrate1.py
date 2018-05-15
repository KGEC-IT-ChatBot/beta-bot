import csv
import os
import nltk
import re
curr_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'../data/')


header_ary = ["loan_id", "account_id", "date", "amount", "duration", "payments", "status",";", "disp_id", "client_id", "type",";", "account_id", "district_id", "frequency", "date",";", "client_id" , "birth_number"]


def printOut(account_id):
	disp_id=""
	dist=""
	output_ary = []
	with open(os.path.join(curr_path,"loan.csv"),'r') as f:
	    reader = csv.reader(f, delimiter= ';')
	    zerovar = 0
	    
	    for row in reader:
		if zerovar==0:
		    zerovar = zerovar + 1
		else:
		    sn1 = row [0]
		    sn2 = row [1]
		    sn3 = row [2]
		    sn4 = row [3]
		    sn5 = row [4]
		    sn6 = row [5]
		    sn7 = row [6]
		    zerovar = zerovar + 1
		    y = str(sn2)
		    if y == account_id:
		        output_ary.append(row)
		        loan_id = str(sn1)
		        y = str(sn2)
		        date = str(sn3)
		        amount = str(sn4)
		        duration = str(sn5)
		        payments = str(sn6)
		        status = str(sn7)
		        


	output_ary1=[]
	'''with open(os.path.join(curr_path,"disp.csv"),'r') as f:
	    reader1 = csv.reader(f, delimiter= ';')
	    zerovar1 = 0

	    for row in reader1:
		if zerovar1==0:
		    zerovar1 = zerovar1 + 1
		else:
		    sn11 = row [0]
		    sn22 = row [2]
		    sn33 = row [1]
		    sn44 = row [3]
		    zerovar1 = zerovar1 + 1
		    y = str(sn22)
		    if y == account_id:
		        output_ary1.append(row[0])
		        output_ary1.append(row[1])
		        output_ary1.append(row[3])
		        output_ary.append(output_ary1)
		        disp_id = str(sn11)
		        y = str(sn22)
		        client_id = str(sn33)
		        type_id = str(sn44)
		        break'''

	output_ary2=[]
	with open(os.path.join(curr_path,"account.csv"),'r') as f:
	    reader1 = csv.reader(f, delimiter= ';')
	    zerovar1 = 0
	    for row in reader1:
		if zerovar1==0:
		    zerovar1 = zerovar1 + 1
		else:
		    sn11 = row [0]
		    sn22 = row [2]
		    sn33 = row [1]
		    sn44 = row [3]
		    zerovar1 = zerovar1 + 1
		    x = str(sn11)
		    if x == account_id:
		        output_ary2.append(row[1])
		        output_ary2.append(row[2])
		        output_ary2.append(row[3])
		        output_ary.append(output_ary2)
		        dist =  str(row[1])
		        zerovar1 = zerovar1 + 1
		        x = str(sn11)
		        frequency = str(sn22)
		        dist_id = str(sn33)
		        date = str(sn44)
		        break

	output_ary3=[]
	with open(os.path.join(curr_path,"order.csv"),'r') as f:
	    reader1 = csv.reader(f, delimiter= ';')
	    zerovar1 = 0
	    for row in reader1:

		if zerovar1==0:
		    zerovar1 = zerovar1 + 1
		else:
		    sn11 = row [0]
		    sn22 = row [1]
		    sn33 = row [2]
		    sn44 = row [3]
		    sn55 = row [4]
		    sn66 = row [5]
		    zerovar1 = zerovar1 + 1
		    y = str(sn22)
		    if y == account_id:
		        output_ary3.append(row[0])
		        output_ary3.append(row[2])
		        output_ary3.append(row[3])
		        output_ary3.append(row[4])
		        output_ary3.append(row[5])
		        output_ary.append(output_ary3)
		        order_id = str(sn11)
		        y = str(sn22)
		        bank_to = str(sn33)
		        account_to = str(sn44)
		        amount = str(sn55)
		        k_symbol = str(sn66)
		        
	output_ary4=[]
	with open(os.path.join(curr_path,"client.csv"),'r') as f:
	    reader1 = csv.reader(f, delimiter= ';')
	    zerovar1 = 0
	    for row in reader1:
		if zerovar1==0:
		    zerovar1 = zerovar1 + 1
		else:
		    sn11 = row [0]
		    sn22 = row [2]
		    sn33 = row [1]
		    zerovar1 = zerovar1 + 1
		    x = str(sn11)
		    y = str(sn22)
		    if y == dist and x == client_id :
		        output_ary4.append(row[0])
		        output_ary4.append(row[1])
		        output_ary.append(output_ary4)

		        birth_no = str(sn33)

	output_ary5=[]
	with open(os.path.join(curr_path,"card.csv"),'r') as f:
	    reader1 = csv.reader(f, delimiter= ';')
	    zerovar1 = 0
	    for row in reader1:
		if zerovar1==0:
		    zerovar1 = zerovar1 + 1
		else:
		    sn11 = row [0]
		    sn22 = row [1]
		    sn33 = row [2]
		    sn44 = row [3]
		    zerovar1 = zerovar1 + 1
		    y = str(row[1])
		    if y == disp_id :
		        output_ary5.append(row[0])
		        output_ary5.append(row[2])
		        output_ary5.append(row[3])
		        output_ary.append(output_ary5)
		        card_id = str(sn11)
		        y = str(row[1])
		        type_id = str(sn33)
		        issued = str(sn44)

	print("file writing is successful")
	with open("Sampleoutput.txt",'w') as f2:
	    for row in header_ary:
		f2.write(row+" ")
	    f2.write("\n")   
	    for row in output_ary:
		for item in row:
		    f2.write(item + ",")
		f2.write(";")
		

	test1=input("enter your query")
	print(test1)
	tokens1=nltk.word_tokenize(test1)
	print(tokens1)
	len1=len(tokens1)
	print(len1)
	for name in tokens1:
	    if name == "loan_id":
		print(l_id)
	    if name == "date":
		print(date)
	    if name == "amount":
		print(amount)
	    if name == "duration":
		print(duration)
	    if name == "payments":
		print(payments)
	    if name == "status":
		print(status)
	    if name == "dist_id":
		print(dist_id)
	    if name == "frequency":
		print(frequency)
	    if name == "card_id":
		print(card_id)
	    if name == "disp_id":
		print(y)
	    if name == "type":
		print(type_id)
	    if name == "issued":
		print(issued)
	    if name == "client_id":
		print(client_id)
	    if name == "birth_number":
		print(birth_no)
	    if name == "order_id":
		print(order_id)
	    if name == "bank_to":
		print(bank_to)
	    if name == "account_to":
		print(account_to)
	    if name == "k_symbol":
		print(k_symbol)
	    if name == "statu":
		print(status) 


    
        
