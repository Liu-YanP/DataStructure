#插入排序
'''
最优：O(n)
最差：O(n^2)
稳定
'''
def insert_sort(alist):
    for index,item in enumerate(alist):
        while index>0 and  alist[index-1]>item:
        	alist[index] = alist[index-1]
        	index-=1
        alist[index]=item


if __name__ == '__main__':
    alist = [2, 4, 5, 23, 2, 1, 4, 1]
    insert_sort(alist)
    print(alist)
