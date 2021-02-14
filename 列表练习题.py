# 有一个列表names，保存了一组姓名names = ['zhangsan', 'lisi', 'chris', 'jerry', 'henry']
# 再让用户输入一个姓名，如果这个姓名在列表里存在，提示用户姓名已存在；
# 如果这个姓名在列表里不存在，就将这个姓名添加到列表里
# names = ['zhangsan', 'lisi', 'chris', 'jerry', 'henry']
# n = input('请输入一个名字：')
# if n in names:
#     print('用户名已存在')
# else:
#     names.append(n)
#     print(names)
# for name in names:
#     if n == name:
#         print('用户已存在')
# else:
#     names.append(n)
#     print(names)
# 冒泡排序的优化
# nums = [3, 1, 9, 8, 4, 2, 0, 7, 5]
# n = 0
# count = 0
# while n < len(nums) - 1:
#     i = 0
#     flag = True
#     while i < len(nums) - 1 - n:
#         count += 1
#         if nums[i] > nums[i+1]:
#             nums[i], nums[i+1] = nums[i+1], nums[i]
#             flag = False
#         i += 1
#     if flag:
#         break
#     n += 1
# print(nums)
# print(count)

# 求列表中最大的数值

# 第一种
# nums.sort()
# print(nums)
# print('最大值是{}'.format(nums[-1]))
# # 第二种
# nums.sort(reverse=True)
# print(nums)
# print('最大值是{}'.format(nums[0]))
# # 第三种  并得到他的下标
# a = nums[0]  # 假设a是列表中最大的值
# for num in nums:
#     if a < num:
#         a = num
# print('最大值是%d,他的下标是%d' % (a, nums.index(a)))
# # while语句得到下标的方法
# a = nums[0]
# i = 0
# index = 0
# while i < len(nums):
#     if nums[i] > a:
#         a = nums[i]
#         index = i
#     i += 1
# print('最大值是%d,他的下标是%d' % (a, index))

# 移除空字符串
# nums = ['zhangsan', '', '', 'wangwu', 'laotie', 'mengye', '']
# 方法一
# i = 0
# while i < len(nums):
#     if nums[i] == '':
#         nums.remove(nums[i])
#         i -= 1
#     i += 1
# print(nums)
# 方法二
# word = []
# for num in nums:
#     if num != '':
#         word.append(num)
# nums = word
# print(nums)
# 一个学校,有3个办公室，现在有10位老师等待工位的分配，请编写程序，完成随机的分配
import random

teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
rooms = [[], [], []]
for teacher in teachers:
    room = random.choice(rooms)
    room.append(teacher)
print(rooms)
# 第0个房间有3个人，分别是
# 带下标我们一般都使用while
# for循环也可以带下标
for i, room in enumerate(rooms):
    print('第{}个房间有{}个人，分别是：'.format(i, len(room)), end='')
    for teacher in room:
        print(teacher, end=' ')
    print()

# 列表推导式作用是使用简单的语法创建一个列表
# num = [i for i in range(0, 10) if i % 2 == 0]
# print(num)
# # points 是一个列表。这个列表里的元素都是元组
# points = [(x, y) for x in range(5, 10) for y in range(10, 20)]
# print(points)
# 请写出一段python代码实现分组一个list里面的元素，比如[1,2,3,~100]变成[1,2,3],[4,5,6]~]
# m = [i for i in range(1, 101)]
# print(m)
# n = [m[j:j + 3] for j in range(0, 100, 3)]
# print(n)
