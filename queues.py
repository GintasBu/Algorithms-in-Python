class Queue:
    def __init__(self):
        self.length=0
        self.head=None
        
    def is_empty(self):
        return (self.length==0)
        
    def insert(self, cargo):
        node=Node(cargo)
        node.next=None
        if self.head==None: 
            self.head=node
        else:
            last=self.head
            while last.next: 
                last=last.next
            last.next=node
        self.length=self.length+1
        
        
    def remove(self):
        cargo=self.head.cargo
        self.head=self.head.next
        self.length-=1
        return cargo
        
        
class Node:
    
    def __init__(self, cargo=None, next=None):
        self.cargo=cargo
        self.next=next
    
    def __str__(self):
        return str(self.cargo)
        
    def print_list(self):
        while self:
            print self,
            self=self.next
        #print
     
    
    
    def print_backward(self):
        if self.next != None:
            tail = self.next
            tail.print_backward()
        print self.cargo,        
        
        
        
        
class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head   = None
        self.last   = None

    def is_empty(self):
        return (self.length == 0)
        
        
    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.length == 0:
            # if list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # find the last node
            last = self.last
            # append the new node
            last.next = node
            self.last = node
        self.length = self.length + 1
        
    def remove(self):
        cargo=self.head.cargo
        self.head=self.head.next
        self.length-=1
        if self.length==0: self.last=None
        return cargo
		
    def print_queue(self):
        while self:
            print self.head.cargo,
            self=self.next