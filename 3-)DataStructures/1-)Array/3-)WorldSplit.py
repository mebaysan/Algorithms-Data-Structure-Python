"""
input  -> ["deeplearning","d,dll,a,deep,dee,base,lear,learning"]
output -> ['deep','learnign']
"""

def word_split(liste):
    word = list(liste[0]) # "deeplearning" -> ["d","e",...]
    d = liste[1].split(',') # ["d","dll","a","deep","dee","base","lear","learning"]

    for i in range(1,len(word)):
        c = word[:]
        c.insert(i," ")
        x,y = "".join(c).split() # "d", "eeplearning"        "de","eplearning"
        if x in d and y in d:
            return f"{x},{y}"
    return "Bulamadım"

print(word_split(["deeplearning","d,dll,a,deep,dee,base,lear,learning"]))
print(word_split(["deeplearni2ng","d,dll,a,deep,dee,base,lear,learning"]))
