a=10
b=20
if a>b:
    print("a>b")
    print("區塊語法都會被執行")

    print("空一行後，相同縮排")
else:
    print("條件不成立")

if a < b:
    print("a < b 成立")
elif a == b:
    print("a == b 成立")
elif a > b:
    print("a > b 成立")
else:
    print("都不成立")