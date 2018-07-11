#插入排序
'''
最优：O(n)
最差：O(n^2)
稳定
'''
def insert_sort(alist):
    n = len(alist)
    for j in range(1, n ):
        for i in range(j):
            if alist[i] > alist[j]:
                alist[j], alist[i] = alist[i], alist[j]


if __name__ == '__main__':
    alist = [2, 4, 5, 23, 2, 1, 4, 1]
    insert_sort(alist)
    print(alist)
