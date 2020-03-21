class ListNode:
    def __init__(self, data=0,next=None):
        self.data = data 
        self.next = next 
    
def search_list(L, key):
    while (L and L.data!=key):
        L = L.next 
    return L


def insert_after (node, new_node):
    new_node.next = node.next 
    node.next = new_node

# 7.1 Merge two sorted linked list

def merge_linked_list (node1, node2):
    curNode = ListNode()
    if node1 == None and node2 == None:
        curNode.next = None 
    elif node1 == None and node2 != None: 
        curNode.next = merge_linked_list(node1.next, node2) 
    elif node1 != None and node2 == None:
        curNode.next = merge_linked_list(node1.next, node2)
    else: 
        if node1.data < node2.data:
            curNode.data = node1.data 
            curNode.next = merge_linked_list(node1.next, node2)
        else:
            curNode.data = node2.data 
            curNode.next = merge_linked_list(node1, node2.next)
    return curNode


# Consider using dummy head to reduce bug 
def betterMethod (L1, L2):
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next 
        else: 
            tail.next, L2 = L2, L2.next 
        tail = tail.next 
    
    tail.next = L1 or L2 

    return dummy_head.next 