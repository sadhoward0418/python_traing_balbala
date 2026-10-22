#無窮迴圈
#while True:
    #print("1")

# count = 0 
# while count <5:
#     print(f"count<5, {count}")
#     count=count+1

"""
設計一個系統選單
1.呼叫客服
2.文字聯繫
3.留下資料
4.離開系統
"""

while True:
    print("======客服系統======")
    print("1.呼叫客服")
    print("2.文字聯繫")
    print("3.留下資料")
    print("4.離開系統")
    print("===================")
    choice = input("輸入1~4選擇功能或按q離開: ")

    if choice == "1":
        print("請稍等")
    elif choice == "2":
        print("請輸入訊息")
    elif choice =="3":
        print("請留下您的聯絡資料與需求")
    elif choice=="4":
        print("感謝您的使用，系統已關閉。再見！")


