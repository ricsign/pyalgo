"""
 @desc:
 @author: Richard
 @contact: 1955283190@gmail.com
 @site: www.Richard.com
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49
 """
'''
a = int(input())
li = []
min = 9999999999999
li.append([a])
for i in range(a):
    b = input().split()
    li.append(b)

def minimum(a,b):
    return a if a>= b else b

def valid_page(li,cur=1):
    if cur >= len(li) :return False
    if li[cur][0] == 0: return True
    for i in range(len(li)-1):
        return valid_page(li,cur+1)

def shortest_path(li,mini,cur,local_val=0):
    if li[cur][0] == 0:
        mini = minimum(mini,local_val)
        local_val = 0
        return mini
    else:
        for i in range(len(li[cur][1:])):
            shortest_path(li, mini, cur + 1, local_val + 1)


if valid_page(li):
    print('Y')
    print(shortest_path(li, min, 1))
else:
    print('N')
'''
# def longeest_p_substring(s):
#     if s is None or len(s) == 1: return s
#     if len(s) == 2: return s[0]
#     mid_len = len(s) // 2
#     max_sub = 0
#     i = 0
#     local_max = 0
#     while True:
#         if mid_len-i <= 0 or mid_len+i >= len(s): return max(max_sub,local_max)
#         if s[mid_len-i] != s[mid_len+i]:
#             max_sub = max(local_max,max_sub)
#             i = 0
#             local_max = 0
#             break
#         else:
#             i += 1
#             local_max += 1
#
#     return max_sub

# 2014
# number = int(input())
# assigning_sheet_one = input().split()
# assigning_sheet_two = input().split()
# dictionary = {}
# for _ in range(number):
#     a = assigning_sheet_one.pop()
#     b = assigning_sheet_two.pop()
#     dictionary[a] = b
#
# for i in dictionary.keys():
#     if i == dictionary[i] or i != dictionary[dictionary[i]]:
#         print('bad')
# print('good')


#2018
# number_of_pages = int(input())
# whole_book = [input().split() for _ in range(number_of_pages)]
# shortest_length = float('inf')
# all_pages_can_be_reached = 'N'
# pages_can_be_reached = 1
# hash_table = [1]+[0 for _ in range(number_of_pages-1)]


# def justify(current_page,temp_shortest):
#     global number_of_pages,pages_can_be_reached,shortest_length,all_pages_can_be_reached
#     if pages_can_be_reached == number_of_pages:
#         all_pages_can_be_reached = 'Y'
#     if len(current_page) == 1:
#         shortest_length = min(shortest_length,temp_shortest)
#         temp_shortest = 0
#         return
#     for next_page in current_page[1:]:
#         pages_can_be_reached += 1
#         temp_shortest += 1
#         if hash_table[int(next_page)-1] == 0:
#             hash_table[int(next_page) - 1] = 1
#             justify(whole_book[int(next_page)-1],temp_shortest)
#         temp_shortest -= 1
#         hash_table[int(next_page) - 1] = 0
#
#
#
# justify(whole_book[0],0)
# print(all_pages_can_be_reached)
# print(shortest_length+1)


#2015
import time
count = 0
dic = []
initial_time = time.time()
def pi_day(slot_left,value_left,prev,lis):
    global count
    if slot_left == 0:
        count += 1
        #print(lis)
        return
    max_value = value_left // slot_left
    min_value = prev if slot_left > 1 else max_value
    for i in range(min_value,max_value+1):
        value_left -= i
        slot_left -= 1
        lis.append(i)
        pi_day(slot_left,value_left,i,lis)
        lis.pop()
        value_left += i
        slot_left += 1

pi_day(2,8,1,[])
print(count)
final_time = time.time()
print(final_time-initial_time)
















