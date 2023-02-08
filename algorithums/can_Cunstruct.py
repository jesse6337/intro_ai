<<<<<<< HEAD
def can_construct(target, wordBank, memo = {}):
    if target == '':
        return True
    if target in memo:
        return False
    for i in range(len(wordBank)):
        if target.startswith(wordBank[i]):
            part = target.replace(wordBank[i],"", len(wordBank[i]))
            memo[part] = can_construct(part,wordBank)
            if memo[part] == True:return True
        
    return False
print(can_construct('hi', ['h','i']))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrf", ['e', 'ee','eee','eeee','eeeee']))
=======
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
>>>>>>> 25d7757bd88f6b60b6bd294bbf1cc8a872ca43fa
