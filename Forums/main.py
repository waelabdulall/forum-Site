#Workshop - Store Part-2
from models import Member,Post
from stores import MemberStore , PostStore

member1 = Member("Wael Abdulaal",38)
member2 = Member("Khalid Mohammed", 30)
member3 = Member("Nawwar Wael", 1)

post1 = Post("Unix","Is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, development starting in the 1970s ")
post2 = Post("Linux","Is a family of free and open-source software operating systems built around the Linux kernel")
post3 = Post("macOS","Is a series of graphical operating systems developed and marketed by Apple Inc. since 2001")


member_store = MemberStore()
member_store.add(member1)
member_store.add(member2)

# print member_store.get_all()

post_store = PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

# print post_store.get_all()

# for each in member_store.members:
# 	print each

# print

# for each in post_store.posts:
# 	print each

# for each in member_store.get_all():
# 	print each

# print

# for each in post_store.get_all():
# 	print each

#print member_store.get_by_id(3)

print member_store.entity_exist(member1)