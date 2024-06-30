class students:
 data=['ram','shaym','hari']
 
 def display(self):
   for i in self.data:
     print(i)

 def insert(self,name):
   self.data.append(name)
   self.display()

 def update(self,index,name):
   self.data[index]=name
   self.display()

 def delete(self,index):
   self.data.pop(index)
   self.display()

obj = students()
obj.insert()
obj.update()
obj.delete()

 