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