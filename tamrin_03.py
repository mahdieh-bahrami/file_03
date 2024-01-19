n1 = "tamrin_03f.txt"
n2 = "tamrin_03fCopy.txt"
file = open(n1,"r")
x = file.read()
print(x)
file.close()
file = open(n2,"w")
file.write(x)
file.close()