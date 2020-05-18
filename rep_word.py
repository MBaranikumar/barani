
def rep_word():
    user_input = "Hi hello welcome, this is bigboss. cha chicku chicku chim bigboss"
    #print (user_input)

    #find_string = input("enter find string: ")
    find_string = "bigboss"

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
rep_word()
