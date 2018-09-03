import math

def find_next(bears,berries,tourists):
    if bears>=0 and berries>=0:
        bears_next = berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1) 
        berries_next = (berries*1.5) - (int(bears)+1)*(berries/14) - (math.log(1+tourists,10)*0.05) 
        if bears_next <0:
            bears_next=0
        elif berries_next <0:
            berries_next =0.0
        return (int(bears_next),berries_next)

   
Bears = int(input())
print("Number of bears =>",Bears)
Berries = input()
print("Size of berry area =>",Berries)
Berries = float(Berries)
if Bears<4 or Bears>15:
    tourists = 0
elif Bears<=10:
    tourists = 10000*Bears
elif Bears>10:
    tourists = 100000+20000*(Bears-10)  
  
print("Year"+'\t'+"Bears"+'\t'+"Berries"+'\t'+"Tourists")

year = 1
bears_pop = []
berries_pop = []
tourists_total = []
while year < 11:
    if Bears<4 or Bears>15:
        tourists = 0
    elif Bears<=10:
        tourists = 10000*Bears
    elif Bears>10:
        tourists = 100000+20000*(Bears-10)   
    tourists_total.append(tourists)
    
    print(str(year)+'\t'+str(Bears)+'\t'+str(round(Berries,1))+'\t'+str(tourists))
    bears_pop.append(int(Bears))
    berries_pop.append(Berries)    
    (Bears,Berries) = find_next(Bears,Berries,tourists)
    
    year+=1
print()
print("Min:"+'\t'+str(min(bears_pop))+'\t'+str(round(min(berries_pop),1))+'\t'+str(min(tourists_total)))
print("Max:"+'\t'+str(max(bears_pop))+'\t'+str(round(max(berries_pop),1))+'\t'+str(max(tourists_total)))