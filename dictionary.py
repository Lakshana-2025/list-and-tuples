sen=input("Please enter a sentence: ").split()
dic={"store":"shop","car":"bike","bus":"train","dad":"mom","bro":"sis","sun":"moon"}
for word in sen:
    if word in dic:
        word=dic[word]
        print(word,end=" ")
    else:
        print(word,end=" ")
