# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'c', 'e', 'a', 'c', 'b', 'b', 'c']
# # 计算出 每个单词出现过几次，使用字典写出
# char_count = {}
# for char in chars:
#     # if char in char_count:
#     #     char_count[char] += 1
#     # else:
#     #     char_count[char] = 1
#     if char not in char_count:
#         char_count[char] = chars.count(char)
#
# print(char_count)
#
# # 可以使用内置函数max取最大数
# v = char_count.values()
# max_char = max(v)
# print(max_char)
# # 最大数值的key值是多少
# for k, v in char_count.items():
#     if v == max_char:
#         print(k)
#
# persons = [
#     {'name': 'zhangsan', 'age': 18},
#     {'name': 'lisi', 'age': 20},
#     {'name': 'wangwu', 'age': 37},
#     {'name': 'jerry', 'age': 28},
# ]
# 让用户输入姓名，如果姓名已经存在，提示用户，如果姓名不存在，继续输入年龄，并存入列表里,显示‘添加成功’
# n = input('请输入姓名：')
# for person in persons:
#     if person['name'] == n:
#         print('姓名已经存在')
#         break
# else:
#     print('姓名不存在')
#     y = input('请输入年龄:')
#     new_person = {'name': n}
#     new_person['age'] = y
#     persons.append(new_person)
#     print(persons)
#     print('添加成功！')

# dict1 = {'a': 100, 'b': 200, 'c': 300}
# # 键值对 数据交换
# dict2 = {}
# for k, v in dict1.items():
#     dict2[v] = k
# dict1 = dict2
# print(dict1)
#
# # 字典推导式
# dict2 = {v: k for k, v in dict1.items()}
# print(dict2)

# 声明一个列表，在列表中保存6个学生的信息
students = [
    {'name': 'zhangsan', 'age': 18, 'score': 78, 'tel': '1334246728', 'gender': 'female'},
    {'name': 'lisi', 'age': 22, 'score': 53, 'tel': '1345565643', 'gender': 'male'},
    {'name': 'wangwu', 'age': 34, 'score': 98, 'tel': '1332265648', 'gender': 'male'},
    {'name': 'zheliu', 'age': 21, 'score': 98, 'tel': '1745562413', 'gender': 'unknown'},
    {'name': 'jack', 'age': 31, 'score': 88, 'tel': '1745562418', 'gender': 'male'},
    {'name': 'jerry', 'age': 10, 'score': 60, 'tel': '1305366413', 'gender': 'unknown'},
]
# （1）统计不及格学生的个数
# （2）打印不及格学生的姓名和对应的成绩
# （3）统计未成年学生的个数
# （4）打印手机尾号是8的学生的名字
# （5）打印最高分和对应的学生的名字
# （6）删除性别不明的所有学生
# （7）将列表按学生成绩从大到小排序
count = 0
minor = 0
max_score = students[0]['score']  # 假设第0个学生的成绩是最高分
# max_index = 0  # 假设最高分的学生下标为0
for i, student in enumerate(students):
    if student['score'] < 60:
        count += 1
        print('不及格的学生名字是：{}，成绩是：{}'.format(student['name'], student['score']))
    if student['age'] < 18:
        minor += 1

    # if student['tel'].endswith('8'):
    if student['tel'][-1] == '8':
        print('手机尾号是8的学生的名字:{}'.format(student['name']))
    if student['score'] > max_score:
        max_score = student['score']

print('不及格的学生个数:%d' % count)
print('未成年的学生个数:{}'.format(minor))
print('最高分是：%d' % max_score)
for student in students:
    if student['score'] == max_score:
        print('得到最高分的是：%s' % student['name'])
# （6）删除性别不明的所有学生
# 方法一：将不需要删除的数据添加到新列表
# new_students = [x for x in students if x['gender'] != 'unknown']
# print(new_students)
# 方法二：使用for循环倒着删除要删除的数据，避免“坑”
# x = 0
# for x in range(len(students) - 1, -1, -1):
#     if students[x]['gender'] == 'unknown':
#         students.remove(students[x])
#         print(students)
# 方法三，使用while循环删除需要删除的数据，并及时补齐因删除数据而导致的列表数据索引变化，避免漏删数据
# i = 0
# while i < len(students):
#     if students[i]['gender'] == 'unknown':
#         students.remove(students[i])
#         i -= 1
#     i += 1
# print(students)

# 方法四，遍历在新的列表操作，删除是在原来的列表操作（students[:]是studens的切片，所以修改students对切片无影响）
for student in students[::]:
    if student['gender'] == 'unknown':
        students.remove(student)
print(students)
print('----------')
# （7）将列表按学生成绩从大到小排序
for j in range(0, len(students) - 1):
    for i in range(0, len(students) - 1):
        if students[i]['score'] < students[i + 1]['score']:
            students[i], students[i + 1] = students[i + 1], students[i]
print(students)
