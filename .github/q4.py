
lA = [20, 5, 2, 9, 3]#list one

lB = [20, 2, 9, 3]#list two


def CLists(lsA, lsB):
    for number in lsA:  
        if number not in lsB: 
            return number


if __name__ == "__main__":
    print(CLists(lA, lB))

# Space Complexity - O(1)
# Time Complexity - O(A * B)
