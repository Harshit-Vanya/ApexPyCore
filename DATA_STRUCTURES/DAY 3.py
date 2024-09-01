# class Hashtable:
#     def __init__(self):
#         self.max = 15
#         self.arr = [[] for i in range(self.max)]
        
#     def get_hashmap(self,key):
#         num = 0
#         for i in key:
#             num += ord(i)
#         return num % self.max
    
#     def __setitem__(self,key,val):
#         h = self.get_hashmap(key)
#         fnd =False
#         for idx, elem in enumerate(self.arr[h]):
#             if len(elem) ==2 and elem[0]==key:
#                 self.arrh[h][idx] = (key,val)
#                 fnd = True
#         if not fnd:
#             self.arr[h].append( (key,val) )
       
        
#     def __getitem__(self,key):
#         h = self.get_hashmap(key)
#         for kv in self.arr[h]:
#             if kv[0]== key: 
#                 return kv[1]
    
#     def __delitem__(self,key):
#         h = self.get_hashmap(key)
#         for idx, kv in enumerate(self.arr[h]):
#             if kv[0]== key:
#                 del self.arr[h][idx]
#             else:
#                 return "not found"
    
        
             


       
# -------------------------------------------------------------------EXERCISE---------------------------------------------------------------------------






#     h['Harshit'] = 7
    
    
   
#     print(h['Harshit'])
#     h.__setitem__('Jan 1',27)
#     h.__setitem__('Jan 2',31)
#     h.__setitem__('Jan 3',23)
#     h.__setitem__('Jan 4',34)
#     h.__setitem__('Jan 5',37)
#     h.__setitem__('Jan 6',38)
#     h.__setitem__('Jan 7',29)
#     h.__setitem__('Jan 8',30)
#     h.__setitem__('Jan 9',35)
#     h.__setitem__('Jan 10',30)
    
    # print(h.__getaverage__())

# if __name__ == '__main__':
#     h = Hashtable()
    

#     arv = []

#     f = open("C:\\WHISKEY.py\\DATA STRUCTURES\\material\\nyc_weather.csv","r")
#     for line in f:
#         tokens = line.split(',')
#         try:
#             temperature = int(tokens[1])
#             h.__setitem__(tokens[0],temperature)
#             arv.append(temperature)
#         except:
#             print("Invalid temperature.Ignore the row")

#     def avg7():
#         sum =0
#         for i in range(0,6):
#             sum += arv[i]
#         return sum/7 

#     def max10():
#         max_temp = 0
#         for i in range(0,9):
#             if arv[i]>max_temp:
#                 max_temp = arv[i]
#         return max_temp

#     print(h.__getitem__('Jan 9'))
#     print(h.__getitem__('Jan 4'))

# word_count = {}
# with open("C:\\WHISKEY.py\\DATA STRUCTURES\\material\\poem (1).txt","r") as f:
#     for line in f:
#         words = line.split(' ')
#         for word in words:
#             word=word.replace('\n','')
#             if word in word_count:
#                 word_count[word]+=1
#             else:
#                 word_count[word]=1
# print(line)        
# print(word)
# print(word_count)