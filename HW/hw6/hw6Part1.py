#ask input for dictionary adn input file
dictionary = input("Dictionary file => ")
print(dictionary)
inputfile = input("Input file => ")
print(inputfile)

#read the words from dictionary into a set
s_dictionary = set()
for word in open(dictionary):
    s_dictionary.add(word)

 #see whether the word is in the dictionary
for word in open(inputfile):
    Continue = False
    if word in s_dictionary:
        print('{:15} -> {:15} :FOUND'.format(word.strip(),word.strip()))
        continue
   
   #see whether drop a single letter from the word could match with the words in dictionary 
    drop_right = []
    #a list that include all the possible change words
    for n in range(len(word)):
        new_word = list(word)
        new_word.pop(n)
        if ''.join(new_word) in s_dictionary:
            new_word =  ''.join(new_word)
            drop_right.append(new_word)
    if len(drop_right)>0:
        drop_right.sort()
        nw = drop_right[0]
        print('{:15} -> {:15} :DROP'.\
              format(word.strip(),nw.strip())) 
        if nw in s_dictionary:
            Continue=True       
        
    if Continue:
            continue
        
    #see whether swap two consectuvie letters could match with the words in dictionary
    swap_right = []
    #a list that include all the possible change words
    for n in range(len(word)-1):
        new_word = list(word)
        new_word[n],new_word[n+1]=new_word[n+1],new_word[n]
        if ''.join(new_word) in s_dictionary:
            new_word =  ''.join(new_word)
            swap_right.append(new_word)
    if len(swap_right)>0:
        swap_right.sort()
        sw = swap_right[0]
        print('{:15} -> {:15} :SWAP'.\
                  format(word.strip(),sw.strip()))
        if sw in s_dictionary:
            Continue=True
            
    if Continue:
        continue
    
    # see replace letters of word, whether it will match words from dictionary  
    replace_right = []
    #a list that include all the possible change words
    for n in range(len(word)):
        letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'y', 'z']
        new_word = list(word)
        for i in range(len(letters)):
            new_word[n] = letters[i]
            if ''.join(new_word) in s_dictionary:
                replace_right.append(''.join(new_word))
    if len(replace_right)>0:
        replace_right.sort()
        rr = replace_right[0]
        print('{:15} -> {:15} :REPLACE'.\
            format(word.strip(),rr.strip()))
        if rr in s_dictionary:
            Continue = True
                
    if Continue:
        continue 
    
    #words left that are not match
    print('{:15} -> {:15} :NO MATCH'.\
          format(word.strip(),word.strip()))       
          
            
            
    
        