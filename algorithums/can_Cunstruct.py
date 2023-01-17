def can_construct(target, wordBank):
    if target == []:
        return True
    for i in range(len(wordBank)):
        #check might not work
        if target.startswith(wordBank[i]):
            try:
                part = target.replace(wordBank[i],"")
                can_construct(part,wordBank)
            except:
               print("ERROR")
               return True
        if target.endswith(wordBank[i]):
            try:
                part = target.replace(wordBank[i],"")
                can_construct(part,wordBank)
            except:
               print("ERROR")
               return True
    return False
print(can_construct("enterapotentpot", ['a','p','ent', 'enter', 'ot', 'o', 't']))