user_input = input("enter your paragraph: ")
#print (user_input)

find_string = input("enter find string: ")

split_string = user_input.split()
count = 0

for i in split_string:
    if find_string in i:
        count+=1
    else:
        pass
if count == 0:
    print ("match not found")
else:
    print (count)
