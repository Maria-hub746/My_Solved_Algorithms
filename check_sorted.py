def check_sorted(A:list, ascending=True):
    flag = True
    s = 2*int(ascending)-1
    for i in range(0, len(A)-1):
        if s*A[i] > s*A[i+1]:
            flag = False
            break
    return flag

test = [1, 2, 3, 4, 5, 6, 7]
check_sorted(test)