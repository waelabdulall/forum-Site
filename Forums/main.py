import models

member1 = models.Member("Wael Abdulaal",38)
member2 = models.Member("Khalid Mohammed", 30)

post1 = models.Post("Unix","is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, development starting in the 1970s ")
post2 = models.Post("Linux","is a family of free and open-source software operating systems built around the Linux kernel")
post3 = models.Post("macOS","is a series of graphical operating systems developed and marketed by Apple Inc. since 2001")

print member1.age
print member2.name

print post1.title
print post2.content
print post3.title," | " ,post3.content

