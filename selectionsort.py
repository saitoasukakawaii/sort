#有点不标准的选择排序需要修改
def selection_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[i]>a[j+i+1]:
                a[i],a[j+i+1]=a[j+i+1],a[i]
        print('当前的数组是:'+str(a))
    print('排序后的数组是:'+str(a))
    
