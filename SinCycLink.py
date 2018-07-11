'''
单向循环链表，链表中最后一个节点的next域不再为None，而是指向链表的头节点。

操作：
is_empty() 判断链表是否为空
length() 返回链表的长度
travel() 遍历
add(item) 在头部添加一个节点
append(item) 在尾部添加一个节点
insert(pos, item) 在指定位置pos添加节点
remove(item) 删除一个节点
search(item) 查找节点是否存在
'''


class Node(object):
	"""节点"""

	def __init__(self, item):
		self.next = None
		self.item = item


class SinCycLinkList(object):
	"""单向循环列表"""

	def __init__(self):
		self._head = None

	def is_empty(self):
		return self._head == None

	def length(self):
		if self.is_empty():
			return 0
		else:
			count = 1
			cur = self._head
			while cur.next != self._head:
				count += 1
				cur = cur.next
			return count

	def travel(self):
		if self.is_empty():
			return
		else:
			cur = self._head
			print(cur.item)
			while cur.next != self._head:
				cur = cur.next
				print(cur.item)
		print('')

	def add(self,item):
		'''头部添加节点'''
		node = Node(item)
		if self.is_empty():
			self._head = node
			node.next = self._head
		else:
			node.next = self._head
			# 找到尾节点
			cur = self._head
			while cur.next!=self._head:
				cur = cur.next
			# 尾节点指向Node
			cur.next = node
			#_head指向添加的node
			self._head = node

	def append(self,item):
		node = Node(item)
		if self.is_empty():
			self._head = node
			node.next = self._head
		else:
			cur = self._head
			while cur.next!=self._head:
				cur = cur.next
			cur.next = node
			node.next = self._head


	def insert(self,pos,item):
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			node = Node(item)
			cur = self._head
			count = 0
			while count < (count-1):
				count+=1
				cur = cur.next
			node.next = cur.next
			cur.next = node


	def remove(self,item):
		if self.is_empty():
			return
		else:
			cur = self._head
			pre = Node
			# 第一个节点元素就是要删除元素
			if cur.item == item:
				# 链表不知一个元素
				if cur.next!=self._head:
					# 找到尾节点指向第二个元素
					while cur.next!=sel._head:
						cur = cur.next
					cur.next = self._head.next
					self._head = self._head.next
				else:
					self._head = Node
            # 首节点不是要删除的元素
			else:
			    pre = self._head
			    while cur.next!=self._head:
			    	if cur.item == item:
			    		pre.next=cur.next
			    		return
			    	else:
			    		pre = cur
			    		cur = cur.next

			    if cur.item==item:
			    	pre.next = cur.next


	def search(item):
		if self.is_empty():
			return False
		cur = self._head
		if cur.item==item:
			return True
		else:
			while cur.next!=self._head:
				cur = cur.next
				if cur.item==item:
					return True
		return False


# 测试
if __name__ == '__main__':
	ll = SinCycLinkList()
	ll.append(1)
	ll.append(2)
	ll.append(4)
	ll.insert(2,3)
	ll.add(0)
	ll.travel()
	print("链表长度：",ll.length())
	ll.remove(2)
	ll.travel()
			                      
			

