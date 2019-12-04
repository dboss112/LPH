# classes and objects

class Demo(object):

  def __init__(self,name,age):
    self.name = name
    self.age=age 
 
  def details(self):
    print self.name
    print self.age
   
p1 = Demo("vinay",22)
p2 = Demo("amith",26)

p1.details()
p2.details()
