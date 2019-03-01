class A:
   message = "class message"

   @classmethod
   def cfoo(cls):
      print(cls.message)

   def foo(self, msg):
      self.message = msg
      print(self.message)

   def __str__(self):
      return self.message
 