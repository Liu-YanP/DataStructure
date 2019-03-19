# DataStructure
数据结构与算法

## 冒泡排序
1. 比较相邻元素，若左边比右边大，则交换位置
2. 经过一边的比较后，最小的元素将会在最右边
3. 除第一个元素外，重复步骤1，直到所有元素排序完（外层边界减一）

```
def bubble_sort(alist):
    for i in range(len(alist)-1,0,-1):  #外成循环的边界
        for j in range(j):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
```

## 选择排序
1. 在所有在排序列中，选择最小的放在第一个位置
2. 然后在剩下的未排序列中，选取最小的放在第二个位置
3. 类似与前两步，不停的在未排序列中选取最小的，放在已排序列后

*和冒泡算法的不同之处在于，选择排序是在所有未排序列中选取最小值换一次位置，而冒泡排序需要多次和相邻的数值进行比较换位置*
```
def select_sort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(i+1,n):
            if alist[j]<alist[i]:
                alist[i],alist[j] = alist[j],alist[i]
```
## 插入排序
1. 未排序列的第一个元素看做有序序列，第二个到最后一个元素看做无序序列
2. 按顺序在未排序列中选一个元素，将他插入到已排序列的合适位置（若元素相等，则待插入元素放在相等元素后面）
```
def insert_sort(alist):
    for index,item in enumerate(alist):
        while index>0 and  alist[index-1]>item:  #item为待插入元素，从后往前移动直到寻找到，比item小的元素
        	alist[index] = alist[index-1]      #将比item大的元素往后移
        	index-=1
        alist[index]=item                  #直到找到比item小的元素，将item插入

```

## 希尔排序
1. 首先设定步长gap为int(n/2)
2. 对步长为gap的序列进行插入排序
3. 再次改变步长为gap/2，重复以上步骤。直到步长为1
```
def shell_sort(alist):
    gap = int(len(n)/2)
    while gap>0:
        for i in range(gap,n):
            j = i
            #插入排序法
            while j >= gap and alist[j-gap] > alist[j]:
                alist[j-gap],alist[j] = alist[j],alist[j-alist]
                j -= gap
        gap = int(gap/2) #更新步长
```

## 并归排序
1. 首先通过递归将未排序列二分为左右两个部分
2. 分别为左右两部分设置一个指针
3. 若左指针值小于右指针值，则将左指针值放入列表，并且加一。反之右指针
```
def merge_sort(alist):
    if len(alist)>=1:
        return alist
    num = int(len(alist)/2)
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])
    return merge(left,right)

def merge(left,right):
    result = []
    l,r = 0,0
    while l < len(left) and r < len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    result+=left[l:]
    result+= right[r:]
```

## 快速排序
1. 从数列中挑出一个元素，称为"基准"（pivot），
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面
（相同的数可以到任一边）。
3. 在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

```
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
        #将high指向的元素放到low的位置上
        alist[low] = alist[high]

        #如果low与high未重合，low指向的元素比基准元素小，则low向右移
        while low < high and alist[low] < mid:
            low +=1
        #将low指向的元素放到high的位置上
        alist[high] = alist[low]

    #退出循环后，此时low和high重合，指向的位置为基准元素的正确位置
    #将基准元素放到该位置
    alist[low] = mid

    #对基准元素左边的子序列进行快速排序
    quick_sort(alist, start,low-1)

    #对基准元素右边的子序列进行快速排序
    quick_sort(alist,low+1,end)

```
## 堆排序
大顶堆:所有父节点都大于左右子节点的完全二叉树
将一个列表转化为完全树，下标为$i$的元素的左子树的下标为$2*i+1$，右子树为$2*i+2$，父节点为i//2(//表示取整)

1. 构建初始大顶堆
2. 将堆顶元素（即最大的元素）与末尾元素进行交换，使末尾元素最大。
3. 然后再次重建大顶堆，堆顶的元素为第二大元素
4. 循环往复步骤2和3，寻找出第三、第四...大元素
```
# 堆排序算法
def heap_sort(ls):
    n = len(ls)
    for i in range(n//2-1,-1,-1):  #初始化堆  i为最后一个有子树的节点
        adjustHeap(ls,i,n-1)   #从最后一含有子树的节点开始

    for i in range(n-1,-1,-1):
        ls[0],ls[i] = ls[i],ls[0]  #堆顶和最后的叶子元素换位置
        adjustHeap(ls,0,i-1)  #从堆顶开始调整
    return ls
def adjustHeap(ls,i,n):
    temp = ls[i]  #父元素
    j = 2*i+1  #左子节点
    while j<=n:#左子节点存在，
        if j<n and ls[j]<ls[j+1]:#右节点存在，并且左节点大于右节点
            j+=1
        if temp<ls[j]:
            ls[i] = ls[j]
            i = j
            j = 2*j+1
        else:
            break
    ls[i] = temp
    return ls
    
if __name__ == '__main__':
    ls = [2,45,3,54,674,35,5]
    print(heap_sort(ls))
```