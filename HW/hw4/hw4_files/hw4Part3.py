import hw4_util 
data = hw4_util.read_university_file("university_data.csv")
university_name = input("University name => ")
print(university_name)
firstline = int(input("Line number for first university to compare (1-1000) => "))
print(firstline)
secondline = int(input("Line number for second university to compare (1-1000) => "))
print(secondline)

#function to identify whether the input university is in the data or not
def find_university(data,university_name):
    for n in range(len(data)):
        if data[n][0] == university_name:
            return data[n] 
    return -1

# print 'university not found' if the input university can't find
if find_university(data,university_name)==-1:
    print("University not found")
else:
    print("First university:",data[firstline][0])
    print("Second university:",data[secondline][0])    
    print()
    print("{0:>25}".format('')+\
      "{:>12}".format('First')+\
      "{:>12}".format('Second')+\
      "{:>12}".format('Yours'))
    for i in range(len(data[0])-1):
        print("{0:>25}".format(data[0][i+1])+\
          "{0:>12}".format(data[firstline][i+1])+\
          "{0:>12}".format(data[secondline][i+1])+\
          "{0:>12}".format(find_university(data,university_name)[i+1]))