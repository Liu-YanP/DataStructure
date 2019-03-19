#快速排序算法
'''
步骤为：

1.从数列中挑出一个元素，称为"基准"（pivot），
2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面
（相同的数可以到任一边）。3.在这个分区结束之后，该基准就处于数列的中间位置。这个称为
分区（partition）操作。递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
'''
def quick_sort(alist,start,end):
    '''快速排序'''

    #递归退出条件
    if start>=end:
        return

    #将起始元素设置为基准元素
    mid = alist[start]

    #low为序列从左向右滑动的游标
    low = start
    #high为序列从右向左滑动的游标
    high = end

    while low < high:
        #如果low和high未重合，high指向的元素不比基准元素小，则high向左移
        while low < high and alist[high] >=mid:
            high -= 1
        #将high指向的元素比基准元素小，则放到low的位置上
        alist[low] = alist[high]  #此时low位置上是，基准元素。不怕被覆盖

        #如果low与high未重合，low指向的元素比基准元素小，则low向右移
        while low < high and alist[low] < mid:
            low +=1

        #将low指向的元素放到high的位置上
        alist[high] = alist[low]  #此时higt的元素已经赋值给之前的low了，不怕被覆盖

    #退出循环后，此时low和high重合，指向的位置为基准元素的正确位置
    alist[low] = mid

    #对基准元素左边的子序列进行快速排序
    quick_sort(alist, start,low-1)

    #对基准元素右边的子序列进行快速排序
    quick_sort(alist,low+1,end)


#测试
if __name__ == '__main__':
    alist = [2,5,7,6,3,1]
    quick_sort(alist,0,len(alist)-1)
    print(alist)
