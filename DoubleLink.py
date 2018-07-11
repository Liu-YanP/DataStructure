# 双向链表
'''
每个节点有两个链接：一个指向前一个节点，
当此节点为第一个节点时，指向空值；而另一个指向下一个节点，
当此节点为最后一个节点时，指向空值。

操作
is_empty() 链表是否为空
length() 链表长度
travel() 遍历链表
add(item) 链表头部添加
append(item) 链表尾部添加
insert(pos, item) 指定位置添加
remove(item) 删除节点
search(item) 查找节点是否存在
'''


class Node(object):
    """双向链表节点"""

    def __init__(self, item):
        self.next = None
        self.prev = None
        self.item = item


class DLinkList(object):
    """双向链表"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        cur = self._head
        if self.is_empty():
            return
        while cur != None:
            print(cur.item)
            cur = cur.next
        print('')

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            # 遍历到尾部
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            while count < (pos - 1):
                count += 1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return
        else:
            cur = self._head
            # 第一个元素就是要删除的
            if cur.item == item:
                # 只有一个元素
                if cur.next == None:
                    self._head = None
                else:
                    cur.next.prev = None
                    self._head = cur.next
                return
            else:
                while cur != None:
                    if cur.item == item:
                        cur.next.prev = cur.prev
                        cur.prev.next = cur.next
                        break
                    cur = cur.next


# 测试
if __name__ == '__main__':
    ll = DLinkList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.insert(2, 3)
    ll.add(0)
    print('双向链表长度：', ll.length())
    ll.travel()
    ll.remove(3)
    print(ll.search(2))
    print(ll.search(3))
