import random
start = input('請輸入起始數值')
end = input('請輸入結束數值')
start = int(start)
end = int(end)
r = random.randint(start , end)
count = 0
while True:
    count+=1
    num = input('請猜一個數字:')
    num = int(num)
    if num == r:
        print('你猜中了')
        print('這是你猜的第', count , '次')
        break
    elif num < r:
        print('你猜的數字太小了')
    elif num > r:
        print('你猜的數字太大了')
    print('這是你猜的第', count , '次')