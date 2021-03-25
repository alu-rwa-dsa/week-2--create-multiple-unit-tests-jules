  def linkedList(list):
    n = []
    for l in list:
        n.extend(l)
        r = set(n)
        l = list(r)

    return l


if __name__ == "__main__":
    a = [[2, 4, 9, 2, 1, 6], [9, 5, 22, 1, 0, 56, 8, 5]]

    print(linkedList(a))

# time complexity - O(N)
# space complexity - O(1)