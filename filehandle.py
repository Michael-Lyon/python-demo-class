
"""
'a' -> append mode. This would oppen up the file and append changes(read, write).
It creates a file if it doesn't exist

'w' -> write mode. This allows to write to a file. If the file already contains content, it'll overwrite.
It creates a file if it doesn't exist

'r' -> read mode. This is just used to read the file
This is the defult mode
"""
# from pprint import pprint
# fhand = open("demo.txt")
# num_lines = 0
# frequency = {}
# # The setdefault() method returns the value of the item with the specified key
# # If the key does not exist, insert the key, with the specified value
# for line in fhand:
#     for word in line.split():
#         frequency.setdefault(word, 0)
#         frequency[word] += 1
# # pprint(frequency)
# fhand.close()

# #  replace a text in the file
# with open("demo.txt", "r+") as file:
#     content = file.readlines()
#     for line in content:
#         if "To" in line:
#             pos  = line.index("To")
#             line = line.replace("To", "new text")
            
#     file.seek(0)
#     file.writelines(content)

    

"""
CREATE A PROGRAM TO READ AND WRITE INTO A TXT FILE;

The program should prompt the user to enter the name of a file.
if the file exists, it should let the user know and alow the user anme chnages into the file by adding content or changing words in the file.

If the file doesn't exist it should create the file and allow the user be able to write into the file. and also be able to make changes to the file.

before a user is able to make any chnage to a file they should 
see the content of the file.
"""

# read the file -> try except error
#  if file exist -> open file in append -> allow the user add text to the file
# print tyhe content and aloow the user change the content(a word)
#  if not exist -> create the file in except block -> allow user write to file
# print the file content and allow for changes

filename = input("Enter file name: ")
try:
    file = open(filename)
except FileNotFoundError as e:
    print("File not found")    
    cmd = input("create file y/n: ")
    if cmd == "y":
        file = open(filename, "w")
        choice = input("write to file? y/n: ")
        if choice == "y":
            while True:
                line = input('Type here: ')
                if line == "done":
                    file.close()
                    break
                else:
                    file.write(line+"\n")
                