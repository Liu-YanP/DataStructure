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

	
