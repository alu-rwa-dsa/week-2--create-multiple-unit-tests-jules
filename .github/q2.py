
def SDict(str):
    List = []
    List[:0] = str
    
    d = {}
    for char in List:  
        if char in d:
            d[char] = d[char] + 1
        else:
            d[char] = 1  
    
    return d


if __name__ == "__main__":
    print(SDict("Hello"))

# Time Complexity - O(nlogn)
# Space Complexity - O(n)