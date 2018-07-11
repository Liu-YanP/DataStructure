# 实现一个单链表


# 节点的实现
class SingleNode(object):
    """单链表的节点"""

    def __init__(self, item):
        #-item存放数据
        self.item = item
        #_next是下一个节点
        self.next = None

'''
单链表的操作：
is_emoty()是否为空
length()链表长度
travel()链表遍历
add(item)链表头部添加元素
append(item)链表尾部添加元素
insert(pos,item)指定位置添加元素
remove(item)删除节点
search(item)搜索节点是否存在
'''


class SingleLinkList(object):
    """单链表"""

    def __init__(self):
        self._head = None

    def is_emoty(self):
        '''判断链表是否为空'''
        return self._head == None

    def length(self):
        '''链表长度'''
        # cur初始时指向头结点
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print('')

    def add(self, item):
        '''头部添加元素'''
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        '''尾部添加元素'''
        node = SingleNode(item)
        if self.is_emoty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''指定位置添加元素'''
        # 若指定位置为第一个元素前，执行头部插入
        if pos <= 0:
            self.add(item)

        # 若指定位置为尾部，执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        # 指定位置
        else:
            node = SingleNode(item)
            count = 0
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        '''删除节点'''
        cur = self._head
        pre = None
        while cur != None:
            # 找到要删除的节点
            if cur.item == item:
                if not pre:
                    self._head = cur.next
                else:
                    # 将删除位置的下一个节点赋给删除的前一个节点
                    pre.next = cur.next
                break
            # 没找到要删除的节点，继续向后移
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        '''链表查找节点是否存在，并返回T，F'''
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    # 定义一个单链表
    ll = SingleLinkList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(5)
    ll.insert(3, 4)
    ll.add(0)
    print('链表长度为：', ll.length())
    ll.travel()
    print(ll.search(5))
    ll.remove(2)
    print(ll.search(2))
    print('-------')
    ll.travel()
