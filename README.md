# DataStructure
数据结构与算法

## 冒泡排序
* 思想：对待排序元素的关键字从后往前进行多遍扫描，遇到相邻两个关键字次序与排序规则不符时，就将这两个元素进行交换。这样关键字较小的那个元素就像一个泡泡一样，从最后面冒到最前面来。
* 时间复杂度：最坏：O(n2) 最好: O(n) 平均: O(n2)
* 空间复杂度：O(1)
* 稳定性：稳定，相邻的关键字两两比较，如果相等则不交换。所以排序前后的相等数字相对位置不变。

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
* 思想：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后每次从剩余未排序元素中继续寻找最小（大）元素放到已排序序列的末尾。以此类推，直到所有元素均排序完毕.
* 时间复杂度：最坏:O(n^2) 最好: O(n^2) 平均: O(n^2)
* 空间复杂度：O(1)
* 稳定性：不稳定 例如数组 2 2 1 3 第一次选择的时候把第一个2与1交换使得两个2的相对次序发生了改变。

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
* 思想：每次将一个待排序的数据按照其关键字的大小插入到前面已经排序好的数据中的适当位置，直到全部数据排序完成。
* 时间复杂度：O(n^2) O(n) O(n^2) （最坏 最好 平均）
* 空间复杂度：O(1)
* 稳定性： 稳定 每次都是在前面已排好序的序列中找到适当的位置，只有小的数字会往前插入，所以原来相同的两个数字在排序后相对位置不变。

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
* 思想：希尔排序根据增量值对数据按下标进行分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整体采用直接插入排序得到有序数组，算法终止。
* 时间复杂度：O(n2) O(n) O(n1.5) （最坏，最好，平均）
* 空间复杂度：O(1)
* 稳定性：不稳定 因为是分组进行直接插入排序，原来相同的两个数字可能会被分到不同的组去，可能会使得后面的数字会排到前面，使得两个相同的数字排序前后位置发生变化。
* 不稳定举例: 4 3 3 2 按2为增量分组，则第二个3会跑到前面

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
* 思想：归并排序采用了分治算法，首先递归将原始数组划分为两个子数组，直到数组元素个数为1，对每个子数组进行排序。然后将排好序的子数组递归合并成一个有序的数组。
* 时间复杂度：最坏:O(nlog2n) 最好: O(nlog2n) 平均: O(nlog2n)
* 空间复杂度：O(n)
* 稳定性：稳定

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
* 思想：该算法是分治算法，首先选择一个基准元素,根据基准元素将待排序列分成两部分,一部分比基准元素小,一部分大于等于基准元素,此时基准元素在其排好序后的正确位置,然后再用同样的方法递归地排序划分的两部分。基准元素的选择对快速排序的性能影响很大，所有一般会想打乱排序数组选择第一个元素或则随机地从后面选择一个元素替换第一个元素作为基准元素。
* 时间复杂度：最坏:O(n2) 最好: O(nlogn) 平均: O(nlogn)
* 空间复杂度：O(nlogn)用于方法栈
* 稳定性：不稳定 快排会将大于等于基准元素的关键词放在基准元素右边，加入数组 1 2 2 3 4 5 选择第二个2 作为基准元素，那么排序后 第一个2跑到了后面，相对位置发生变化。

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
* 思想：堆排序是利用堆的性质进行的一种选择排序，先将排序元素构建一个最大堆,每次堆中取出最大的元素并调整堆。将该取出的最大元素放到已排好序的序列前面。这种方法相对选择排序，时间复杂度更低，效率更高。
* 时间复杂度：最坏:O(nlog2n) 最好: O(nlog2n) 平均: O(nlog2n)
空间复杂度：O(1)
* 稳定性：不稳定 例如 5 10 15 10。 如果堆顶5先输出，则第三层的10(最后一个10)的跑到堆顶，然后堆稳定，继续输出堆顶，则刚才那个10跑到前面了，所以两个10排序前后的次序发生改变。

大顶堆:所有父节点都大于左右子节点的完全二叉树
将一个列表转化为完全树，下标为$i$的元素的左子树的下标为 $2i+1$，右子树为$2i+2$，父节点为i//2(//表示取整)

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
## 计数排序
局限于整数。
1. 找到无序数组A中的最大值maxValue
2. 开辟一个新的数组B，长度为maxValue+1
3. 开始计数：如果无序数组A的值等与新数组B的下标，则数组B在该下标处的值加一
4. 遍历数组B,输出结果
```
import random
def count_sort(ls):
    maxValue = max(ls)
    count_ls = [0 for i in range(maxValue+1)]
    new_ls = []
    for value in ls:
        count_ls[value] +=1 

    for i in range(len(count_ls)):
        for count in range(count_ls[i]):
            new_ls.append(i)
    return new_ls

if __name__ == '__main__':
    ls = list(range(20))
    random.shuffle(ls)  #在源列表上洗牌
    print(ls)
    print(count_sort(ls))
```
## 桶排序
1. 首先计算每个桶内的数据范围
2. 遍历所有元素，将元素放入对应的桶内
3. 对每个桶内的元素排序
4. 将每个桶的元素连接起来
```
import random

def bucket_sort(ls,bucketSize):
    minValue = min(ls)
    maxValue = max(ls)
    buckets = [[] for i in range(bucketSize)]  #初始化桶
    result = []

    space = (maxValue-minValue+1)/bucketSize  #计算每个桶的数据范围

    for  i in ls:
        j = int((i-minValue)//space)  #计算元素应该放入那个桶，j为桶的编号
        buckets[j].append(i)
    for i in range(bucketSize):
        adjust_bucket(buckets[i])  #对桶内元素进行排序
        result.extend(buckets[i])
    return result

def adjust_bucket(ls):  #对桶内元素进行排序
    for index, item in enumerate(ls):
        while index>0 and ls[index-1]>item:
            ls[index] = ls[index-1] 
            index = index-1
        ls[index] = item

if __name__ == '__main__':
    ls = list(range(20))
    random.shuffle(ls)
    print(ls)
    print(bucket_sort(ls,4))
```
## 基数排序
* 思想：基数排序是通过“分配”和“收集”过程来实现排序，首先根据数字的个位的数将数字放入0-9号桶中，然后将所有桶中所盛数据按照桶号由小到大，桶中由顶至底依次重新收集串起来，得到新的元素序列。然后递归对十位、百位这些高位采用同样的方式分配收集，直到没各位都完成分配收集得到一个有序的元素序列。
* 时间复杂度：最坏:O(d(r+n)) 最好:O(d(r+n)) 平均: O(d(r+n))
* 空间复杂度：O(dr+n) n个记录，d个关键码，关键码的取值范围为r
* 稳定性：稳定 基数排序基于分别排序，分别收集，所以其是稳定的排序算法。

1. 计算最大元素的位数
2. 初始化桶，范围[0,9]
3. 从元素的最低位数开始，将其放入对应下标的桶中
4. 然后按顺序连接桶中元素，并再次将元素按十位上的数放入对应桶的下标
5. 循环步骤3、4,直到最高位处理完。将数据输出
```
# 基数排序
import random
def radix_sort(ls):
    maxValue = max(ls)
    d = len(str(maxValue))  #最大值的位数
    for i in range(d):
        buckets = [[] for i in range(10)]
        for j in range(len(ls)):
            buckets[ls[j]//(10**i)%10].append(ls[j])
            #print(buckets)
        ls = []
        for bucket in buckets:
            ls.extend(bucket)
    return ls

if __name__ == '__main__':
    ls = list(range(25))
    random.shuffle(ls)
    print(ls)
    print(radix_sort(ls))
```