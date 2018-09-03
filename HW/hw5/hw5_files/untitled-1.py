line = ''
for n in range(9):
    line = line+str(n)+' '
    
row_list = []
for n in line:
    if n != ' ':
        new_line = ''
        for i in range(9):
            new_line += n+','+str(i)+' '
        row_list.append(new_line)
print(row_list)

for small in row_list:
    for range(3):
        
    print(small)