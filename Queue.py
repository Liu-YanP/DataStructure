#队列的实现

'''
同栈一样，队列也可以用顺序表或者链表实现。

操作
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
'''
class Queue(object):
	"""队列"""
	def __init__(self):
		self.items = []		


	def is_empty(self):
		return self.items == []

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()


	def size(self):
		return len(self.items)


#测试
if __name__ == '__main__':
	queue = Queue()
	queue.enqueue('hello')
	queue.enqueue('liu')
	print(queue.size())
	print(queue.dequeue())
	print(queue.size())