import re
def ReverseParagraph(x):
    end = re.compile('[.]')
    newsentence = end.split(x)
    return newsentence


if __name__ == '__main__':
    p = input("Enter Sentence :")
    x = ReverseParagraph(p)
    for s in x:
        a = s.strip()
        words = a.split()
        rev_sentence = " ".join(reversed(words[:-2])) +" "+ " ".join(words[-2:])
        print (rev_sentence)
