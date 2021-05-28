# lst = []
# def printDivisors(n):

#     for i in range(1,n+1):
#         if n%i == 0:
#             print(i,end=" ")
    
#     return

# n = int(input())
# printDivisors(n)


# lst = []
# def countBits(n):
#     while n!=0:
#         r = n%2
#         lst.append(r)
#         n = n//2
#     c = lst.count(1)
#     return lst
        




        
# n = int(input())
# print(countBits(n))


# a,b = input().split(' ')
# start = int(a)
# end = int(b)

# lst = []  
# for i in range(start, end+1):
#   if i>1:
#     for j in range(2,i):
#         if(i % j==0):
#             break
#     else:
#         lst.append(i)
# print(len(lst))
# lst = []
# a = int(input())
# b = [int(input().split(" ")) for i in range(0,a)]
# c = int(input('Search element: '))
# for i in b:
#     if i==c:
#         ind = b.index(i)
#         lst.append(ind)
# print(lst[0])
# lst = []
# length = int(input())
# arr = [int(i) for i in input().split()]
# t = int(input())
# for i in arr:
#     if i == t:
#         print(arr.index(i))
#         break
#     else:
#         print(-1)

#*********************************************Substring pattern*****************************
# lst = []
# def printSubstrings(string):
#     n = len(string)
#     for i in range(0,n):
#         for j in range(i,n):
#             lst.append(string[i:(j+1)])
#     print(lst)
#     return 
# string = input()
# printSubstrings(string)

#************************************Reverse string word wise*******************************
# a = input()
# lst = a.split(" ")
# lst.reverse()
# for i in lst:
#     print(i,end=' ')


# def reverseStringWordWise(string):
#     lst = string.split(" ")   
#     anslst = ' '.join(reversed(lst))
#     return anslst
# string = input()
# ans = reverseStringWordWise(string)
# print(ans)


#Remove consecutive duplicates
# def consec(string):
#     answ = string[0]
#     mover = string[0]
#     for i in string[1:]:
#         if i!=mover:
#             answ +=i
#             mover = i
#     return answ
# a = input()
# x = consec(a)
# print(x)


# ****************************************Remove occurence of other characters**************************
# string = input()
# c = input()

# s = string.replace(c,"")
# print(s)

# string = input()
# c = input()
# outout = ""
# for i in string:
#     if i !=c:
#         outout +=i
# print(outout)


# *************************************************Reverse each word in string###########################
s = input()
words = s.split(" ")
nwords = [i[::-1] for i in words]
for i in nwords:
    print(i,end=" ")






