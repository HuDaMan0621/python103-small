# $ python3 square2.py
# How big is the square? 10
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********

size = int(input("How big is the square?  "))
confim = f'you entered {int(size)}' #user input
print (confim)                      #prints the number user enters
count = 1                           #starting from 1 
while count <= size:                #while size is smaller than count 
    print('**********')             #print stars 
    count = count + 1               #add 1
    if size < count:                #add 1 until count is larger than size
        break                       #stop

# count = 1

# while count <= 5:
#     print('*****')
#     count = count + 1


# i in range(side):
#     for i in range(side):
#         print('*', end = '  ')
#     print()
