def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
        print('当前的数组是:'+str(a))
    print('排序后的数组:'+str(a))



            
