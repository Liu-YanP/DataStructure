def count_sort(ls):
	minValue = min(ls)
	maxValue = max(ls)
	count_ls = range(minValue,maxValue+1)
	nn = [0 for i in range(len(count_ls))]
	new_ls = []
	for i in range(len(count_ls)):
		for value in ls:
			if count_ls[i]==value:
				nn[i]+=1
	for i in range(len(count_ls)):
		for count in range(nn[i]):
			new_ls.append(count_ls[i])

	return new_ls

if __name__ == '__main__':
	ls = [12,3,43,56,7865,53,3]
	print(count_sort(ls))

	
