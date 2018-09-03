name=str(input("Filename => "))#temp_data_short.txt temp_data.txt
print(name)
month=int(input("Month => "))#input data name and month
print(month)


dataname = open(name,"r")
str1 = dataname.read()
list = str1.strip('\n').split('\n')
data=[]
for n in range(len(list)):
    thelastmonth = list[n].split(',')
    data.append(thelastmonth)

themonth=[]
month2=1
while month2 < len(data):  
    date = data[month2][1].split('-')
    data[month2].remove(data[month2][1])
    data[month2].insert(1,date)
    if month == int(date[1]):
        themonth.append(data[month2])
    month2+=1

sum1=[]
for i in range(len(themonth)):
    if themonth[i][-3]!='':
        sum1.append(float(themonth[i][-3]))
avg=sum(sum1)/len(sum1)
print("Earliest recorded average {0:.2f} in {1}".format(float(themonth[0][-3]),themonth[0][1][0]))
print("Latest recorded average {0:.2f} in {1}".format(float(themonth[-1][-3]),themonth[-1][1][0]))
print("Average temperature: {0:.2f}".format(avg))