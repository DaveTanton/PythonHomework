  
import random as r

def inputcheck (message):
    while True:
        try:
            message = int(input(message))
            if message <= 0:
                message = 'You must enter a valid number only : '
                continue
            else:
                return message
        except:
            message = 'You must enter a valid number only : '

print("**********************")
print("*    Dave Tanton     *")
print("*                    *")
print("* password Generator *")
print("**********************")
print("\nPlease enter the following information as a number:")
while True:
    passwordLength = inputcheck("\nPassword Length : ")
    numberOfPassword = inputcheck("Number of passwords to be generated : ")
    print("")
    count = 0
    while count <= numberOfPassword - 1:
        result = ""
        for each in range(passwordLength):
            result += result.join(chr(r.randint(35, 122)))
        print("password ", count + 1, " : ", result)
        count = count + 1
    retry = input("\nGenerate more passwords? Y/N: ").lower()
    if retry == "y":
        continue
    else:
        break
print("\nAll done\nThank you for using this generator")
