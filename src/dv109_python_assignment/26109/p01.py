hours_per_day = 2
days = 2
total_hours= hours_per_day*days
A=10
a=2
mystr1="中文字1"
mystr2='中文字2'

mystr3='A=10'
mystr4="A=10"
mystr5="A={A}"
mystr6='A={A}'
mystr7=f"A={A}"
mystr8=f'A={A}'


#中文變數=120
print(total_hours)
#print(中文變數)
#盡量不要用到中文變數

"""多行註解
多行註解"""
if a>10:
    print(a>10)
    print("test")


print("新的一行")
print(mystr1)
print(mystr2)
print(mystr3)
print(mystr4)
print(mystr5)
print(mystr6)
print(mystr7)
print(mystr8)
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
study_hours = 2
study_hours == 2

c=100
d=100
print(c == d)
print(c is d)

name='小明'
hours=2
print(f"{name}每天學習{hours}小時")
mystr=f"{name}每天學習{hours}小時"
print(mystr)

mystr_B=f"{name}每天學習{hours+2}小時"
print(mystr_B)

print("abc", "123")
print("abc", "123", sep="@", end="")
print("abc", "123")

average=83.3966234643515657746455
print(f"平均分數:{average:.1f}")

age_text = input("請輸入年齡：")
age = int(age_text)
hours_text = input("每天學習幾小時：")
hours = float(hours_text)