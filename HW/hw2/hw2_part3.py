def percentage_happy(sentence):
    sentence = sentence.lower()
    h = sentence.count("laugh")+sentence.count("happiness")+sentence.count("love")+sentence.count("excellent")+sentence.count("good")
    return h/len((sentence.strip()).split(" "))

def percentage_sad(sentence):
    sentence = sentence.lower()
    s = (sentence.lower()).count("bad")+sentence.count("sad")+sentence.count("terrible")+sentence.count("horrible")+sentence.count("problem")
    return s/len((sentence.strip()).split(" "))

a = input("Enter a sentence => ")
print(a)
print("Percentages. happy: {:.3f}".format(percentage_happy(str(a))),"sad: {:.3f}".format(percentage_sad(str(a))))
if percentage_happy(str(a))>percentage_sad(str(a)):
    print("This is a happy sentence")
elif percentage_happy(str(a))==percentage_sad(str(a)):
    print("This is a neutral sentence")
else:
    print("This is a sad sentence")
