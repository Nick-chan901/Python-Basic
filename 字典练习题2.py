# 用三个元组表示三门学科的选课学生姓名(一个学生可以同时选多门课)
sing = ('李白', '白居易', '李清照', '杜甫', '王昌龄', '王维', '孟浩然', '王安石')
dance = ('李商隐', '杜甫', '李白', '白居易', '岑参', '王昌龄')
rap = ('李清照', '刘禹锡', '岑参', '王昌龄', '苏轼', '王维', '李白')
# (1) 求选课学生总共有多少人
# (2) 求只选了第一个学科的人的数量和对应的名字
# (3) 求只选了一门学科的学生的数量和对应的名字
# (4) 求只选了两门学科的学生的数量和对应的名字
# (5) 求只选了三门学生的学生的数量和对应的名字

total = set(sing + dance + rap)  # set集合可以去重
print('选课学生总共有%s' % len(total))
# 第一题的思路：创建一个空列表，然后将只选第一科目的放进去
new_peson = []
for name in sing:  # 遍历第一学科中的所有人名
    # print(name)
    if name not in dance and name not in rap:  # not in 判断,将不是第一学科的内容排除掉
        new_peson.append(name)  # append 将筛选后的内容加入到空列表中
print('只选了第一个学科的人共有:{}个,他们分别是：{}'.format(len(new_peson), new_peson))  # 使用len语句 将新列表的字长，也就是个数输出

# 第二~五题的思路：创建一个字典，将所有的数据进行计数，统计出每个名字出现的次数后，再通过遍历、判断语句，根据出现次数，进行输出
new_dict = {}  # 创建空字典
the_all = sing + dance + rap
for n in the_all:  # 遍历所有数据
    if n not in new_dict:  # 判断 n 不在新字典里吗？
        new_dict[n] = the_all.count(n)  # 因为字典中的同名数据会被叠加，所以直接将计数数值给到 new_dict[n]中
print(new_dict)
count = 0
a = 0
b = 0
al = []
bl = []
cl = []
# 分别将出现的选择3门、2门、1门的次数，以及存放三种数据的列表 进行定义
for k, v in new_dict.items():  # 对字典中的数据 进行键值对遍历
    if v == 3:
        count += 1
        al.append(k)

    elif v == 2:
        a += 1
        bl.append(k)
    elif v == 1:
        b += 1
        cl.append(k)

print('选了三门学生一共是:{}人,分别是：{}'.format(count, al))
print('选了二门学生一共是:{}人,分别是：{}'.format(a, bl))
print('选了一门学生一共是:{}人,分别是：{}'.format(b, cl))
