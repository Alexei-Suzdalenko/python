class Person:
  def __init__(self, name, age):
    self.name = name
    self.age  = age
  test = 'other value'  

p1 = Person('alexei', 40)

print( p1 )
print( p1.name )
print( p1.age ) 
print( p1.test )