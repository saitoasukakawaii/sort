def binary_search(A,v,p,q):
#升序排列
    if p == (p+q)//2 and A[p] == v:
        return print('所查找的数位于第%d位'%p)
    elif p == (p+q)//2 and A[p] != v:
        return print('不存在该元素')
    elif A[(p+q)//2] >= v:
        q = (p+q)//2
        binary_search(A,v,p,q)
    elif A[(p+q)//2] < v:
        p = (p+q)//2+1
        binary_search(A,v,p,q)
