def Calculate(number):
    list = []
    var = number
    occurence = 1

    while var != 0: 
        addList = number - (var - 1)
        list.append(addList)
        if occurence == addList:
            var = var - 1  
            occurence = 1
        else:
            occurence = occurence + 1  
        
    return list


print(Calculate(6))
# Space Complexity - O(1)
# Time Complexity - O(nlogn)
