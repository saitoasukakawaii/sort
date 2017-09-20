def insertion_sort(a):
    n=len(a)
    for j in range(1,n):
        key=a[j]
        i=j-1
        while i>=0 and a[i]>key:
            a[i+1]=a[i]
            i-=1
        a[i+1]=key
        print('当前的数组是:'+str(a))
    print('排序后的数组是:'+str(a))
        
