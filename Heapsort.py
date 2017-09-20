#包含节点函数，生成最大堆函数max_heapify,建堆函数built_max_heap,
#堆排序函数heap_sort
#优先级队列函数有
#heap_insert(S,x)：把元素x插入集合S。这一操作可写为S←S∪{x}。
#heap_maximum(S)：返回S中具有最大关键字的元素。
#heap_extract_max(S)：去掉并返回S中的具有最大关键字的元素。
#heap_increase_key(S,x,k)：将元素x的关键字的值增加到k，这里k值不能小于x的原关键字的值

#父节点与子节点的计算
def parent(i):
    return (i-1)//2
def left(i):
    return 2*i+1
def right(i):
    return 2*(i+1)

#生成最大堆
def max_heapify(lists, i, heap_size):
    largest = i
    l = left(i)
    r = right(i)
    if l >= heap_size:
        return lists
    if l < heap_size and lists[l] > lists[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and lists[r] > lists[largest]:
        largest = r
    if largest != i:
        lists[i],lists[largest] = lists[largest],lists[i]
        return max_heapify(lists, largest, heap_size)

#建堆    
def built_max_heap(lists):
    heap_size = len(lists)
    for i in range(heap_size//2-1, -1, -1):
        max_heapify(lists, i, heap_size)

#堆排序
def heap_sort(lists):
    built_max_heap(lists)
    heap_size = len(lists)
    for i in range(len(lists)-1, 0, -1):
        lists[i],lists[0] = lists[0],lists[i]
        heap_size -= 1
        max_heapify(lists, 0, heap_size)

if __name__ != '__main':
    a=[1, 6, 4, 8, 2, 9, 3, 7, 5]
    heap_sort(a)
    print(a)

def heap_insert(lists, key):
    lists.append(float('inf'))
    heap_size = len(lists)
    heap_increase_key(lists, heap_size, key)

def heap_maximum(lists):
    return lists[0]

def heap_extract_max(lists):
    heap_size =len(lists)
    if heap_size < 1:
        return 'heap underflow'
    max = lists[0]
    lists[0],lists[heap_size-1] = lists[heap_size-1],lists[0]
    lists.pop()
    heap_size -= 1
    max_heapify(lists, 0 ,heap_size)
    return max

def heap_increase_key(lists, i, key):
    if key < lists[i]:
        return 'new key in smaller than current key.'
    lists[i] = key
    while i > 0 and lists[parent(i)] < lists[i]:
        lists[i],lists[parent(i)] = lists[parent(i)],lists[i]
        i = parent(i)
        
