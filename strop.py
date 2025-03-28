import string

def get_span(S,ss):
    span=[]
    start=0
    while start<len(S):
        
        start=S.find(ss,start)
        if start==-1:
            break
        end=start+len(ss)
        span.append((start,end))
        start+=1
       
    return span
        
def reverseword(s):
    reversed=s[::-1]
    return reversed

def remove_punctuation(s):
    lst=[]
    for w in s:
        if w.isalnum():
            lst.append(w)
    return ''.join(lst)

def count_words(s):
    word=s.split()
    return len(word)


def character_map(s):
    ch={ch:s.count(ch)for ch in s}
    return ch

def transform(string):
    list_of_strings = list(string)
    print(list_of_strings)
    reversed_list = list_of_strings[::-1]
    reversed_sentence = "".join(reversed_list)
    new_sentence = reversed_sentence.swapcase()
    print("Translated/transformed sentence is:- ")
    print(new_sentence)



def makeTitle(s):
    
    return s.title()


    
def normalizespace(s):
    w=s.split()
    return ' '.join(w)

def get_permutations(s, step=0):

    if step == len(s):

        print("".join(s))  

        return
 
    for i in range(step, len(s)):

        s_list = list(s)

        s_list[step], s_list[i] = s_list[i], s_list[step]  

        get_permutations(s_list, step + 1) 
 

