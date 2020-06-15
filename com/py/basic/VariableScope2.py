def outer_function():
    b = 20
    print("b : ", b)

    def inner_func():
        c = 30
        print("c : ", c)
      #  b = b+20       #won't let you update the existing value
        print("updated b : ", b)

    inner_func()


a = 10
print("a : ", a)
outer_function()
