import sys
input = sys.stdin.readline

class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        
# cursor 왼쪽이면 current
# cursor 오른쪽이면 current.next

class LinkedList:
    def __init__(self):
        self.head = self.current = ListNode(val=None)
        
    def append(self, val):
        self.current.next = ListNode(val=val, prev=self.current) 
        self.current = self.current.next
        
    def cmd_l(self):
        if self.current.prev != None:
            self.current = self.current.prev
    
    def cmd_d(self):
        if self.current.next != None:
            self.current = self.current.next
        
    def cmd_b(self):
        if self.current.prev != None:
            to_delete = self.current
            
            if to_delete.prev != None:                
                self.current.prev.next = self.current.next
            if to_delete.next != None:
                to_delete.next.prev = to_delete.prev
            self.current = self.current.prev
        
    def cmd_p(self, val):
        new_node = ListNode(val=val, prev=self.current, next=self.current.next)
        if self.current.next:
            self.current.next.prev = new_node
        
        self.current.next = new_node        
        self.current = self.current.next
        
    def print(self):
        node = self.head.next
        while node:
            print(node.val, end='')
            node = node.next

linked_list = LinkedList()            
str = input()
m = int(input())

for c in str.strip():
    linked_list.append(c)

for _ in range(m):
    command = input().split()
    if command[0] == 'P':
        linked_list.cmd_p(command[1])        
    elif command[0] == 'L':
        linked_list.cmd_l()        
    elif command[0] == 'D':
        linked_list.cmd_d()        
    elif command[0] == 'B':
        linked_list.cmd_b()        

linked_list.print()
