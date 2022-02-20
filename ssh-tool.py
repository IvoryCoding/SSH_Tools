#   Date:        2022/02/14
#   Author:      Emma Gillespie
#   Description: Add known ssh hosts and connect to them. Terminal command file to make ssh easier
#   Resources:   https://realpython.com/python-command-line-arguments/#:~:text=argc%20is%20an%20integer%20representing,remaining%20elements%20of%20the%20array.
#                https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/

#!/usr/bin/python3

import sys
import os
import platform

#Function for add
def addSSH(conName, username, password, ip):
    #Write/append to sshconnections.txt file
    file_object = open('connections.txt', 'a')
    file_object.write(f'{conName}:{username}:{password}:{ip}\n')
    file_object.close()
    print("\nConnection was added. You can now connect to it. Using the -con argument\n")

#Function for connect
def connectSSH(conName):
    connections = readConnections()

    if (platform.system() == 'Linux'):
        commandString = f'sshpass -p {connections[conName][1]} ssh {connections[conName][0]}@{connections[conName][2]}' #Need sshpass do sudo apt install sshpass
        os.system(commandString)
    else:
        commandString = f'putty.exe -ssh {connections[conName][0]}@{connections[conName][2]} -pw {connections[conName][1]}'
        os.system(commandString)

#Function for listing the ssh names
def listSSH():
    connections = readConnections()

    for key in connections:
        print(f'{key}:{connections[key][0]}:{connections[key][1]}:{connections[key][2]}\n')

#Function for reading the connection file. Returns a dictionary of all lines found
def readConnections():
    connectDict = {}
    fileOBJ = open('connections.txt', 'r')
    for line in fileOBJ:
        temp = line.split(":")
        connectDict[temp[0]] = [temp[1], temp[2], temp[3].rstrip("\n")]
    fileOBJ.close()
    return connectDict

#Function for removing saved ssh connections and saves/overwrites file
def removeSSH(conName):
    #Displays the connection data to remove and asks if they are sure they want to remove it
    connections = readConnections()
    del connections[conName]
    
    file_object = open('connections.txt', 'w')
    for key in connections:
        file_object.write(f'{key}:{connections[key][0]}:{connections[key][1]}:{connections[key][2]}\n')
    file_object.close()

    print("\nConnection was removed. You can list connections using -list argument.\n")

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
        print("\nusage: \"python3 ssh-tool.py -help\"\n")
    else:
        #Running the program with -help will list all command and usages (usage: "python3 ssh_tool.py -help") -h or -help
        if sys.argv[1] == '-help' or sys.argv[1] == '-h':
            print("\n-add will add new ssh connection \n\t(usage: \"python3 ssh-tool.py -add name-connection username password ip-address\")")
            print("-rem will remove the ssh connection \n\t(usage: \"python3 ssh-tool.py -rem name-connection\")")
            print("-con will connect to the given ssh name \n\t(usage: \"python3 ssh-tool.py -con name-connection\")")
            print("-list will list all ssh name of ssh connections \n\t(usage: \"python3 ssh-tool.py -list\")")
            print("-usri will open terminal user interface \n\t(usage: \"python3 ssh-tool.py -usri\")\n")
        
        #Running the program with -add will add a new one (usage: "python3 ssh_tool.py -add name-ssh username password") -a or -add
        elif sys.argv[1] == "-add" or sys.argv[1] == '-a':
            if len(sys.argv) == 6:
                addSSH(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
            else:
                print("\nusage: \"python3 ssh-tool.py -add name-connection username password ip-address\"\n")
        #Running the program with -con will connect to ssh name (usage: "python3 ssh_tool.py -con name-ssh") -c or -con
        elif sys.argv[1] == "-con" or sys.argv[1] == '-c':
            if len(sys.argv) == 3:
                connectSSH(sys.argv[2])
            else:
                print("\nusage: \"python3 ssh-tool.py -con name-ssh\"\n")
        #Running the program with -list will list the ssh name of ssh connections (usage: "python3 ssh_tool.py -list") -l or -list
        elif sys.argv[1] == "-list" or sys.argv[1] == '-l':
            if len(sys.argv) == 2:
                listSSH()
            else:
                print("\nusage: \"python3 ssh-tool.py -list\"\n")
        #Running the program with -usri will open terminal user interface (usage: "python3 ssh_tool.py -usri") -ui or -usri
        #Running the program with -rem will remove the ssh connection (usage: "python3 ssh_tool.py -rem name-ssh") -r or -rem
        elif sys.argv[1] == "-rem" or sys.argv[1] == '-r':
            if len(sys.argv) == 3:
                removeSSH(sys.argv[2])
            else:
                print("\nusage: \"python3 ssh-tool.py -rem name-ssh\"\n")
        
        #Debugging
        #for arg in enumerate(sys.argv):
        #    print(f"Argument: {arg}")

#Add documentation for ssh_tools.py
#Obfuscate program code