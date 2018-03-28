#Workshop - Filtering
class MemberStore:

	members = []
	last_id = 1

	def add(self,member):
		member.id = MemberStore.last_id
		MemberStore.members.append(member)
		MemberStore.last_id += 1
	
	def get_all(self):
		return MemberStore.members

	# def get_by_id(self,id):

	# 	all_members = self.get_all()
	# 	for result in all_members:
	# 		if result.id ==id:
	# 			return result

	def get_by_id(self, id):
		all_members = self.get_all()

		result = None

		for member in all_members:
			if member.id == id:
				result = member
				break

		return result

	# def entity_exist(self,member):
	# 	if member == self.get_by_id(member.id):
	# 		result = True
	# 		return result

	def entity_exists(self, member):

		result = True
		if self.get_by_id(member.id) is None:
			result = False
		return result

	def get_by_name(self,name):
		pass
		# all_members= self.get_all()

		# for member in all_members:



		# return result

	def delete(self,id):
		member = self.get_by_id(id)
		MemberStore.members.remove(member)


	def update(self,member):
		pass


		
class PostStore:
	posts = []

	def add(self,post):
		self.posts.append(post)

	def get_all(self):
		return PostStore.posts

