import time

def bruteforceStringMatcher(text : str , pattern : str):
    start_time = time.time()
    count = 0
    result = []
    for i in range(len(text)):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            if j == len(pattern)-1:
                count+=1
                result.append(i)
        if (i+len(pattern) >= len(text)):
            break

    return result,count,time.time()-start_time

def compute_lps(pattern):
    """
    Compute the Longest Prefix Suffix (LPS) array for the pattern.
    The LPS array is used to skip characters while matching.
    """
    length = 0  # length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    Perform KMP search of the pattern in the given text.
    """
    start_time = time.time()
    m = len(pattern)
    n = len(text)
    
    # Preprocess the pattern to get the LPS array
    lps = compute_lps(pattern)

    i = 0  # index for text
    j = 0  # index for pattern
    count = 0
    result = []

    while i <= n-m:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            result.append(i - j)
            count += 1
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result,count,time.time()-start_time


def lastOccurenceMap(text : str):
    LOM = {}
    for i in range (len(text)):
        LOM[text[i]] = i

    return LOM

def boyerMoore(text :str , pattern : str):
    start_time = time.time()
    m = len(pattern)
    n = len(text)
    count = 0
    last_occurrence = lastOccurenceMap(pattern)
    s = 0  # s is the shift of the pattern with respect to the text
    result = []

    while s <= n - m:
        j = m - 1

        # Keep reducing index j of pattern while characters of pattern and text are matching
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        # If the pattern is present at the current shift, then index j will become -1 after the loop
        if j < 0:
            # result.append(s)
            count +=1
            if (s+m >= len(text)):
                break
            elif (text[s + m]) not in last_occurrence:
                s += 1
            else:
                s += (m-last_occurrence[(text[s + m])] if s + m < n else 1)
        else:
            if (s+j >= len(text)):break
            if (text[s + j]) not in last_occurrence:
                s += 1
            else:
                s += max(1, j - last_occurrence[(text[s + j])])

    return result,count,time.time()-start_time

# Example usage
# print("flag")
# text = "ABABDABACDABABCABAB"
# pattern = "ABABCABAB"
# matches1,count1,time1 = bruteforceStringMatcher(text,pattern)
# matches2,count2,time2 = kmp_search(text, pattern)
# matches3,count3,time3 = boyerMoore(text,pattern)

# print(f"Brute Force : {matches1} found {count1} runtime : {time1}",)
# print(f"KMP : {matches2} found {count2} runtime : {time2}")
# print(f"Boyer-Moore : {matches3} found {count3} runtime : {time3}")