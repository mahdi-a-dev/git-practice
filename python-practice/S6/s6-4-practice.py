#1
def sum_list(l):
    if len(l) == 0:
        return 0

    return l[0] + sum_list(l[1:])
    
    
#2
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

#3
def reverse_str(s):
    if len(s) == 0:
        return ""
    
    return reverse_str(s[1:] + s[0])

#4
def count_element(l, elemet):
    if len(l) == 0:
        return 0
    if l[0] == elemet:
        return 1 + count_element(l[1:], elemet)
    else:
        return count_element(l[1:], elemet)
    

#5
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

#6
def digit(num):
    if num == 0:
        return 0
    return 1 + digit(num // 10)

