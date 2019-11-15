from itertools import combinations
s = "123456"
clist=list(combinations(s, 5))
print(f'组合数的个数为{len(clist)}。')
print('它们是:\n',clist)