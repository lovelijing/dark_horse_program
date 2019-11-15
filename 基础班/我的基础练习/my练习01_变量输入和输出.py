#一、变量
#1、计算利润
print('\n\n1、计算利润')
print('-'*20)
revenue=98456
costs=45000
profit=revenue-costs
print(profit)



#2、折扣价格
print("\n\n2、折扣价格")
print('-'*20)
price=19.95
discountPercent=30
markdown=price*discountPercent/100
price=price-markdown
print(price)



#二、字符串
print('\n\n3、字符串')
print('-'*20)
print('1、'+'abcdefg'+'hijklmn'+'字符串连接')
print('2、'+'Hello Python!'.upper())
print('3、'+'HEllO Python!'.lower())
print('4、'+str('hhopwque'.count('h')))
print('5、'+'wdDSCVDFVDFrtVERVERFVg'.capitalize())
print('6、'+'good and best'.title())
print('7、'+'dfvdgvdf    '.rstrip())
print('8、'+'abcdefghijklmnopq'[2:8])
print('9、'+'abcdefghijklmnopq'[3:])
print('10、'+'abcdefghijklmnopq'[:8:2])
print('11、'+'abcdefghijklmnopq'[::-1])
print('12、'+'abcdefghijklmnopq'[-5:-1])
print('13、'+'abcdefghijklmnopq'[-2:-10:-1])
print('14、'+str(len('Hello world!')))
print(r'15、root\etc\bin\public\0\0.5')
strlist=dir(str)
print('字符串的所有方法：')
for i in range(len(strlist)):
    print(strlist[i]+',',end='')
    if i%8==0 :
        print()



#三、int float eval和str函数
print('\n\n4、int float eval和str函数')
print('-'*20)
print(int('235'))
print(float('123.69'))
print(eval('23.5')+eval('78.9'))
print(str(12356)+'890pfghjknlnlkj')


#四、print和format
print('\n\n5、print和format')
print('-'*20)
print('{0:10d}'.format(12345678))
print('{0:10,d}'.format(12345678))
print('{0:10.2f}'.format(12345.678))
print('{0:10,.2f}'.format(123.45678))
print('{0:10,.3f}'.format(123.45678))
print('{0:10.2%}'.format(12.345678))
print('{0:10,.3%}'.format(12.345678))
print('{0:s} are {1:d} old'.format('You',25))
print('十六进制{0:0x}'.format(58798512456))
print('八进制{0:0o}'.format(1234567891879999))
print('二进制{0:0b}'.format(12345678))





#五、input函数
print('\n\n6、input函数')
print('-'*20)
town=input('Enter the name of your city:   ')
print('Your city name is  '+
      town)

