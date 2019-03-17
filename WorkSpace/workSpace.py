#!/bin/python

import sys
import os
import urllib2
import json

data = {}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def  getWorkSpace():
    
    f = open('.sys/data.txt', 'r')
    info = f.read()
    
    data = json.loads(info)
    f.close()
    return data["data"]

def printWindows(workSpace):
    for eWindow in workSpace:
        sWindow = ""
        if eWindow["application"] != "":
            sWindow += "App: \"" + eWindow["application"] + "\" "
        sWindow += "dir: "+eWindow["dir"]
        print "  ", sWindow

def main():
    
    global data
    data = getWorkSpace()
    
    while True:
        print "\r> ",
        line = sys.stdin.readline()
        line = line[:-1]
        args = line.split(" ")
        
        while "" in args:
            args.remove("")
        
        if len(args) == 0:
            continue
    
        command = args[0].lower()
        
        if command == "open":
            openWorkSpace(args)
        
        elif command == "add":
            addWorkSpace(args)
        
        elif command == "delete":
            deleteWorkSpace(args)

        elif command == "list":
            listWorkSpace(args)

        elif command == "save":
            rawData = "{\"data\":"+json.dumps(data)+"}"
            f = open('.sys/data.txt', 'w')
            f.write(rawData)
            f.close()
            print "\r",

        elif command == "help":
            helpMenu()

        elif command == "quit":
            print bcolors.OKBLUE + "\r  Goodbye!" + bcolors.ENDC
            break

    return

def openWorkSpace(args):
    global data
    if len(args) != 2:
        print bcolors.YELLOW + "\r  syntax: open <WorkSpace name>" + bcolors.ENDC
        return
        
    workSpaceName = args[1]
    if workSpaceName not in data:
        print bcolors.YELLOW + "\rWork Space", workSpaceName, "does not exist."
        print "[help] for more about functions" + bcolors.ENDC
        return
        
    print bcolors.OKBLUE + "\r  Work Space: ", workSpaceName + bcolors.ENDC
    for eWindow in data[workSpaceName]:
        osCommand = "open "
        if eWindow["application"] != "":
            osCommand += "-a \"" + eWindow["application"] + "\" "
        osCommand += eWindow["dir"]
        print "  ", osCommand
        os.system(osCommand)

    return

def addWorkSpace(args):
    global data
    if len(args) != 2:
        print bcolors.YELLOW + "\r  syntax: add <WorkSpace name>" + bcolors.ENDC
        return
            
    workSpaceName = args[1]
    if workSpaceName in data:
        print bcolors.YELLOW + "Work Space", workSpaceName, "already exist."
        print "[help] for more about functions" + bcolors.ENDC
        return

    newWorkSpace = ",\""+workSpaceName+"\":"
    newWorkSpace += "["
            
    while True:
        print "Application: ",
        app = sys.stdin.readline()[:-1]
        print "Directory: ",
        dir = sys.stdin.readline()[:-1]
        if dir == "":
            if newWorkSpace[-1:] == ",":
                newWorkSpace = newWorkSpace[:-1]
            break
        newWorkSpace += "{\"application\":"+"\""+app+"\""+","+"\"dir\":\""+dir+"\"},"

    newWorkSpace += "]"
            
    rawData = json.dumps(data)
    rawData = rawData[:-1] + newWorkSpace + "}"

    data = json.loads(rawData)
    json.dumps(data)

    print bcolors.BOLD + "Added", workSpaceName + bcolors.ENDC
    printWindows(data[workSpaceName])

    return

def listWorkSpace(args):

    flag = 0
    workSpaceName = ""
    
    if len(args) == 2:
        if args[1] == "-a":
            flag = 1
        else:
            workSpaceName = args[1]
            flag = 2

    elif len(args) != 1:
        print bcolors.YELLOW + "[help] for more about functions" + bcolors.ENDC
        return
    
    if flag == 2:
        if workSpaceName not in data:
            print bcolors.YELLOW + "Work Space", workSpaceName, "does not exist." + bcolors.ENDC
            return
        
        print bcolors.OKBLUE + " Work Space: ", workSpaceName + bcolors.ENDC
        printWindows(data[workSpaceName])
    
    else:
        keyList = data.keys()
        for key in keyList:
            if key != "__ZERO_INDEX__":
                print bcolors.OKBLUE + "\r ", key + bcolors.ENDC
                if flag == 1:
                    printWindows(data[key])

    return

def helpMenu():
    print bcolors.YELLOW + "\r  [add <WorkSpace name>]" + bcolors.ENDC + " to add new workspace"
    print bcolors.YELLOW + "  [open <WorkSpace name>]" + bcolors.ENDC + " to open existing workspace"
    print bcolors.YELLOW + "  [list < |-a|WorkSpace name>]" + bcolors.ENDC + " to see all workspaces"
    print bcolors.YELLOW + "  [delete <WorkSpace name>" + bcolors.ENDC + " to delete existing workspace]"
    print bcolors.YELLOW + "  [save]" + bcolors.ENDC + " to save the change(s) made"
    print bcolors.YELLOW + "  [quit]" + bcolors.ENDC + " to terminate the program"

    return

def deleteWorkSpace(args):
    global data
    if len(args) != 2:
        print bcolors.YELLOW + "\r  syntax: delete <WorkSpace name>" + bcolors.ENDC
        return
        
    workSpaceName = args[1]
    if workSpaceName not in data:
        print bcolors.YELLOW + "\rWork Space", workSpaceName, "does not exist."
        print "[help] for more about functions" + bcolors.ENDC
        return

    print bcolors.FAIL + "Are you sure about deleting", workSpaceName, "(y/n)? This cannot be undone. " + bcolors.ENDC,
    ans = sys.stdin.readline().lower()[:-1]
        
    if ans != "y":
        print bcolors.YELLOW + "Action aborted." + bcolors.ENDC
        return

    del data[workSpaceName]
    print bcolors.OKBLUE + "Workspace", workSpaceName, "deleted" + bcolors.ENDC

if __name__ == '__main__':
    main()

