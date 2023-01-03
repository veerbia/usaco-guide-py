# Creating Strings I
s = input()
perms = []
char_count = [0] * 26

def search(curr):
    if len(curr) == len(s):
        perms.append(curr)
    else:
        for i in range(26):
            if char_count[i] > 0:
                char_count[i] -= 1
                search(curr + chr(ord('a') + i))
                char_count[i] += 1

for c in s:
    char_count[ord(c) - ord('a')] += 1

search("")
print(len(perms))
for p in perms:
    print(p)

# Time Complexity: O(n!)
# Space Complexity: O(n!)
