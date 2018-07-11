#二分法查找
'''
二分查找又称折半查找，优点是比较次数少，查找速度快，平均性能好；其缺点是要求待查表为
有序表，且插入删除困难。因此，折半查找方法适用于不经常变动而查找频繁的有序列表。首先，
假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，如果两者相等，则
查找成功；否则利用中间位置记录将表分成前、后两个子表，如果中间位置记录的关键字大于查
找关键字，则进一步查找前一子表，否则进一步查找后一子表。重复以上过程，直到找到满足条件
的记录，使查找成功，或直到子表不存在为止，此时查找不成功。
'''
#非递归实现
def binary_search(alist,item):
    first = 0
    last = len(alist)
    while first<last:
        midpoint = int((first+last)/2)
        if alist[midpoint]==item:
            return True
        elif item < alist[midpoint]:
            last = midpoint -1
        else:
            first = midpoint + 1

    return False

#递归实现
def binary_search2(alist,item):
    if len(alist)==0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item<alist[midpoint]:
                return binary_search2(alist[:midpoint],item)
            else:
                return binary_search2(alist[midpoint+1:],item)

#测试
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 13))
print(binary_search2(testlist, 713))
