# 請使用者輸入身高(cm)與體重(kg)，計算並印出 BMI 值與體位判斷

#這是在github上編輯的內容

#嘿這是本地庫咚咚

height = int(input("请输入您的身高(cm)："))
weight = int(input("请输入您的体重(kg)："))

height = height / 100
print(f'your height is {height}')
print(f'your weight is {weight}')
bmi = weight / (height * height)
print(f'your bmi is {bmi:.2f}')
if bmi < 18.5:
    print('體位判斷:體重過輕')
elif bmi < 22.9:
    print('體位判斷:健康體位')
elif bmi < 27.5:
    print('體位判斷:體重過重')
else:
    print('體位判斷:肥胖')
