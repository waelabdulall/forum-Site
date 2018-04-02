#Workshop - Inheritance
class BaseStore():

	def __init__(self,data_provider,last_id):
		self._data_provider = data_provider
		self._last_id = last_id

	def get_all(self):
		return self._data_provider

	def get_by_id(self, id):
		for instance in self.get_all():
			if instance.id == id:
				return instance

	def add(self,item_instance):
		item_instance.id = self._last_id
		self._data_provider.append(item_instance)
		self._last_id +=1

class MemberStore(BaseStore):

	members = []
	last_id = 1

	def add(self,member):
		member.id = MemberStore.last_id
		MemberStore.members.append(member)
		MemberStore.last_id += 1
	
	def get_all(self):
		return MemberStore.members


	def get_by_id(self, id):
		all_members = self.get_all()

		result = None

		for member in all_members:
			if member.id == id:
				result = member
				break

		return result


	def entity_exists(self, member):

		result = True
		if self.get_by_id(member.id) is None:
			result = False
		return result


	def get_by_name(self,name):
		all_members= self.get_all()
		for member in all_members:
			if member.name == name:
				yield member


	def delete(self,id):
		member = self.get_by_id(id)
		MemberStore.members.remove(member)


	def update(self,member):
		
		all_members = self.get_all()
		for i, each in enumerate(all_members):
			if each.id == member.id:
				all_members[i] = member
				break
				

		
class PostStore(BaseStore):
	posts = []

	def add(self,post):
		self.posts.append(post)

	def get_all(self):
		return PostStore.posts

