
"""

九九乘法表
1x1=1
1x2=2
...
9x1=9
...
9x9=81
用for迴圈
"""

for i in range(9):
    #print(i+1)
    #print(f" 1 (1+1)= {1*(1+1)}")
    for j in range(1):
        print(f"{i+1}*{j+1}={(i+1)*(j+1)}",end=" ")
        print(f"{i+2}*{j+1}={(i+2)*(j+1)}",end=" ")
        print(f"{i+3}*{j+1}={(i+3)*(j+1)}")
    print()
  


   