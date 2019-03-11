#在一个数组中，任选不想相邻的数相加。使其和最大
import numpy as np
arr = [1,2,4,1,7,8,3]  #任意选取不相邻的数，使其和最大

#递归的方法
def rec_opt(arr,i):
    if i==0:
        return arr[0]
    elif i==1:
        return max(arr[0],arr[1])
    else:
        A = rec_opt(arr,i-2)+arr[i]
        B = rec_opt(arr,i-1)
        return max(A,B)

#非递归  一般对于重叠子问题使用，非递归的方法
def opt(arr):
    s = np.zeros(len(arr))
    s[0] = arr[0]
    s[1] = max(arr[0],arr[1])
    for i in range(2,len(arr)):
        A = s[i-2]+ arr[i]
        B = [i-1]
        s[i] = max(A,B)
    return s

if __name__ == '__main__':
    print(rec_opt(arr,len(arr)-1))
    print(opt(arr)[len(arr)-1])
