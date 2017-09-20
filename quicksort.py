import random
def quick_sort(lists, p, r):
    if p-r >= -1:
        return lists
    q = partition(lists, p, r)
    quick_sort(lists, p, q-1)
    quick_sort(lists, q+1, r)
    return lists

def partition(lists, p, r):
    n = r-p
    x = lists[r]
    i = p-1
    for j in range(p,r):
        if lists[j] <= x:
            i += 1
            lists[i],lists[j] = lists[j],lists[i]
    lists[i+1],lists[r] = lists[r],lists[i+1]
    return i+1

if __name__ == '__main__':
    a = [1,6,2,4,8,5,9,7,3]
    n = len(a)-1
    quick_sort(a,0,n)
    print(a)
    
def randomized_quick_sort(lists, p, r):
    if p-r >= -1:
        return lists
    q = randomized_partition(lists, p, r)
    randomized_quick_sort(lists, p, q-1)
    randomized_quick_sort(lists, q+1, r)
    return lists

def randomized_partition(lists, p, r):
    i =random.randint(p, r)
    lists[r],lists[i] = lists[i],lists[r]
    return partition(lists, p, r)
