"""
    2048核心算法
"""

def zero_to_end(list01):
    """
    将列表按照需要的格式排序，将，如：
    [2,0,2,0] --> [2,2,0,0]
    :param list01:
    :return:
    """
    new_list = [item for item in list01 if item != 0]
    new_list += [0] * list01.count(0)
    list01[:] = new_list[:]

def merge(list_target):
    """
    [2,2,0,0] -- >  [4,0,0,0]
    :param list_target:
    :return:
    """
    zero_to_end(list_target)
    for i in range(len(list_target)-1):
        if list_target[i] == list_target[i+1]:
            list_target[i] += list_target[i+1]
            list_target[i+1] = 0
    zero_to_end(list_target)


def print_map(map):
    """
    打印列表
    :param map:
    :return:
    """
    for r in range(len(map)):  # 0 1 2 3 4 5
        for c in range(len(map[r])):  # 0 1 2 3 4 5
            print(map[r][c],end=" ")  # [0][0] [0][1] [0][2]
        print()


def move_left(map):
    """
    列表向左移动
    :param move:
    :return:
    """
    for item in range(len(map)):
        merge(map[item])

def move_right(map):
    """
    列表向右移动
    :param move:
    :return:
    """
    for item in range(len(map)):
        list_merge = map[item][::1]
        merge(list_merge)
        map[item][::-1] = list_merge

def move_up(map):
    """
    列表向上移动
    :param map:
    :return:
    """
    tmp_list = []
    for r in range(len(map)):  # 0
        list02 = []
        for c in range(len(map)):  # 0 1 2 3
            list02.append(map[c][r])
        tmp_list.append(list02)
    for item in range(len(tmp_list)):
        list_merge = tmp_list[item][::1]
        merge(list_merge)
        tmp_list[item] = list_merge
    sum(tmp_list)
    map[:] = tmp_list


def sum(tmp_list):
    list06 = []
    for r in range(len(tmp_list)):  # 0
        list07 = []
        for c in range(len(tmp_list)):  # 0 1 2 3
            list07.append(tmp_list[c][r])  # 0 0 , 1 0
        list06.append(list07)
    tmp_list[:] = list06

list01 = [
    [2,0,0,2],
    [2,2,0,0],
    [2,0,4,4],
    [4,0,0,2],
]

move_up(list01)
print_map(list01)
# print(list01)
#
# tmp_list = []
# count = 0
# for r in range(len(list01)):  # 0
#     list02 = []
#     for c in range(len(list01)):  # 0 1 2 3
#         if r == count:
#             list02.append(list01[c][count])
#     tmp_list.append(list02)
#     count += 1
# print(tmp_list)
#
# for item in tmp_list:
#     merge(item)
#
# print(tmp_list,end="")
# print()
#
# list05 = []
# for item in tmp_list:
#     print(item)
# # 0   1  2  3
# # [4, 2, 4, 0] 0 1 2 3
# # [2, 0, 0, 0]
# # [4, 0, 0, 0]
# # [2, 4, 2, 0]
# # 0 0 , 1 0 , 2 0 , 3 0
# # 0 1 , 1 1 , 2 1 , 3 1
# list06 = []
#
# for r in range(len(tmp_list)):  # 0
#     list07 = []
#     for c in range(len(tmp_list)): # 0 1 2 3
#         list07.append(tmp_list[c][r])  # 0 0 , 1 0
#     list06.append(list07)
#
# print()
#
# for item in list06:
#     print(item)
# tmp_list.append([123])
# tmp_list[-1].append(456)
# print(tmp_list[-1])

