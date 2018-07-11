#冒泡排序
'''
最优：O(n)
最差：O(n^2)
稳定
'''
def bubble_sort(alist):
    for j in range(len(alist) - 1, 0, -1):
        for i in range(j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


if __name__ == '__main__':
    alist = [25,2,12,14,54,41,15,23,45,21,4]
    bubble_sort(alist)
    print(alist)
