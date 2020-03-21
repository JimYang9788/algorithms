class ListNode:
    def __init__(self, data=0,next=None):
        self.data = data 
        self.next = next 
    
    def search_list(self, L, key):
        while (L and L.data!=key):
            L = L.next 
        return L

    
