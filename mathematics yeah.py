nArr=[]
for i in range(1,3):
    nArr.append(int(input()))
  
for n in nArr:
    if n>=1 and n<=(10**9):
        prod = 1
        sum = 0
        for i in range(1, n+1):
            prod = prod*i
            sum = sum+i
        if prod%sum==0:
            print("YEAH")
            break
        else:
            print("NAH")
            break
