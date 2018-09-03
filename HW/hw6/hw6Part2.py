import textwrap

Continue = True
otherword = True
title = input("Enter a title (stop to end) => ")
print(title) 
print()
while Continue == True:
    # ask for input
    othertitle = []
    beasts_other = set()
    beasts_inset = set()
    #when input is stop, stop
    if title.lower() == 'stop':
        None
        Continue = False
    else:
        # see whether the input word is valid or not
        count = 0 
        count_list = []
        for line in open('titles.txt'):
            if line.lower().count(title) == 0:
                count_list.append('False')
                count +=1
            else:
                count_list.append('True')
                count += 1
        if count_list.count('False')==count:
            print("This title is not found!")
            title = input("Enter a title (stop to end) => ")
            print(title)      
            print()
            otherword = False  
        
        # if the input word is valid    
        for line in open('titles.txt'):
            # find the title that includes the input word
            sline = line.strip().split('|')
            if sline[0].lower().count(title)==1:
                print("Found the following title:",sline[0])
                
                beasts_in = []
                #find beasts in this title 
                for n in range(1,len(sline)):
                    beasts_in.append(sline[n])
                    beasts_inset.add(sline[n])
                beasts_in.sort()
                beasts_in = 'Beasts in this title: ' +', '.join(beasts_in)
                bi = textwrap.wrap(beasts_in)
                for n in bi:
                    print(n)
                print()
                break
            
        # find other books contains the same beasts
        for line in open('titles.txt'):
            line = line.strip().split('|')
            if line != sline:
                for n in beasts_inset:
                    if n in line:
                        othertitle.append(line[0])
                        for i in range(1,len(line)):
                            beasts_other.add(line[i])  
                        break      
        #print beasts that are in common
        if otherword == True:
            othertitle.sort()
            othertitle = 'Other titles containing beasts in common: '+', '.join(othertitle)
            ot = textwrap.wrap(othertitle)
            for n in ot:
                print(n)
            print()
            # find beasts only in the input title book
            beasts_only = list(beasts_inset - beasts_other)
            beasts_only.sort()
            beasts_only = 'Beasts appearing only in this title: ' +', '.join(beasts_only)
            bo = textwrap.wrap(beasts_only)
            for n in bo:
                print(n)
            print()
            title = input("Enter a title (stop to end) => ")
            print(title) 
            print()        
        
        


    