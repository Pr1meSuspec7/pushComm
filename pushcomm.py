import napalm
import time
from os import system, name 
from termcolor import colored
from tabulate import *
from getpass import getpass
from simple_term_menu import TerminalMenu


ipDevices_commandsToRun = {'DEVICES': [],
							'COMMANDS': []}


# Default parameters
userDevice = ''
pwdDevice = ''
portDevice = 22



# Function for run commands on devices with each output
def connectDeviceSSH():
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
	devices_input = input('Insert one or more ip addresses separated by comma: ')
	devices_input_list = devices_input.replace(" "," ").split(",")
	devices_input_list_clean = []
	for string in devices_input_list:
		string = check_if_ipv4(string.strip())
		if string and string not in ipDevices_commandsToRun['DEVICES']:
			ipDevices_commandsToRun['DEVICES'].append(string)

def delDevice():
	print(ipDevices_commandsToRun['DEVICES'])
	devices_input = input('Insert one or more ip addresses separated by comma: ')
	devices_input_list = devices_input.replace(" "," ").split(",")
	devices_input_list_clean = []
	for string in devices_input_list:
		string = check_if_ipv4(string.strip())
		if string and string in ipDevices_commandsToRun['DEVICES']:
			ipDevices_commandsToRun['DEVICES'].remove(string)

# Function for add commands
def addCommand():
	command_input = input('Insert an IOS command separated by comma: ')
	command_input_list = command_input.replace(" "," ").split(",")
	command_input_strip = []
	for i in command_input_list:
		command_input_strip.append(i.strip())
	command_input_list_clean = []
	for string in command_input_strip:
		if string:
			command_input_list_clean.append(string)
	for command in command_input_list_clean:
		if command not in ipDevices_commandsToRun['COMMANDS']:
			ipDevices_commandsToRun['COMMANDS'].append(command)

def delCommand():
	command_input = input('Insert an IOS command separated by comma: ')
	command_input_list = command_input.replace(" "," ").split(",")
	command_input_strip = []
	for i in command_input_list:
		command_input_strip.append(i.strip())
	command_input_list_clean = []
	for string in command_input_strip:
		if string:
			command_input_list_clean.append(string)
	for command in command_input_list_clean:
		if command in ipDevices_commandsToRun['COMMANDS']:
			ipDevices_commandsToRun['COMMANDS'].remove(command)

# Function for change default port protocol
def modifyPortDevice():
	global portDevice
	port = int(input('Insert port protocol: '))
	if port < 0 or port > 65535:
		print('Port must be a number beetween 0 and 65535')
		modifyPortDevice()
		#return None
	else:
		portDevice = port
		print(colored('Port protocol modified!', 'yellow'))

# Function for change username to connect devices
def modifyUsername():
	username = input('Insert username: ')
		#return None
	global userDevice
	userDevice = str(username)
	print(colored('Username modified!', 'yellow'))

# Function for change password to connect devices
def modifyPassword():
	password = getpass()
		#return None
	global pwdDevice
	pwdDevice = str(password)
	print(colored('Password modified!', 'yellow'))

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
		#print('ERROR: Must be an ipv4 address')
		return
	while len(quadinteger) != 4:
		#print('ERROR: Must be four octects')
		return
	for octect in quadinteger:
		if octect > 255 or octect < 0:
			#print('ERROR: Each octects must be beetween 0 and 255')
			return
	return ip




def menu():
	# MAIN MENU
	main_menu_title = " ===== Main Menu =====\n"
	main_menu_items = ["Edit parameters", "Edit devices list", "Edit commands list", "Save output in a file (WIP)", "Push commands on devices", "Quit"]
	main_menu_cursor = "> "
	main_menu_cursor_style = ("fg_cyan", "bold")
	main_menu_style = ("bg_red", "fg_yellow")
	main_menu_exit = False
	main_menu = TerminalMenu(menu_entries=main_menu_items,
							 title=main_menu_title,
							 menu_cursor=main_menu_cursor,
							 menu_cursor_style=main_menu_cursor_style,
							 #menu_highlight_style=main_menu_style,
							 cycle_cursor=True)
	# EDIT PARAM MENU
	edit_param_menu_title = " ===== Edit Parameters =====\n"
	edit_param_menu_items = ["Set username", "Set password", "Set telnet/SSH (WIP)", "Set port protocol", "Back to Main Menu"]
	edit_param_menu_back = False
	edit_param_menu = TerminalMenu(edit_param_menu_items,
							 edit_param_menu_title,
							 main_menu_cursor,
							 main_menu_cursor_style)
							 #main_menu_style)
	# EDIT DEVICES MENU
	edit_dev_menu_title = " ===== Edit Devices =====\n"
	edit_dev_menu_items = ["Add device", "Del device", "Back to Main Menu"]
	edit_dev_menu_back = False
	edit_dev_menu = TerminalMenu(edit_dev_menu_items,
							 edit_dev_menu_title,
							 main_menu_cursor,
							 main_menu_cursor_style)
							 #main_menu_style)
	# EDIT COMMANDS MENU
	edit_com_menu_title = " ===== Edit Commands =====\n"
	edit_com_menu_items = ["Add command", "Del command", "Back to Main Menu"]
	edit_com_menu_back = False
	edit_com_menu = TerminalMenu(edit_com_menu_items,
							 edit_com_menu_title,
							 main_menu_cursor,
							 main_menu_cursor_style)
							 #main_menu_style)
	while not main_menu_exit:
		system('clear')
		print('')
		print(tabulate(ipDevices_commandsToRun, headers='keys', tablefmt="rst"))
		print('Username: ' + colored(userDevice, 'cyan'))
		print('Password: ' + colored('*' * len(pwdDevice), 'cyan'))
		print('Protocol: ' + colored('SSH', 'cyan'))
		print('Port: ' + colored(str(portDevice), 'cyan'))
		print('')
		print('')
		main_sel = main_menu.show()
		if main_sel == 0:
			while not edit_param_menu_back:
				system('clear')
				print('')
				print(tabulate(ipDevices_commandsToRun, headers='keys', tablefmt="rst"))
				print('Username: ' + colored(userDevice, 'cyan'))
				print('Password: ' + colored('*' * len(pwdDevice), 'cyan'))
				print('Protocol: ' + colored('SSH', 'cyan'))
				print('Port: ' + colored(str(portDevice), 'cyan'))
				print('')
				print('')
				edit_sel = edit_param_menu.show()
				if edit_sel == 0:
					print("Set username")
					modifyUsername()
					time.sleep(2)
				elif edit_sel == 1:
					print("Set password")
					modifyPassword()
					time.sleep(2)
				elif edit_sel == 2:
					print("Set telnet/SS")
					time.sleep(2)
				elif edit_sel == 3:
					print("Set port protocol")
					modifyPortDevice()
					time.sleep(2)
				elif edit_sel == 4:
					edit_param_menu_back = True
					print("Back Selected")
			edit_param_menu_back = False
		elif main_sel == 1:
			while not edit_dev_menu_back:
				system('clear')
				print('')
				print(tabulate(ipDevices_commandsToRun, headers='keys', tablefmt="rst"))
				print('Username: ' + colored(userDevice, 'cyan'))
				print('Password: ' + colored('*' * len(pwdDevice), 'cyan'))
				print('Protocol: ' + colored('SSH', 'cyan'))
				print('Port: ' + colored(str(portDevice), 'cyan'))
				print('')
				print('')
				edit_sel = edit_dev_menu.show()
				if edit_sel == 0:
					print("Add device")
					addDevice()
					time.sleep(2)
				elif edit_sel == 1:
					print("Del device")
					delDevice()
					time.sleep(2)
				elif edit_sel == 2:
					edit_dev_menu_back = True
					print("Back Selected")
			edit_dev_menu_back = False
		elif main_sel == 2:
			while not edit_com_menu_back:
				system('clear')
				print('')
				print(tabulate(ipDevices_commandsToRun, headers='keys', tablefmt="rst"))
				print('Username: ' + colored(userDevice, 'cyan'))
				print('Password: ' + colored('*' * len(pwdDevice), 'cyan'))
				print('Protocol: ' + colored('SSH', 'cyan'))
				print('Port: ' + colored(str(portDevice), 'cyan'))
				print('')
				print('')
				edit_sel = edit_com_menu.show()
				if edit_sel == 0:
					print("Add command")
					addCommand()
					time.sleep(2)
				elif edit_sel == 1:
					print("Del command")
					delCommand()
					time.sleep(2)
				elif edit_sel == 2:
					edit_com_menu_back = True
					print("Back Selected")
			edit_com_menu_back = False
		elif main_sel == 3:
			print("Save output in a file")
			time.sleep(2)
		elif main_sel == 4:
			print("Push commands on devices")
			connectDeviceSSH()
			time.sleep(2)
		elif main_sel == 5:
			main_menu_exit = True
			print("Quit Selected")

if __name__ == "__main__":
	menu()
