def longestSubstring(s, k) :
 
    # Store the required answer
    ans = 0
 
    # Create a frequency map of the
    # characters of the string
    freq = [0]*26
 
    # Store the length of the string
    n = len(s)
 
    # Traverse the string, s
    for i in range(n) :
 
        # Increment the frequency of
        # the current character by 1
        freq[ord(s[i]) - ord('a')] += 1
    unique = 0
    for i in range(26) :
        if (freq[i] != 0) :
            unique += 1
    for curr_unique in range(1, unique + 1) :

        Freq = [0]*26

        start, end = 0, 0

        cnt, count_k = 0, 0
 
        while (end < n) :
            if (cnt <= curr_unique) :
                ind = ord(s[end]) - ord('a')
 
                if (Freq[ind] == 0) :
                    cnt += 1
 
                Freq[ind] += 1

                if (Freq[ind] == k) :
                    count_k += 1
 
                end += 1
             
            else :
                ind = ord(s[start]) - ord('a')
 
                if (Freq[ind] == k) :
                    count_k -= 1
 
                Freq[ind] -= 1

                if (Freq[ind] == 0) :
                    cnt -= 1

                start += 1
 
            if ((cnt == curr_unique) and (count_k == curr_unique)) :
 
                ans = max(ans, end - start)
    print(ans)
S = "ababbc"
K = 2
longestSubstring(S, K)
