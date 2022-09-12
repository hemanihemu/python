def valid_number(str):
    i = 0
    j = len(str) - 1
 
   
    while i<len(str) and str[i] == ' ':
        i += 1
    while j >= 0 and str[j] == ' ':
        j -= 1
 
    if i > j:
        return False
 
    if (i == j and not(str[i] >= '0' and
                       str[i] <= '9')):
        return False
 
    
    if (str[i] != '.' and str[i] != '+' and
        str[i] != '-' and not(str[i] >= '0' and
        str[i] <= '9')):
        return False
 
    
    flagDotOrE = False
 
    for i in range(j + 1):
         
        
        if (str[i] != 'e' and str[i] != '.' and
            str[i] != '+' and str[i] != '-' and not
           (str[i] >= '0' and str[i] <= '9')):
            return False
 
        if str[i] == '.':
           
            if flagDotOrE:…
