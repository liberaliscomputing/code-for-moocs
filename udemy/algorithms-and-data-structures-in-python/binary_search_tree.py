# -*- coding: utf-8 -*-
class Node(object):

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)
            
    def insert_node(self, data, node):
        if node.data > data:
            if node.prev:
                self.insert_node(data, node.prev)
            else:
                node.prev = Node(data)
        else:
            if node.next:
                self.insert_node(data, node.next)
            else:
                node.next = Node(data)
        
    def delete(self, data):
        if not self.root:
            return 'Binary search tree is empty.'
        self.delete_node(data, self.root)
    
    def delete_node(self, data, node):       
        if node.data > data:
            if node.prev:
                node.prev = self.delete_node(data, node.prev)  
        elif node.data < data:
            if node.next:
                node.next = self.delete_node(data, node.next)      
        elif node.data == data:
            if not node.prev and not node.next:
                print 'Removing a leaf node...'
                del node
                return None
            elif not node.prev:
                print 'Removing a node with a right child...'
                next = node.next
                del node
                return next
            elif not node.next:
                print 'Removing a node with a left child...'
                prev = node.prev
                del node
                return prev
            else:
                print 'Removing a node with two children...'
                pred = self.get_max(node.prev)
                node.data = pred.data
                node.prev = self.delete_node(pred.data, node.prev)
                return node
        else:
            print 'No node found: {}'.format(data)
                
    def get_min_val(self):
        if not self.root:
            return 'Binary search tree is empty.'
        return self.get_min(self.root)
    
    def get_min(self, node):
        if not node.prev:
            return node
        return self.get_min(node.prev)
    
    def get_max_val(self):
        if not self.root:
            return 'Binary search tree is empty.'
        return self.get_max(self.root)
    
    def get_max(self, node):
        if not node.next:
            return node
        return self.get_max(node.next)
    
    def traverse(self, order='in'):
        if not self.root:
            return 'Binary search tree is empty.'
        else:
            if order == 'in':
                self.traverse_in_order(self.root)
            elif order == 'pre':
                self.traverse_pre_order(self.root)
            elif order == 'post':
                self.traverse_post_order(self.root)
            else:
                return 'Wrong order parameter.'
    
    def traverse_in_order(self, node):
        if node.prev:
            self.traverse_in_order(node.prev)
            
        print node.data
        
        if node.next:
            self.traverse_in_order(node.next)
        
    def traverse_pre_order(self, node):
        print node.data
        
        if node.prev:
            self.traverse_pre_order(node.prev)
            
        if node.next:
            self.traverse_pre_order(node.next)
        
    def traverse_post_order(self, node):
        if node.prev:
            self.traverse_post_order(node.prev)
            
        if node.next:
            self.traverse_post_order(node.next)
            
        print node.data

        
if __name__ == '__main__':
    bst = BinarySearchTree()
