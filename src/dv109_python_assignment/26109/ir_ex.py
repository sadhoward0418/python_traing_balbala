"""
if練習

1.設計一個程式，鳩收使用者輸入的考試分數(0-100分)
2.每10分為一個級距，A級98分以上(包含89)，B級為80以上，類推至E級
3.不滿E級就輸出不及格
4.使用IF完成

"""

#接受使用者輸入
score=input("請輸入你的分數，0~100")
if int(score)>=0 and int(score)<=100:
    print("輸入的分數格是正確，進行轉換...")
    intScore=int(score)
    if intScore >= 90 and intScore <= 100:
        print("A級")
    elif intScore >= 80 and intScore < 90:
        print("B級")
    elif intScore >= 70 and intScore < 80:  
        print("C級")
    elif intScore >= 60 and intScore < 70:  
        print("D級")
    elif intScore >= 50 and intScore < 60:  
        print("E級")
    else:
        print("不及格或其他級別") 
    
else:
    print("輸入的數字不符合，程式將結束")
