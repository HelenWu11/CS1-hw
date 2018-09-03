def time_to_seconds(h,m,s):
    return h*3600+m*60+s
def seconds_to_str(second):
    H = second//3600
    M = (second-H*3600)//60
    S = second-H*3600-M*60
    return str(H)+" "+"hours"+" "+str(M)+" "+"mins"+" "+str(S)+" "+"secs"

print("A day in 2017 is 23 hours 56 minutes and 4 seconds long.")
print("Which is equivalent to",time_to_seconds(23,56,4),"seconds.")
a = input("Enter a future year => ")
print(a)

print("A day in year",int(a),"will be",int(time_to_seconds(23,56,4)+(6*(int(a)-2017)/900000000)*3600),"seconds long")
print("which is equivalent to",seconds_to_str(int(time_to_seconds(23,56,4)+(6*(int(a)-2017)/900000000)*3600)))

