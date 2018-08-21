class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


def v1 (vin, r1, r2):
  v1=vin*(r2/(r1+r2))
  print(v1)
v1(3.3,5000.0,2000.0)