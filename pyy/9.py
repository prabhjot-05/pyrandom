with open("lines.txt","w") as f:
    f.writelines(["Hello ","How are you ","Bye "])
with open("lines.txt", "r") as f:
    line = f.read()
    print(line)