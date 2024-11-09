from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''
def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open("passowrd.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account name: ")
    pwd = input("password: ")

    with open("passowrd.txt","a") as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n")

while True:
    print("what you wnat to do ?")
    print("if you want to quite typ -> q")
    mode = input("view add -> ").lower()
    if(mode =="q"):
        print("thankuu :) byee")
        break

    if(mode == "view"):
        view()
    elif(mode=="add"):
        add()
    else:
        print("....invalid input...")
        continue