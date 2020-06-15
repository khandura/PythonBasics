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


replace_string()
toggle_string_case()
slit_string()
