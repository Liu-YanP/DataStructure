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