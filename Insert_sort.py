#插入排序
'''
最优：O(n)
最差：O(n^2)
稳定
'''
def insert_sort(alist):
    for index,item in enumerate(alist):
        while index>0 and  alist[index-1]>item:  #item为待插入元素，从后往前移动直到寻找到，比item小的元素
        	alist[index] = alist[index-1]      #将比item大的元素往后移
        	index-=1
        alist[index]=item                  #直到找到比item小的元素，将item插入


if __name__ == '__main__':
    alist = [2, 4, 5, 23, 2, 1, 4, 1]
    insert_sort(alist)
    print(alist)
