#ask input for dictionary adn input file

dictionary = input("Dictionary file => ")
print(dictionary)
inputfile = input("Input file => ")
print(inputfile)
keyboard = input("Keyboard file => ")
print(keyboard)

#save keyboard as a dictionary that the first letter as key and rest letters as values
f = open(keyboard)
s = f.read().strip().split('\n')
key = dict()
for n in s:
    n = n.split(' ')
    s = n.pop(0)
    key[s]=n
f.close()

print('Spellcheck results:')

#read the words from dictionary into a set
d_dictionary = dict()
for word in open(dictionary):
    word = word.strip().split(',')
    d_dictionary[word[0]]=word[1]

 #see whether the word is in the dictionary
for word in open(inputfile):
    ow = word.strip()
    Continues = False
    if word.strip() in d_dictionary:
        print('{:15} -> {:15} :FOUND'.format(word.strip(),word.strip()))
        
   
   #see whether drop a single letter from the word could match with the words in dictionary 
    elif word not in d_dictionary:
        word_right = set()
        word_match = []
        word = word.strip()
        for n in range(len(word)):
            new_word = list(word)
            new_word.pop(n)
            if ''.join(new_word) in d_dictionary:
                new_word =  ''.join(new_word)
                word_right.add(new_word)
        
        
        #see whether swap two consectuvie letters could match with the words in dictionary
        for n in range(len(word)-1):
            new_word = list(word)
            new_word[n],new_word[n+1]=new_word[n+1],new_word[n]
            if ''.join(new_word) in d_dictionary:
                new_word =  ''.join(new_word)
                word_right.add(new_word)
        
        # see replace letters of word, whether it will match words from dictionary  
        for n in range(len(word)):
            new_word = list(word)
            for i in key[new_word[n]]:
                new_word[n] = i
                if ''.join(new_word) in d_dictionary:
                    word_right.add(''.join(new_word))
        
        #find threes words that with the highest frequency      
        for n in word_right:
            Continues = True
            word_match.append((d_dictionary[n],n))
        word_match.sort()
        word_match.reverse()
        #situation that words that are matched are less or equal to three words
        if len(word_match)<=3:
            n = 1
            for word in word_match:
                print('{:15} -> {:15} :MATCH '.format(ow,word[1])+str(n))
                n += 1
        #situation that words that are matched are more than three words         
        elif len(word_match)>3:
            n =1
            while n < 4:
                for i in range(3):
                    print('{:15} -> {:15} :MATCH '.format(ow,word_match[i][1])+str(n))
                    n += 1    
            
        if Continues:
            continue
        
        #words left that are not match
        print('{:15} -> {:15} :NO MATCH'.\
              format(word.strip(),word.strip()))