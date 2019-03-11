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