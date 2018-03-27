#Workshop - Store Part-2
class MemberStore:

	members = []
	last_id = 1

	def add(self,member):
		# append name
		member.id = MemberStore.last_id
		MemberStore.members.append(member)
		MemberStore.last_id += 1
	
	def get_all(self):
		# to get all /members
		return MemberStore.members

	def get_by_id(self,id):
		all_members = self.get_all()

		return result

	def entity_exist(self,member):	
		result = True
		return result

	def delete(self,id):
		pass
		
class PostStore:
	posts = []

	def add(self,post):
		# append post
		self.posts.append(post)

	def get_all(self):
		# to get all /posts
		return PostStore.posts

