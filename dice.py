import random
total = 0
for i in range(10):
    x = random.randint(1,6)
    print(str(i+1)+"回目："+str(x))
    total += x

average = total / 10
print("平均値:" + str(round(average, 2)))
# 期待される出力結果例
"""
1回目：1
2回目：1
3回目：3
4回目：6
5回目：4
6回目：3
7回目：4
8回目：1
9回目：2
10回目：3
平均値:2.8
"""
