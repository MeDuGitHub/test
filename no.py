# coding :=utf-8

ia = 10
li = []
print("请输入10个数字！")
while ia:
    try:
        an = eval(input("请输入第{}个数字".format(ia)))
    except:
        print("请输入数字！")
        ia += 1
    ia -= 1
    if type(an) == int: li.append(an)
print(li)
