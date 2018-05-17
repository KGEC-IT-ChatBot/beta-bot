import os
import csv

def login_func():
	curr_path = os.path.dirname(os.path.realpath(__file__))
	print("Running facial recognition...")
	os.system('echo -n > shellOut.txt')
	print(curr_path+"login")
	os.system("fswebcam -d /dev/video0 -r 640x480 --jpeg 85 -f 5 face_recognition/unknown/user.jpg")
	os.system('face_recognition /home/moumita/chatbot_final/beta-bot/face_recognition/known/ /home/moumita/chatbot_final/beta-bot/face_recognition/unknown/  > shellOut.txt')

	
	file=open("shellOut.txt","r")
	lines=file.readlines()
	file.close()
	names=[]
	possible_user=[]

	for line in lines:
		names.append(line[line.index(",")+1:line.index('\n')])
	#print (curr_path)
	with open(os.path.join(curr_path,"data/credential.csv")) as file:
		reader = csv.reader(file, delimiter= ',')
		for row in reader:
			if(row[0] in names):
				possible_user.append(row)
	if(len(possible_user)==0):
		print ("User not found")
		op=raw_input("Try again? Y/N")
		if(op=="Y" or op=="y"):
			return (-1,-1)
		else:
			exit()
	else:
		print ("Facial match found in database")
		u=raw_input("Enter username : ")
		p=raw_input("Enter password : ")
		confirmed_user=[]
		for user in possible_user:
			if(user[1]==u and user[2]==p):
				confirmed_user=user
				print ("Logged in")
				break
		if(len(confirmed_user)==0):
			print("User not found")
			op=raw_input("Try again? Y/N")
			if(op=="Y" or op=="y"):
				return (-1,-1)
			else:
				exit()
		else:
			return (confirmed_user[1],confirmed_user[3])

def main():
	return
