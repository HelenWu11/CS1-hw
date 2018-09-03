filename = input()
print("Filename =>",filename)
month = int(input())
print("Month =>",month)
f = open(filename)
s = f.read()
f.close()

#split the txt into each single line
f = open(filename)
line_list = []
month_temp = []
s = s.split('\n')

#split each line into a list with different parts as parts of the list
for n in range(len(s)-1):
    #find month of each year
    if s[n].split(',')[1].count('-0'+str(month))==1:
        s[n] = s[n].replace('\n',',')
        s[n] = s[n].split(',')
        s[n][1]=s[n][1].replace('-',',')
        s[n] = ','.join(s[n])
        s[n] = s[n].split(',')
        month_temp.append(s[n]) 
    
    elif s[n].split(',')[1].count('-'+str(month))==1:
        s[n] = s[n].replace('\n',',')
        s[n] = s[n].split(',')
        s[n][1]=s[n][1].replace('-',',')
        s[n] = ','.join(s[n])
        s[n] = s[n].split(',')
        month_temp.append(s[n]) 
        
#earliest recorded average temperature with the year    
print("Earliest recorded average {:.2f}"\
      .format(float(month_temp[0][10])),\
      "in", str(month_temp[0][1]))

# latest recrorded average temperature with the year
print("Latest recorded average {:.2f}"\
      .format(float(month_temp[len(month_temp)-1][10])),\
      "in", str(month_temp[len(month_temp)-1][1]))

sum_avetemp = 0
num_avetemp = 0
#find average temperature with all the vaild data
for n in range(len(month_temp)):
    if month_temp[n][10] != '':
        sum_avetemp += float(month_temp[n][10])
        num_avetemp += 1       
print("Average temperature: {:.2f}".\
      format(sum_avetemp/num_avetemp))

min_temp = []
min_ntemp = []
#find the minimum tempture within all the valid data
for n in range(len(month_temp)):
    if month_temp[n][12] != '':
        min_temp.append(float(month_temp[n][12]))
        min_ntemp.append(n)
print("Lowest min value recorded: {:.2f}".format(min(min_temp)),\
      "in year(s): "+str(month_temp[min_ntemp[min_temp.index(min(min_temp))]][1]))

max_temp = []
max_ntemp = []
#find the maximum temptrue within all the valid data
for n in range(len(month_temp)):
    if month_temp[n][11] != '':
        max_temp.append(float(month_temp[n][11]))
        max_ntemp.append(n)
print("Highest max value recorded: {:.2f}"\
      .format(max(max_temp)),\
      "in year(s): "+str(month_temp[max_ntemp[max_temp.index(max(max_temp))]][1]))

print("Histogram of average temperature")
average = []
year = []
sum_average = 0
sum_number = 0
#find the valid data
for n in range(len(month_temp)):
        if month_temp[n][10] != '':
            average.append(month_temp[n][10])
            year.append(month_temp[n][1])           

#situation that the length of the list is less than 10 years
if len(average)<=10:
    sum_average += float(month_temp[n][10])
    sum_number += 1    
    print(year[average.index(average[0])]+'-'\
          +year[average.index(average[len(average)-1])]+':'+' '+\
          int(sum_average/sum_number)*'*')   

#situation that the length of the list is more than 10 years    
if len(average)>10:
    #when the lenght can't divide by 10 years
    if len(average)%10 != 0:
        len_average = int(len(average)/10)+1
        number = 0
        times = 0
        #there are (len_average) interval, and one interval has less than 10 years
        while number < len_average-1:
            sum_average = 0
            sum_number = 0
            average_list = []
            year_list = []
            #there are ten years in each interval, not including the last interval
            for n in range(10):
                #find average of each ten years, which is each interval
                sum_average += float(average[n+times])
                average_list.append(average[n+times])
                year_list.append(year[n+times])
                sum_number += 1                
            print(year[times]+'-'+year[n+times]+':'+' '+\
          int(sum_average/sum_number)*'*') 
            number+=1
            times +=10
            
        sum_average = 0
        sum_number = 0
        #count average for the last interval
        for n in range(len(average)-times):
            sum_average += float(average[times+n])
            sum_number += 1
        print(year[times]+'-'+year[n+times]+':'+' '+\
          int(sum_average/sum_number)*'*') 
            
    #situation that the years can be divided by 10         
    else:
        len_average = int(len(average)/10)
        number = 0
        times = 0
        while number < len_average:
            sum_average = 0
            sum_number = 0
            average_list = []
            year_list = []
            for n in range(10):
                sum_average += float(average[n+times])
                average_list.append(average[n+times])
                year_list.append(year[n+times])
                sum_number += 1                
            print(year[times]+'-'+year[n+times]+':'+' '+\
          int(sum_average/sum_number)*'*')         
            number+=1
            times +=10
    
