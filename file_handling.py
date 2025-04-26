# f = open("demofile.txt", "rt")
# print(f.read())
# print(f.read(2))
# print(f.readline())
# print(f.readline())

# for x in f:
#     print(x)
#
# f.close()
#

# append
# f = open("demofile.txt", "a")
# f.write("Now the file has more content!")
# f.close()
#
# #open and read the file after the appending:
# f = open("demofile.txt", "r")
# print(f.read())

# overwrite
# f = open("demofile.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()
#
# #open and read the file after the overwriting:
# f = open("demofile.txt", "r")
# print(f.read())

# f = open("myfile.txt", "w")
# print(f)
# f.close()

# f = open("myfile.txt", "x")
# print(f)
# f.close()

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

import os
os.rmdir("myfolder")
