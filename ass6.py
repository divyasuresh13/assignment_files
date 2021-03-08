file_obj = open("newfile.txt","a")
for i in range(1,3):
    file_obj.write("Hello")
file_obj.close()