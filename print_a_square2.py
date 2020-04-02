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

 
side = int(input("How big is the square?  "))

print("Square Star Pattern") 

for i in range(side):
    for i in range(side):
        print('*', end = '  ')
    print()
