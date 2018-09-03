from syllables import find_num_syllables
Paragraph = input()
print("Enter a paragraph =>",Paragraph)

number = 0
paragraph = Paragraph.split()
while number<len(paragraph):
    if paragraph[number].find('es') == len(paragraph[number])-len('es'):
        paragraph[number] = paragraph[number].replace('es','')
    number += 1
number = 0
while number<len(paragraph):
    if paragraph[number].find('ed') == len(paragraph[number])-len('ed'):
        paragraph[number] = paragraph[number].replace('ed','')
    number += 1     
new_paragraph = ' '.join(paragraph)
new_paragraph = new_paragraph.replace('-',' ')
        
n = 0
num = 0
hardwords_list=[]
while n < len(Paragraph.split()):
    if find_num_syllables(Paragraph.split()[n])>=3 and Paragraph.split()[n].count('-') == 0:
        hardwords_list.append(Paragraph.split()[n])
    num = num + find_num_syllables(Paragraph.split()[n])
    n+=1
   
print("Here are the hard words in this paragraph:")
print(hardwords_list)

ASL = len(Paragraph.split())/int(Paragraph.count('.')) 
#ASL (average sentence length) is given by the number of words per sentence

PHW = len(hardwords_list)/len(Paragraph.split())*100
#PHW: the number of words of three or more syllables that do not contain a hyphen (-) and three-syllable words that do not end with 'es' or ed. 
#Divide this count by the total number of words in the text and multiply the result by 100 to get a percentage

ASYL = num/len(Paragraph.split())
# ASYL (average number of syllables) is given by the total number of syllables divided by the total number of words

print("Statistics: ASL:{:.2f}".format(ASL),\
      "PHW:{:.2f}".format(PHW)+'%'+" "\
      "ASYL:{:.2f}".format(ASYL))
print("Readability index (GFRI): {:.2f}".format(0.4*(ASL + PHW)))
print("Readability index (FKRI): {:.2f}".format( 206.835-1.015*ASL-86.4*ASYL))
