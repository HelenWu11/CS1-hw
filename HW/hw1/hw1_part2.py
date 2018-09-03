First = input("First => ")
print(First)
Second = input("Second => ")
print(Second)
print("Example variable names")

a = str(First) + "_" + str(Second)
print("Lower case:", a.lower())

b = str(First) + "_" + str(Second)
print("For constants:", b.upper())

c = str(First) +" "+ str(Second)
print("Camel case:", (c.title()).replace(" ",""))

d = "_" + str(First) + "_" + str(Second)
print("System variables:", d.lower())

f = str(First) + "_" + str(Second)
print("Silly variable:", (f.replace("a", "_").replace("e", "_")).lower())
