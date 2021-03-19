class ListNode():
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"

def addTwoNumbers( l1: ListNode, l2: ListNode) -> ListNode:
    n1 = 0
    s1 = 0
    index1 = l1
    while index1.next != None:
        s1 = s1 + index1.val * 10 ** n1
        n1 = n1 + 1
        index1 = index1.next
    s1 = s1 + index1.val * 10 ** n1
    n1 = n1 + 1


    n2 = 0
    s2 = 0
    index2 = l2
    while index2.next != None:
        s2 = s2 + index2.val * 10 ** n2
        n2 = n2 + 1
        index2 = index2.next
    s2 = s2 + index2.val * 10 ** n2
    n2 = n2 + 1

    s3 = s1 + s2
    l3 = ListNode(s3 % 10)
    index3 = l3
    s3 = s3 // 10
    while s3 > 0:
        new3 = ListNode(s3 % 10)
        index3.next = new3
        index3 = new3
        s3 = s3 // 10
    return l3

l=addTwoNumbers(ListNode([2,4,3]),ListNode([5,6,4]))
print(l)

