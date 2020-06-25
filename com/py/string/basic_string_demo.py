def replace_string():
    message = "Python for Beginners"
    print("message : ", message)
    print("message after replace for - FOR : ", message.replace("for", "FOR"))


def toggle_string_case():
    message = "hello"
    print(message)
    print("upper case message : ", message.upper())
    print("lower case message : ", message.lower())

    # print("for" in message)


def slit_string():
    message = "Java, Python, Scala"
    print("Message : ", message)
    message_split = message.split(',')
    print("message after split : ", message_split)
    print("type of message : ", type(message))
    print("type of splitted message ", type(message_split))
    print("length of splitted message : ", len(message_split))


def string_other_methods():
    message = "Python Demo"
    print("message : ", message)
    print("message.capitalize : ", message.capitalize())
    print("message.casefold : ", message.casefold())
    print("message.count('o') : ", message.count('o'))
    print("message.startswith : ", message.startswith('Python'))
    print("message.endswith : ", message.endswith('Demo'))
    print("message.len : ", len(message))
   # message = None
    print("message.len : ", message.__len__())  # this line will produce error as we have set message to None

    print("message.find('mo') ", message.find('mo'))
    print("message.index('y') : ", message.index('y'))
    print("message.join('hello') : ", message.join("hello"))


replace_string()
toggle_string_case()
slit_string()
string_other_methods()
