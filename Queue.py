'''This is the implementation of queue'''

class Queue():

    def __init__(self):
        self.que=[]

    def enqueue(self,data):

        ''' This will insert element in Queue'''

        self.que.append(data)

    def dequeue(self):

        ''' This will remove element in Queue'''
        
        try:
            self.que.remove(self.que[0])
        except IndexError:
            print('Please Enqueue before Dequeue')
            
    def isEmpty(self):
        
        ''' This will tell you if queue is empty or not'''
        
        if len(self.que):
            return False
        else:
            return True


    def find(self,data):
        
        ''' Method to test if element exist inside Queue'''
        
        self.exist_in_queue='N'

        for i in range(len(self.que)):
            if i==data:
                return True
            else:
                self.exist_in_queue='N'

        if self.exist_in_queue=='N':
            return False
            

        
