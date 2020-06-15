a = 50

def outer_function():
    a = 10
    print("a called from inside outer_function : ", a) #this will print the 10 from outer_function

    def inner_function():
        a = 20
        print("a called from inside inner_function : ", a)  #this will print the 20 from inner_function

    inner_function()
    print("a : ", a)    #this will print the 10 from outer_function


print("a called from global : ", a) #this will print the 50 from global module
outer_function()
print("a called from global : ", a) #this will print the 50 from global module

