"""
Intuition:
The code identifies and prints duplicate characters in a given string along with their counts. It first converts the string to a sorted list of characters. 
Then, it iterates through the list, using a nested loop to count consecutive duplicate characters. If a character appears more than once, it adds the character 
to a set and prints the character with its count. This ensures each duplicate character is processed and printed only once.
"""

def print_duplicates(s):
    l = list(s)
    l.sort()
    s = set()
    for i in range(len(l)):
        if l[i] not in s:
            c = 1
            j = i
            while j < len(l) - 1 and l[j] == l[j+1]:
                c += 1
                j += 1
            if c > 1:
                s.add(l[i])
            if c > 1:
                print(l[i],'->',c)

print_duplicates("test string")
