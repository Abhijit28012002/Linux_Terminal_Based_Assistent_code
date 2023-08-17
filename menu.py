import os

os.system("tput setaf 4")
print("\t\t\t\t Welcome Come To my Command Line Code")
os.system("tput setaf 3")
print("\t\t\t\t -------------------------------------")

print("\n\n")


#Some Command I can run using command line
print(
"""
Press 1: To see the Date
Press 2: To Check Calender
Press 3: Set Up Account
Press 4: To Create a file
Press 5: To Open Firefox
"""
)

print("\n")

while True:
	choice=input("Enter Your choice: ")
	if choice=='1':
		os.system("tput setaf 2")
		print("The Current Date Is ")
		os.system("date")
		os.system("tput setaf 3")
	elif choice=='2':
		os.system("tput setaf 2")
		print("This Month Calender Is ")
		os.system("cal")
		os.system("tput setaf 3")
	elif choice=='5':
		os.system("tput setaf 2")
		print("Firefox Browser are going to Open ")
		os.system("firefox")
		os.system("tput setaf 3")
	elif choice=='4':
		os.system("tput setaf 2")
		file=input("Enter Your File name(With Extention): ")
		os.system(f'touch { file }')
		print(f'{file} created successfully')
		os.system("tput setaf 3")
	elif choice=='3':
		os.system("tput setaf 2")
		user=input("Enter Your user name: ")
		os.system(f'useradd {user}')
		print(f'User {user} Created successfully')
		os.system("tput setaf 3")
	else:
		break


print("\t\t\tGood Bye.....")
	


