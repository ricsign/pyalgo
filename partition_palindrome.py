original_string = 'abacdccdaa'
count = 0
total_list = []


def is_palindrome(s):
    low = 0
    high = len(s)-1
    while high >= low:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True


def partition_palindrome(string,start,current_list):
    global count
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            pass
