def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open("ak-" + filename, "wb")
    file.write(data)
    file.close()
    
def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()
    

print("\n\n-----------------------------------------------------------------------\n")
print("----------------------- ENCRYPT AND DECRYPT ---------------------------\n")
print("-----------------------------------------------------------------------\n")
print("----------------------------------------------------------- By Ak017 --\n\n")
print("\tNote : Fist copy the required file to this current location\n")
print("\t       If you try to decrypt file with incorrect key it will damage your encrypted file\n")
choice = ""
while choice != "3":
    print(" Please select you option.")
    print(" 1. Encrypt File")
    print(" 2. Decrypt File")
    print(" 3. Quit\n")
    choice = input()
    if choice == "1" or choice == "2":
        key = int(input("\nEnter a key : "))
        filename = input("\nEnter filename with extension: ")
    if choice == "1":
        Encrypt(filename, key)
    if choice == "2":
        Decrypt(filename, key)