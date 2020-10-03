pw = '123'
x = 2
while True:
    password = input('請輸入您的密碼:')
    if password == pw:
        print('登入成功')
        break
    else:
        print('密碼輸入錯誤! 還有', x ,'次機會')
        x = x - 1
        if x < 0:
            print('登入三次錯誤，很糟糕呢!')
            break