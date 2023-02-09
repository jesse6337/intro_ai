def countConstruct(target, wordBank): # count num of possible combinations
    if target == '':
        return 1
    returnList = 0
    for i in range(len(wordBank)):
        if target.startswith(wordBank[i]):
            part = target.replace(wordBank[i], '', len(wordBank[i]))
            inner = countConstruct(part, wordBank)
            returnList += inner
        
    return returnList

print(countConstruct('enterapotentpot', ['a','p','ent','enter','ot','o','t']))