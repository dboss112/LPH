class Parent(object):
 def override(self):
  print "PARENT override()"

 def implicit(self):
  print "PARENT implicit()"

 def altered(self):
  print "PARENT altered()"

class Child(Parent):

 def override(self):
  print "CHILD override()"

 def altered(self):
  print "CHILD, BEFORE PARENT altered()"
  super(Child, self).altered()
  print "CHILD, AFTER PARENT altered()"

class Demo(object):
 
 
 def work(self,my_obj):
  if my_obj != c: 
   my_obj.implicit()
  
  my_obj.override()
  my_obj.altered()
 
 

d=Demo()
p=Parent()
c=Child()
d.work(p)
d.work(c)
