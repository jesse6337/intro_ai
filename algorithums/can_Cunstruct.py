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