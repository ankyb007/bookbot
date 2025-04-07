def num_of_words(content):
    num_words=0
    for i in content.split():
        num_words+=1
    return num_words

def num_of_chars(content):
    counted={}
    for i in content.lower():
        if i not in counted:
            counted[i]=1
        else:
            counted[i]+=1
    return counted

def sort_on(dict):
    return dict["num"]

def sorted_dict(counted):
    lst=[]
    for i in counted:
        exmp={}
        if i.isalpha():
            exmp["name"]=i
            exmp["num"]=counted[i]
            lst.append(exmp)

    lst.sort(reverse=True, key=sort_on)
    return(lst)
   


