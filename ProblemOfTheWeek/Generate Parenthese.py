"""
 @desc:
 @author: Richard
 @contact: qq1955283190@gmail.com
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49
 """

n = int(input("What is the value of n?"))
res = []


def generate(left,right,temp):
    if left == right == 0: # Qualified
        res.append(temp)
        return
    if left < 0 or right < 0 or left > right: # Backtrack
        return
    if left > 0:
        generate(left-1,right,temp+"(")
    if right > left:
        generate(left,right-1,temp+")")

generate(n,n,'')
print(res)
# [ "((()))", "(()())", "(())()", "()(())",  "()()()"]
# ['((()))', '(()())', '(())()', '()(())', '()()()']
