def isisomorphio(sl,s2):
    if len(sl)!=len(s2):
        return false
    else:
        map1,map2=(),()
        for i in range (len(sl)):
            ch1,ch2=s1[i],s2[i]
            if ch1 not in map1:
                map1[ch1]=ch2
            if ch2 not in map2:
                map2[ch2]=ch1
            if map1[ch1]!=ch2 or map2[ch2]!=ch1:
                return False
    return True
s1=str(input("enter a string 1"))
s2=str(input("enter a string 2"))
print(isisomorphio(s1,s2))
