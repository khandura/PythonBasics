import sys

print("argument is : "+sys.argv[0])
print('# this is not  a comment')

print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")