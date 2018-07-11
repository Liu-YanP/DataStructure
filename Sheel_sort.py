#希尔排序

def shell_sort(alist):
    n = len(alist)
    #初始步长
    gap = int(n/2)
    while gap > 0:
        #按步长进行插入排序
        for i in range(gap,n):
            j = i
            #插入排序
            while j >= gap and alist[j-gap] > alist[j]:
                alist[j-gap],alist[j] = alist[j],alist[j-gap]
                j-=gap

            #得到新步长
        gap = int(gap / 2)


#测试
alist = [25,2,12,14,54,41,15,23,45,21,4]
shell_sort(alist)
print(alist)
