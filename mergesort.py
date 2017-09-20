
def merge(left,right):
    result = []
    r,l = 0,0
    while r<len(left) and l<len(right):
        if left[r] < right[l]:
            result.append(left[r])
            r += 1
        else:
            result.append(right[l])
            l += 1
    result += left[r:]
    result += right[l:]
    return result
    
def merge_sort(lists):
    if len(lists) <= 1 :
        return lists
    else:
        num = len(lists)//2
        left = merge_sort(lists[:num])
        right = merge_sort(lists[num:])
        return merge(left,right)
