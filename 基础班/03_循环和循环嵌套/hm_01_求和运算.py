print("\n\n求输入两数间的整数和及奇数和与偶数和\n\n")
print("请输入求和范围，必需是整数：")
intmix=int(input("最小值："))
intmax=int(input("最大值："))
i=intmix
sum=0
oushusum=0
jishusum=0
while i<=intmax:
    if i%2==0:
        oushusum=oushusum+i
    else:
        jishusum=jishusum+i
    sum=sum+i
    i=i+1

print("从{}到{}，的和为{}".format(intmix,intmax,sum))
print("从{}到{}，的偶数和为{}".format(intmix,intmax,oushusum))
print("从{}到{}，的奇数和为{}".format(intmix,intmax,jishusum))
