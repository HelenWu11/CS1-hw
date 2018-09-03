a = input("Word => ")
print(a)
b = input("#columns => ")
print(b)
c = input("#rows => ")
print(c)
print("Your word is:", str(a)+"\n")

print("(a)")
print((("***"+" ")*int(int(b)-1)+"***"+"\n")*int(c))

print("(b)")
print((("***"+" ")*int(int(b)-1)+"***"+"\n")*(int((int(c)-1)/2))+("***"+" ")*int((int(b)-1)/2)+"CS1",("***"+" ")*int(((int(b)-1)/2)-1)+"***")
print((("***"+" ")*int(int(b)-1)+"***"+"\n")*int((int(c)-1)/2))

print("(c)")
print(("***"+" ")*int((int(b)-1)/2),"|"," "+("***"+" ")*int(((int(b)-1)/2)-1)+"***")
print((("***"+" ")*int(int(b)-1)+"***"+"\n")*int(((int(c)-1)/2)-1),"|"," "+("***"+" ")*int(((int(b)-1)/2)-1)+"CS1",("***"+" ")*int(((int(b)-1)/2)-1),"|"+" ")
print((("***"+" ")*int(int(b)-1)+"***"+"\n")*int(((int(c)-1)/2)-1)+("***"+" ")*int((int(b)-1)/2),"|"," "+("***"+" ")*int((int(b)-1)/2-1)+"***")
