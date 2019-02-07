#Weimin Gao
#CSC 113 moring
#midterm project
#10/26/2017

#For test code 
#testStr = "aBCdde 123asb a c b23123ced !@~@#bcd"
#testStr2 = "1231 ABCCDE !@%#^^#ABC ZZZ AAA"
#test_file=open("test.txt","w") 
#print(testStr, file = test_file) 
#print(testStr2, file = test_file)
#test_file.close 
#End of test code

import random
#The encryption phase:
#A)The key file:
n = random.randint(-1, 25)
temp = random.randint(97, 122)
keyChar = chr(temp)
key_file = open("key_file.txt", "w")
print(n,keyChar, file = key_file)
key_file.close 

#B)Encrypting the file:
newStr = ""
newWord = ""
test_file = open("test.txt","r")
Str = test_file.readline()  
encrypted_file=open("encrypted.txt","w") 
while (Str != ""):
    Str = Str.lower()
    Split = Str.split()
    StrLen = len(Split)
    for i in range (StrLen):
        word=Split[i]
        word_list = list(word)
        listLen = len(word_list)
        for j in range (listLen):
            if (isinstance(word_list[j],int) == False):
                if (word_list[j] >= 'a' and word_list[j] <= 'z'):
                    if (word_list[j] == keyChar):
                        word_list[j]=word_list[j].upper()
                    else:
                        check = ord(word_list[j])+n
                        if (check < 97):
                            check = check-96+122
                        if (check > 122):
                            check = check-123+97
                        word_list[j]=chr(check)
            newWord = newWord + word_list[j]
        if (i == StrLen-1):
            newStr = newStr + newWord + " "
        else:
            newStr = newStr + newWord + " " 
        newWord = ""
    print(newStr, file = encrypted_file) 
    newStr = ""
    Str = test_file.readline()
encrypted_file.close

#encrypted_file=open("encrypted.txt","r") # For test code
#print(encrypted_file.read())        # For test code

#The decryption phase:
#A)Reading the key file: 
key_file=open("key_file.txt","r")
key_data = key_file.readline()
data_list = key_data.split()
temp = data_list[0]
n2 = int(temp)
keyChar2 = data_list[1]

#B)Decrypting the file:
newStr = ""
newWord = ""
encrypted_file=open("encrypted.txt","r")
Str2 = encrypted_file.readline()
decrypted_file=open("decrypted.txt","w")
while (Str2 != ""):
    Split2 = Str2.split()
    Str2Len = len(Split2)
    for i in range (Str2Len):
        word2=Split2[i]
        word_list2 = list(word2)
        list2Len = len(word_list2)
        for j in range (list2Len):
            if (isinstance(word_list2[j],int) == False):
                if (word_list2[j] >= 'a' and word_list2[j] <= 'z'):
                    check2 = ord(word_list2[j])-n2
                    if (check2 < 97):
                        check2 = check2-96+122
                    if (check2 > 122):
                        check2 = check2-123+97
                    word_list2[j]=chr(check2)
                else:
                    word_list2[j]=word_list2[j].lower()
            newWord = newWord + word_list2[j]
        if (i == Str2Len-1):
            newStr = newStr + newWord + " "
        else:
            newStr = newStr + newWord + " " 
        newWord = ""
    print(newStr, file = decrypted_file) 
    newStr = ""
    Str2 = encrypted_file.readline()
decrypted_file.close

#decrypted_file=open("decrypted.txt","r") # For test code
#print(decrypted_file.read())        # For test code