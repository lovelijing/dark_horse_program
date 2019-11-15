from itertools import permutations
s = "1234"
plist=list(permutations(s, 3))
print(f'排列数的个数为{len(plist)}。')
print('它们是:\n',plist)