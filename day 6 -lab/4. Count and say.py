def countAndSay(n):
    if n == 1:
        return "1"
    
    prev_term = countAndSay(n - 1)
    result = ""
    count = 1
    
    for i in range(len(prev_term)):
        if i + 1 < len(prev_term) and prev_term[i] == prev_term[i + 1]:
            count += 1
        else:
            result += str(count) + prev_term[i]
            count = 1
    
    return result

n = 1
print(countAndSay(n))
