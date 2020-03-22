
import napalm
import time
from os import system, name 
from termcolor import colored
from tabulate import *
from getpass import getpass


ipDevices_commandsToRun = {'DEVICES': [],
							'COMMANDS': []}


# Default parameters
userDevice = ''
pwdDevice = ''
portDevice = 22


# Function for run commands on devices with each output
def connectDevice():
	Driver = napalm.get_network_driver('ios')
	for ip in ipDevices_commandsToRun['DEVICES']:
		Parameters = Driver(hostname=ip,username=userDevice,password=pwdDevice,optional_args={"port": portDevice})
		print('')
		print(colored('CONNECTING TO [' + ip + '] ********************************************************', 'yellow'))
		try:
			Parameters.open()
		except napalm.base.exceptions.ConnectionException:
			print(colored('\nERROR: Cannot connect to ' + ip, 'red'))

		resultCommand = '' # Need to define before next try block otherwise doesn't work in the for loop
		try:
			resultCommand = Parameters.cli(ipDevices_commandsToRun['COMMANDS'])
		except AttributeError:
			pass
		for k in resultCommand:
		    print(colored('\n' + '[ ' + ip + ' - ' + str.upper(k) + ' ]', 'green'))
		    print(resultCommand[k])
		print('\n')
	quit()

# Function for add devices
def addDevice():
	device = input('Insert an ip address: ')
	if device not in ipDevices_commandsToRun['DEVICES']:
		ipDevices_commandsToRun['DEVICES'].append(device)
	else:
		print('Device already exist!')

# Function for add commands
def addCommand():
	command = input('Insert an IOS command: ')
	if command not in ipDevices_commandsToRun['COMMANDS']:
		ipDevices_commandsToRun['COMMANDS'].append(command)
	print('\nDevices loaded:')
	for i in ipDevices_commandsToRun['COMMANDS']:
		print(i)

# Function for change default port protocol
def modifyPortDevice():
	port = int(input('Insert port protocol: '))
	if port < 0 or port > 65535:
		print('Port must be a number beetween 0 and 65535')
		modifyPortDevice()
		#return None
	global portDevice
	portDevice = int(port)
	print(colored('Port protocol modified!\n', 'yellow'))

# Function for change username to connect devices
def modifyUsername():
	username = input('Insert username: ')
		#return None
	global userDevice
	userDevice = str(username)
	print(colored('Username modified!\n', 'yellow'))

# Function for change password to connect devices
def modifyPassword():
	password = getpass()
		#return None
	global pwdDevice
	pwdDevice = str(password)
	print(colored('Password modified!\n', 'yellow'))

# Function for clear terminal
def clearPrompt():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

# Function for check if input is an ipv4 address
def check_if_ipv4(ip):
	quad = ip.split(".")
	quadinteger = []
	try:
		quadinteger = [int(num) for num in quad]
	except ValueError:
		print('ERROR: Must be an ipv4 address')
		return None
	while len(quadinteger) != 4:
		print('ERROR: Must be four octects')
		break
	for octect in quadinteger:
		if octect > 255 or octect < 0:
			print('ERROR: Each octects must be beetween 0 and 255')
			break

# Function for interactive menu
def menu():
	print('')
	print(tabulate(ipDevices_commandsToRun, headers='keys', tablefmt="rst"))
	print('')
	print('')
	print('**************** MAIN MENU ******************')
	choice = input('''
        1: Change username
        2: Change password
        3: Change SSH port (default port 22)
        4: Add device to connect
        5: Add command to run
        6: Save output in a file (Work in progress...)
        7: Push commands on devices
        Q: Quit

       Please enter your choice: ''')
	if choice == '1':
		clearPrompt()
		print('\n You have select: 1 --> Change username\n')
		modifyUsername()
		menu()
	elif choice == '2':
		clearPrompt()
		print('\n You have select: 2 --> Change password\n')
		modifyPassword()
		menu()
	elif choice == '3':
		clearPrompt()
		print('\n You have select: 3 --> Change SSH port (default port 22)\n')
		modifyPortDevice()
		menu()
	elif choice == '4':
		clearPrompt()
		print('\n You have select: 4 --> Add device to connect\n')
		addDevice()
		menu()
	elif choice == '5':
		clearPrompt()
		print('\n You have select: 5 --> Add command to run\n')
		addCommand()
		menu()
	elif choice == '6':
		clearPrompt()
		print('\n You have select: 6 --> Save output in a file (Work in progress...)\n')
		# INSERT FUNCTION HERE
		menu()
	elif choice == '7':
		clearPrompt()
		print('\n You have select: 7 --> Push commands on devices\n')
		connectDevice()
		menu()
	elif choice == 'Q' or choice == 'q':
		#return None
		quit()
	else:
		print(colored('\nYou must only select one option.', 'yellow'))
		print(colored('Please try again\n', 'yellow'))
		time.sleep(3)
		clearPrompt()
		menu()

# Main function calls menu()
def main():
	clearPrompt()
	menu()

if __name__ == '__main__':
	main()