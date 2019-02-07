#Weimin Gao
#CSC 113 moring

#For test code 
testStr = "aBCdde 123asb a c b23123ced !@~@#bcd"
testStr2 = "1231 ABCCDE !@%#^^#ABC ZZZ AAA"
test_file=open("test.txt","w") 
print(testStr, file = test_file) 
print(testStr2, file = test_file)
test_file.close  
#End of test code

n = input("Please enter your n value: ")
keyChar = input ("Please enter a special alphabetic character: ")
key_file = open("key_file.txt", "w")
print(n, file = key_file)
print(keyChar, file = key_file)
key_file.close

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
    print (newStr)# For test 
    print(newStr, file = encrypted_file) 
    newStr = ""
    Str = test_file.readline()
encrypted_file.close