
#Example: For n = 8:
# *********
# *       *
# *       *
# *       *
# *       *
# *       *
# *       *
# *********

def solution(n):
    if n ==1:
        return ['*']
    result = []
    result.append('*' * n)
    for _ in range(n - 2):
        result.append('*' + ' '*(n-2) + '*')
    result.append('*' * n)
    return result
