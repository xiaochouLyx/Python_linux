class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
class sigle_list(object):
    """使用默认参数"""
    def __init__(self,node = None):
        """保存头节点 即第一个节点"""
        self._head = node

    """判断链表是否为空"""
    def is_empty(self):
        if self._head == None:
            return True
        else:
            return False


    def The_length(self):
        """定义游标current进行遍历 cur指向头节点"""
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    """遍历链表"""
    def travel(self):
        cur = self._head

        while cur != None:
            print(cur.value,end=" ")
            cur = cur.next

    """头插法"""
    """时间复杂度O(1)"""
    def add(self,value):
        node = Node(value)
        node.next = self._head
        self._head = node

    """指定 最坏是O(n)"""
    def insert(self,value,index):
        if index <= 0:
            self.add(value)
        elif index >= self.The_length()-1:
            self.append(value)
        else:
            node = Node(value)
            count = 0
            pre = self._head
            while count != index-1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node



    """尾插法"""
    def append(self,value):
        """将传入的值构造为一个节点"""
        node = Node(value)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    """删除节点 给出值删除节点"""
    """最坏时间复杂度为O(n)"""
    def remove(self,item):
        cur = self._head
        pre = None
        while cur!=None:
            if cur.value == item:
                """当删除的是第一个节点时 pre还没有进入链表中所以直接对头节点进行操作"""
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


    """查询数据是否存在"""
    """最坏时间复杂度为O(n)"""
    def search(self,item):
        cur = self._head
        while cur != None:
            if cur.value == item:
                return True
            else:
                cur = cur.next
        return False
    """查找链表中倒数第k的值"""
    def FindKthToTail(self,k):
        cur = self._head
        # pre = None
        n = 1
        while cur.next != None:
            if n <k:
                cur = cur.next
                n+=1
            else:
                break
        print(n)
        if n<k:
            return
        else:
            if k <=0:
                return
            pre = self._head
            while cur.next!=None:
                cur = cur.next
                pre = pre.next
        return pre.value

# """链表的反转"""
#三个变量 head当前节点 pre当前节点的前一个节点 temp暂存当前节点
    def reserve(self):
        pre = None   #当前节点的前一个节点
        head = self._head  #当前节点
        """链表为空返回"""
        if head == None:
            return

        while head != None:
            """建立一个临时变量temp"""
            temp = head.next
            head.next = pre  #反转

            pre = head  #pre向右移
            head = temp #head指向下一个节点
        return pre
# 合并两个链表
    #递归调用
    def Merge(self,p1,p2):
        if p1 == None:
            return p2
        if p2 == None:
            return p1
        pMergeNew = None
        if p1.value < p2.value:
            pMergeNew = p1
            pMergeNew.next = self.Merge(p1.next,p2)
        else:

            pMergeNew = p2
            pMergeNew.next = self.Merge(p1,p2.next)
        return pMergeNew

if __name__ == '__main__':
    li = sigle_list()
    # print(li.is_empty())
    li.append(1)
    li.add(2)
    li.append(4)
    li.append(3)
    li.insert(9,3)
    # print(li.is_empty())
    # print(li.The_length())
    # print(li.search(2))
    # li.travel()
    # li.remove(1)
    # print("")
    li.travel()
    print("")
    print(li.FindKthToTail(0))