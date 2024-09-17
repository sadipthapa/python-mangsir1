# f=open("text.txt")
# print(f.readlines()[0])
# f.close()


with open("text.txt",'a') as f:
    f.write("\n added from python sc")
