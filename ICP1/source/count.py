string=input("Enter string:")
letters=0
numbers=0
for i in string:
      if(i.isdigit()):
            numbers=numbers+1
      elif(i.isalpha()):
          letters=letters+1
print("The number of digits is:")
print(numbers)
print("The number of letters is:")
print(letters)