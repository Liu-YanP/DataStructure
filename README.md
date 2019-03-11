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

** 和冒泡算法的不同之处在于，选择排序是在所有未排序列中选取最小值换一次位置，而冒泡排序需要多次和相邻的数值进行比较换位置 **
```
def select_sort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(i+1,n):
            if alist[j]<alist[i]:
                alist[i],alist[j] = alist[j],alist[i]
```