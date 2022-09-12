def stair(n):
    if n <= 1:
        return n
    else:
        return stair(n-1)+ stair(n-2)
s=int(input("n="))
print(stair(s+1))
