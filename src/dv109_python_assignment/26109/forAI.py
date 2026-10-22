for i in range(1, 10):          # 外層迴圈控制被乘數 (1~9)
    for j in range(1, 10):      # 內層迴圈控制乘數 (1~9)
        print(f"{i}*{j}={i*j}", end="\t")  # 印出算式，用 \t 隔開
    print()                     # 每一列結束後換行