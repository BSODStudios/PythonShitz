#Secure notepad written by Jacob Cohen
from subprocess import call



import sys
import time

shift = int("13")

def caesar(plainText, shift): 
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            ch.lower()
            stayInAlphabet = ord(ch) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)

            
        else:
            finalLetter = ch
            
                
        cipherText = cipherText + finalLetter
        
        

    #print ("Your ciphertext is: ", cipherText)

    print ("Encryption: ", cipherText)
    time.sleep(2)
    return cipherText


def caesar_reshift(plainText, shift): 
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            ch.lower()
            stayInAlphabet = ord(ch) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
        
        else:
            finalLetter = ch
        cipherText = cipherText + finalLetter
        
        

    #print ("Your ciphertext is: ", cipherText)
    return cipherText


#User


############PASSWORD HERE v v v############################ RIGHT HERE |
#                                                                      V
passw = " "

call('color e', shell=True)

#Secure notepad logo
print("                                            _                       _ ")
time.sleep(0.1)
print("                                           | |                     | |")
time.sleep(0.1)
print(" ___  ___  ___ _   _ _ __ ___   _ __   ___ | |_ ___ _ __   __ _  __| |")
time.sleep(0.1)
print("/ __|/ _ \/ __| | | | '__/ _ \ | '_ \ / _ \| __/ _ \ '_ \ / _` |/ _` |")
time.sleep(0.1)
print("\__ \  __/ (__| |_| | | |  __/ | | | | (_) | ||  __/ |_) | (_| | (_| |")
time.sleep(0.1)
print("|___/\___|\___|\__,_|_|  \___| |_| |_|\___/ \__\___| .__/ \__,_|\__,_|")
time.sleep(0.1)
print("                                                   | |                ")
time.sleep(0.1)
print("                                                   |_|                ")
time.sleep(0.1)
print(" ______ _   _  _____ _______     _______ _______ ______ _____  ")
time.sleep(0.1)
print("|  ____| \ | |/ ____|  __ \ \   / /  __ \__   __|  ____|  __ \ ")
time.sleep(0.1)
print("| |__  |  \| | |    | |__) \ \_/ /| |__) | | |  | |__  | |  | |")
time.sleep(0.1)
print("|  __| | . ` | |    |  _  / \   / |  ___/  | |  |  __| | |  | |")
time.sleep(0.1)
print("| |____| |\  | |____| | \ \  | |  | |      | |  | |____| |__| |")
time.sleep(0.1)
print("|______|_| \_|\_____|_|  \_\ |_|  |_|      |_|  |______|_____/")
time.sleep(0.3)
print("             .-""-.")
time.sleep(0.1)
print("           / .--. \  ")
time.sleep(0.1)
print("          / /    \ | ")
time.sleep(0.1)
print("          | |    | |  ")
time.sleep(0.1)
print("          | |.-""-.| | ")
time.sleep(0.1)
print("         ///`.::::`\  ")
time.sleep(0.1)
print("        ||| ::/  \::;  ")
time.sleep(0.1)
print("        ||; ::\__/::;  ")
time.sleep(0.1)
print("         \\\ '::::' /  ")
time.sleep(0.1)
print("          `=':-..-'`  ")
time.sleep(0.1)
print("Developed by Jacob Cohen (yakovliam)")
time.sleep(0.2)








def write():
    shift = int("13")
    file = open("SNPFile.snp","w")
    print("Opening file...")
    time.sleep(2)
    plainText = input("> ")
    
    cipherWrite = caesar(plainText, shift)
    file.write(cipherWrite)

    file.close()
    inter_2_UI()

def append():
    shift = int("13")
    file = open("SNPFile.snp","a")
    print("Opening file...")
    time.sleep(2)
    plainText = input("> ")
    
    cipherWrite = caesar(plainText, shift)
    file.write(" " + cipherWrite)

    file.close()
    inter_2_UI()

def read():
    file = open("SNPFile.snp","r")
    print("Recalling... Please wait...")
    plainText = file.read()
    time.sleep(2)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    plainText = caesar_reshift(plainText, shift)
    print("> " + plainText)
    input("")
    file.close()



def recall_user_note():
    file = open("SNPFile.snp","r")
    print("Recalling... Please wait...")
    time.sleep(2)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("> " + file.read())
    file.close()
    print("\n\n% Press Enter To Change Selection %")
    wait_input = input("")
    inter_2_UI()
    
    


def write_user_note():
    file = open("SNPFile.snp","w")
    print("Opening file...")
    time.sleep(2)
    user_input_write = input("> ")
    file.write(user_input_write)
    file.close()
    inter_2_UI()
    #sys.exit()
    #^remove later
    
    
    
    
def continue_UI():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Test?")
    








def inter_2_UI():
        call('color e', shell=True)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        time.sleep(0.1)
        
        print(" ______ _ _        ")
        time.sleep(0.1)
        print("|  ____(_) |     _ ")
        time.sleep(0.1)
        print("| |__   _| | ___(_)")
        time.sleep(0.1)
        print("|  __| | | |/ _ \  ")
        time.sleep(0.1)
        print("| |    | | |  __/_ ")
        time.sleep(0.1)
        print("|_|    |_|_|\___(_)")
        time.sleep(0.1)
        print("\n")
        time.sleep(0.1)
        print("\n")
        time.sleep(0.1)
        print("\n")
        time.sleep(0.1)
        print("\n")
        time.sleep(0.1)
        print("- Do not write capitals- the encryption method does not support -")
        time.sleep(0.1)
        print("- Logout, Recall, Append, or Write? -: ")
        time.sleep(0.1)
        print("\n")
        time.sleep(0.1)
        print("\n")
        time.sleep(0.1)
        recallorno = input("> ")
        if recallorno == "recall":
            read()
            inter_2_UI()
        
        if recallorno == "append":
            append()
        if recallorno == "write":
            write()
        if recallorno == "logout":
            print("Logging out...")
            time.sleep(3)
            print("Logged out user\n")
            time.sleep(0.5)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            UI()
        if recallorno == "continue":
            continue_UI()
            inter_2_UI()
        else:
            inter_2_UI()

        


def UI():
    
    print("------------------------------------------")
    time.sleep(0.1)
    print("-------------------------------")
    time.sleep(0.1)
    enter_user = input("Please enter your username: ")
    time.sleep(3)
    enter_pass = input("Please enter your password: (0/2) ")

    if enter_pass != passw:
            print("Logging in...")
            time.sleep(2)
            call('color c', shell=True)
            print("Incorrect Password or Username! (1/2) ")
            time.sleep(1)
            call('color e', shell=True)
            enter_pass = input("Please enter your password (1/2) ")
    if enter_pass != passw:
        print("Logging in...")
        time.sleep(2)
        call('color c', shell=True)
        print("Incorrect Password or Username! You will now be exited.(2/2) ")
        time.sleep(1)
        sys.exit()
    else:
        print("Logging in...")
        time.sleep(1)
        call('color a', shell=True)
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou are now logged in.")
        inter_2_UI()

    


UI()

#                                  |
#Code below not part of a function |
#                                  v





