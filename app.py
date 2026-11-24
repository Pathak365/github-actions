# This is a student class
class student:

  def __init__(self, name, age, location):
      self.name = name
      self.age = age
      self.location = loca

  def is_teen(self):
    if 13>= self.age <= 19:
      print(f"{self.name} is teen")

    else:
      print(f"{self.name} is not teen")


student1 = student("Rahul", 33, "Delhi")
print(student1.is_teen())
