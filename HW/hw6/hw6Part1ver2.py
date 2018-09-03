def find_way(i):
    if i in found_list:
        return 'FOUND'
    elif i in drop_list:
        return 'DROP'
    elif i in swap_list:
        return 'SWAP'
    elif i in replace_list:
        return 'REPLACE'
    elif i in left_list:
        return 'NO MATCH'
#input 

#dict_name = input().strip()
dict_name = 'words_10pt.txt'
input_dict = open('words_10pt.txt')
print('Dictionary file =>',dict_name)
list_dict = input_dict.read().strip().split('\n')
set_dict = set(list_dict)

#file_name = input().strip()
file_name = 'input_words.txt'
input_file = open(file_name)
print('Dictionary file => ',file_name)
list_file = input_file.read().strip().split('\n')
set_file = set(list_file)

right_list = list()
found_list =set()
drop_list = set()
swap_list = set()
replace_list= set()
left_list = set()
letters = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z' }

for word in list_file :
    set_change = set()
    jdg = True
    if word in set_dict:
        found_list.add(word)
        set_change.add(word)
        right_list.append(set_change)
        continue 
    
    list_char = list(word)
    
    #drop
    for num in range(len(list_char)):
        x = list_char[:]
        x.pop(num)
        if ''.join(x) in set_dict:
            drop_list.add(word)
            set_change.add(''.join(x))
            jdg = False 
            
    
    #swap
    char = 0
    if jdg:
        while char < len(list_char)-1:
            lst = list_char[:]
            c = lst.pop(char)
            lst.insert(char+1,c)
            if ''.join(lst) in set_dict:
                swap_list.add(''.join(list_char))
                set_change.add(''.join(lst))
                jdg = False 
            char+=1
        
    #replace
    n_change = list_char[:]
    if jdg:
        for num_l in letters:
            for num_n in range(len(n_change)):
                n=n_change[:]
                n[num_n] = num_l
                if ''.join(n) in set_dict:
                    replace_list.add(''.join(n_change))
                    set_change.add(''.join(n))
    if jdg:
        left_list.add(word)
        set_change.add(word)
            
    right_list.append(set_change) 
            
'''
for i in set_file:
    n = list(i)
    n_change = n[:]
    for num_n in range(len(n)):
        for num_l in letters:
            n[num_n] = num_l
            if ''.join(n) in set_dict:
                set_replace.add(''.join(n_change))
                right_list.append((''.join(n_change),''.join(n)))
                continue 
            n=n_change[:] 
'''
#print(right_list)
'''
for n in range(len(list_file)) :
    for right in list_dict:
        if right in right_list[n]:
            right_word = right
            way = find_way(list_file[n])
        else: 
            way = find_way(list_file[n])
            right_word = list_file[n]
'''
#print(replace_list)
#print(found_list)
#print(list_dict)
#print(right_list,'\n',len(right_list),'\n',len(list_file),print(list_file))
#print(set_file)
print(right_list)

for n in range(len(right_list)):
    right=''
    jdg = True
    for check in list_dict:
        if check in right_list[n]:
            right = check 
            #print(right)
            jdg = False 
            break
            #right = list_file[n]
    if jdg:
        right= sorted(right_list[n])[0]
    print('{0:15}->{1:15}:{2:15}'.format(list_file[n],right,find_way(list_file[n])))
            
        
        
    