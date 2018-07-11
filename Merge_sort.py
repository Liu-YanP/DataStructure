#并归排序
def merge_sort(alist):
    n = len(alist)
    if n<=1:
        return alist

    #二分分解
    num = int(n/2)
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])
    #合并
    return merge(left,right)

def merge(left,right):
    '''合并操作，将两个有序数组left[]和left[]合并成一个大的有序数组'''
    #left与right的下标指针
    l, r = 0, 0
    result = []
    while l<len(left) and r < len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r+=1
    result +=left[l:]
    result +=right[r:]
    return result


#测试
if __name__ == '__main__':
    alist = [25,2,12,14,54,41,15,23,45,21,4]
    print(merge_sort(alist))
