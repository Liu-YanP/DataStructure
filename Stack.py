#栈结构的实现
'''
可以用顺序表（list、tuple）实现或链表

栈的操作
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
'''
class Stack(object):
	"""栈"""
	def __init__(self):
		self.items = []  #使用list实现

	def is_empty(self):
		return self.items == []


	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)


#测试

if __name__ == '__main__':
	stack = Stack()
	stack.push('hello')
	stack.push('liu')
	print(stack.peek())
	print(stack.pop())
	print(stack.size())
		