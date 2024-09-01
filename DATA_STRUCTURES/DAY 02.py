# class Node:
#     def __init__(self,data=None,next=None):
#         self.data = data
#         self.next = next

# class Linked_list:
#     def __init__(self):
#         self.head = None
    
#     def insert_at_begining(self,data):
#         node = Node(data,self.head)
#         self.head = node
        
#     def insert_at_end(self,data):
#         if self.head is None:
#             self.head = Node(data)
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data)
    
#     def len_of_ll(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count += 1
#             itr = itr.next
#         return count
        
#     def insert_at(self,index,data):
#         if index < 0 or index > self.len_of_ll():
#             raise Exception("Invalid index")
#         if index == 0:
#             self.insert_at_begining(data)
#             return
        
#         itr = self.head
#         count = 0
#         while itr:
#             if count == index - 1:
#                 node = Node(data,itr.next)
#                 itr.next = node  
#             itr = itr.next
#             count += 1 
#     # Exercise -------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            
#     def insert_after_value(self, data_after, data_to_insert):
        
#         itr = self.head
#         while itr:
#             if itr.data == data_after:
#                 node = Node(data_to_insert,itr.next)
#                 itr.next = node
#                 break
#             itr = itr.next
            
#     def remove_by_value(self, data):
#         if self.head is None:
#             return

#         if self.head.data == data:
#             self.head = self.head.next
#             return

#         itr = self.head
#         while itr.next:
#             if itr.next.data == data:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next
        
        

        
        
            
#     def print(self):
#         itr = self.head
#         llstr = ''
#         while itr:
#             suffix = ''
#             if itr.next:
#                 suffix = '--->'
#             llstr += str(itr.data) + suffix
#             itr = itr.next
#         print(llstr)



# class Nodes:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev


            
           
# if __name__ == '__main__':
#     h = Linked_list()
#     h.insert_at_begining(344)
#     h.insert_at_begining(75)
#     h.print()
#     h.insert_at_end(67)
#     h.insert_at_end(400)
#     h.print()
#     h.insert_at(2, 1000)
#     h.print()
#     h.insert_after_value(1000,2000)
#     h.print()
#     h.remove_by_value(67)
#     h.print()

