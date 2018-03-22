import models

member1 = models.Member("Wael Abdulaal",38)
member2 = models.Member("Khalid Mohammed", 30)

topic1 = models.Post("Unix","is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, development starting in the 1970s ")
topic2 = models.Post("Linux","is a family of free and open-source software operating systems built around the Linux kernel")


print member1.age
print member2.name

print topic1.title
print topic2.content

