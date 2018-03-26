#Workshop - Store Part-2
class MemberStore:

	members = []

	def add(self,member):
		# append name
		self.members.append(member)
	
	def get_all(self):
		# to get all /members
		return MemberStore.members


class PostStore:

	posts = []

	def add(self,post):
		# append post
		self.posts.append(post)
	
	def get_all(self):
		# to get all /posts
		return PostStore.posts

