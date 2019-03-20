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
