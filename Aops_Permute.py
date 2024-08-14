def permute(inputList):
    '''permute(inputList) -> list
    returns list of all permutations of inputList'''

    if len(inputList) == 0:
        return [[]]

    if len(inputList) == 1:
        return [inputList]




    outputList = []

    for num in range(len(inputList)):
        subList = inputList[:]
        special_num = subList.pop(num)

        subPerm = permute(subList)

        for perm in subPerm:
            outputList.append([special_num] + perm)

    return outputList

    
        
            




    

# test cases
print(permute([1]))
print(permute([1,2]))
# should print [[1,2], [2,1]] in some order
print(permute([1,2,3]))
# should print [[1,2,3], [1,3,2], [2,1,3], [3,1,2], [2,3,1], [3,2,1]] in some order
