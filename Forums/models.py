#Workshop - Filtering
class Member:
	def __init__(self,member_name,member_age):
		self.name = member_name
		self.age = member_age

	def __str__(self):
		return "Name: {} | Age: {}".format(self.name,self.age)

class Post:
	def __init__(self,title,content):
		self.title = title
		self.content =content

	def __str__(self):
		return "Title: {} | {}".format(self.title,self.content)