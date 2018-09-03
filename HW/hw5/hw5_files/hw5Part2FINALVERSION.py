data = []
file=input("Filename => ")
print(file)
month=int(input("Month => "))
print(month)
for i in open(file):
    data.append(i.strip().split(','))
data.pop(0)
list_ave = []
list_year = []
list_max = []
list_min = [] 
for i in range (len(data)):
    if int(data[i][1][5:])==month:
        if data[i][10] != '':
            list_max.append((float(data[i][10]),data[i][1][:4]))
        if data[i][11] != '':
            list_min.append((float(data[i][11]),data[i][1][:4]))
        if data[i][9] != '':
            list_ave.append(float(data[i][9]))
            list_year.append(data[i][1][:4])
            
total_average=sum(list_ave)/len(list_ave)
list_min.sort()
list_max.sort()
print("Earliest recorded average {0:.2f} in {1}".format(list_ave[0],list_year[0]))
print("Latest recorded average {0:.2f} in {1}".format(list_ave[-1],list_year[-1]))
print("Average temperature: {0:.2f}".format(total_average))
print("Lowest min value recorded: {0:.2f} in year(s): {1}".format(list_min[0][0],list_min[0][1]))
print("Highest max value recorded: {0:.2f} in year(s): {1}".format(list_max[-1][0],list_max[-1][1]))
print("Histogram of average temperature")
i=0

while i<len(list_year):
    if i+9<len(list_year):
        s=sum(list_ave[i:i+10])/10
        print(str(list_year[i])+"-"+str(list_year[i+9])+":"+" "+"*"*int(s))
          
    else: 
        s = sum(list_ave[i:-1])/len(list_ave[i:-1])
        print(str(list_year[i])+"-"+str(list_year[-1])+":"+" "+"*"*int(s))
    i+=10
        
