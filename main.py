from ftplib import FTP
from getpass import getpass
from os import path

host = input("Host > ")
port = 21
user = input("User for {}:{} > ".format(host, port))
password = getpass("Password for {} on {}:{} > ".format(user, host, port))
debuglevel = 1


def store(connection, *args):
    "Store a file (opened in binary mode) specified by the user"
    filename = input("Filename to store > ") if not args else args[0]
    if path.exists(filename):
        fn_to_send = path.split(filename)[1]
        with open(filename, "rb") as fileobject:
            ret = connexion.storbinary("STOR " + fn_to_send, fileobject)
            print(ret)
    else:
        print("[!] {} didn't exist in the current local working directory !".format(filename))


def ls(connection, *args):
    "List the file in the current working directory"
    ret = connection.dir(*args)
    print(ret)


def del_(connection, *args):
    "Delete a file specified by the user"
    to_del = input("File to delete > ") if not args else args[0]
    ret = connection.delete(to_del)
    print(ret)


def ren(connection, *args):
    "Rename a file specified by the user"
    to_ren = input("Filename to change > ") if not args else args[0]
    new_name = input("New name for {} > ".format(to_ren)) if len(args) <= 1 else args[1]
    ret = connection.rename(to_ren, new_name)
    print(ret)


def mkd(connection, *args):
    "Make a new directory specified by the user"
    dir_name = input("New dir name > ") if not args else args[0]
    ret = connection.mkd(dir_name)
    print(ret)


def cwd(connection, *args):
    "Change the current working directory"
    new_cwd = input("New working directory > ") if not args else args[0]
    ret = connection.cwd(new_cwd)
    print(ret)


def cd(connection, *args):
    "Get the current working directory"
    ret = connection.pwd()
    print(ret)


def size(connection, *args):
    "Get the size of a filename specified by the user"
    filename = input("File to size > ") if not args else args[0]
    ret = connection.size(filename)
    print(ret)


def rmd(connection, *args):
    "Remove a directory specified by the user"
    dir_name = input("Directory to delete > ") if not args else args[0]
    ret = connection.rmd(dir_name)
    print(ret)


commands = {
    "store": store,
    "ls": ls,
    "del": del_,
    "ren": ren,
    "mkd": mkd,
    "cwd": cwd,
    "cd": cd,
    "size": size,
    "rmd": rmd
}

print()

connection = FTP()
connection.connect(host, port)
connection.login(user, password)
connection.set_debuglevel(debuglevel)

print("\n" + connection.getwelcome() + "\n")

while True:
    usercommand = input("\n$ ")
    cmd, *args = usercommand.split(" ")
    
    if cmd in commands.keys():
        commands[cmd](connection, *args)
    elif cmd == "quit":
        break
    elif cmd == "help":
        for k, v in commands.items():
            print("\t- {} :\n{}\n".format(k, v.__doc__))
        print("\t- quit :\nClose the connection")
    else:
        print("Unrecognized command.")

connection.quit()
