#选择排序
'''
最优：O(n^2)
最差：O(n^2)
不稳定
'''
def selection_sort(alist):
    n = len(alist)
    for j in range(n):
        for i in range(j + 1, n):
            if alist[i] < alist[j]:
                alist[j],alist[i] = alist[i],alist[j]


if __name__ == '__main__':
    alist = [2,3,1]
    selection_sort(alist)
    print(alist)
