#one way of file opening
with open("Liza.txt",mode='w+') as l:
    l.write("Hallo!Its me Liza")
with open("Liza.txt",mode='r') as l:   
    print(l.read())

#another way of file opening
f=open("liza.txt",'a')
f.write("\nI love Shawn Mendez's jawline")
f.close()
f=open("liza.txt",'r')
print(f.read())
f.close()