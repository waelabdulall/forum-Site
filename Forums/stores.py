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

	def entity_exists(self,instance):
		result =False
		if instance is not None:
			if instance is self.get_by_id(instance.id):
				result = True

	def add(self,item_instance):
		instance.id = self._last_id
		self._data_provider.append(item_instance)
		self._last_id +=1

	def update(self,updated_instance):
		instances = self.get_all
		for index, instance in enumerate(instances):
			if instance.id == updated_instance:
				instance[index] = updated_instance

	def delete(self,id):
		instance = self.get_all
		if instance is not None:
			self._data_provider.remove(instance)


class MemberStore(BaseStore):

	members = []
	last_id = 1

	def __init__(self):
		super().__init__(self.member,self.last_id)


	def get_by_name(self,name):
		return member for member in self.get_all() if member.name == name :
		
	def get_membr_with_post(self,post):
		members = self.get_all()
		for member, post in itertools.product(member,post):
			if post.member_id == member.id:
				member.post.append(post)
		return members

class PostStore(BaseStore):
	posts = []

	def add(self,post):
		self.posts.append(post)

	def get_all(self):
		return PostStore.posts

