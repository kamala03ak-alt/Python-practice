def vowel(a):
    count=0
    for i in a:
        if i in 'aeiouAEIOU':
            count+=1
    return count
print(vowel(input()))