def solution(a, b):
    answer = 0
    max = a if a >= b else b
    min = b if a >= b else a
    while min <= max :
        answer += min
        min += 1
    return answer
