#   Date:        2022/02/14
#   Author:      Emma Gillespie
#   Description: Add known ssh hosts and connect to them
#   Resources:   https://realpython.com/python-command-line-arguments/#:~:text=argc%20is%20an%20integer%20representing,remaining%20elements%20of%20the%20array.

#!/usr/bin/python3

import sys

#Function for add
def addSSH(conName, username, password):
    #Write/append to sshconnections.txt file
    file_object = open('connections.txt', 'a')
    file_object.write(f'{conName}:{username}:{password}\n')
    file_object.close()
    print(f"Connection was added. You can now connect to it.")

#Function for connect
def connectSSH():
    pass

#Function for listing the ssh names
def listSSH():
    pass

#Function for removing saved ssh connections and saves/overwrites file
def removeSSH():
    pass

#Function for terminal user interface
def userInterface():
    print("Welcome to SSH Tools terminal user interface. Select an option from below:")
    # Loop giving choices to the user. q will quit the application
    # Option to add known ssh hosts (username, and password, and name ssh) saved to a file. Writes to the file and Password is encrypted or file is encrypted
    # Option to open terminal and ssh into machine (read file and connect based on choice. File lines saved to dict based on ssh-name)
    # Option to remove known ssh hosts (name ssh) saved to a file. Overwrites the file
    pass

if __name__ == "__main__":
    # Debug: print(f"Arguments count: {len(sys.argv)}")
    if len(sys.argv) <= 1:
        print("\nusage: \"python3 ssh_tool.py -help\"\n")
    else:
        #Running the program with -help will list all command and usages (usage: "python3 ssh_tool.py -help") -h or -help
        if sys.argv[1] == '-help':
            print("\n-add will add new ssh connection \n\t(usage: \"python3 ssh_tool.py -add name-connection username password\")")
            print("-rem will remove the ssh connection \n\t(usage: \"python3 ssh_tool.py -rem name-connection\")")
            print("-con will connect to the given ssh name \n\t(usage: \"python3 ssh_tool.py -con name-connection\")")
            print("-list will list all ssh name of ssh connections \n\t(usage: \"python3 ssh_tool.py -list\")")
            print("-usri will open terminal user interface \n\t(usage: \"python3 ssh_tool.py -usri\")\n")
        
        #Running the program with -add will add a new one (usage: "python3 ssh_tool.py -add name-ssh username password") -a or -add
        elif sys.argv[1] == "-add":
            if len(sys.argv) == 5:
                addSSH(sys.argv[2], sys.argv[3], sys.argv[4])
            else:
                print("\n(usage: \"python3 ssh_tool.py -add name-connection username password\")\n")
        #Running the program with -con will connect to ssh name (usage: "python3 ssh_tool.py -con name-ssh") -c or -con
        #Running the program with -list will list the ssh name of ssh connections (usage: "python3 ssh_tool.py -list") -l or -list
        #Running the program with -usri will open terminal user interface (usage: "python3 ssh_tool.py -usri") -ui or -usri
        #Running the program with -rem will remove the ssh connection (usage: "python3 ssh_tool.py -rem name-ssh") -r or -rem
        
        #Debugging
        #for arg in enumerate(sys.argv):
        #    print(f"Argument: {arg}")

#Add documentation for ssh_tools.py
#Obfuscate program code