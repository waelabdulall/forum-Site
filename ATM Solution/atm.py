# allowed papers: 100, 50, 10, 5, and rest of request

money = 500

request = 277

''' 
Result:
	100 + 100 + 50 + 10 + 10 + 5 + 2 = 277

Output :
	give 100
	give 100
	give 50
	give 10
	give 10
	give 5
	give 2

Hint:
	while request > 0:
'''

def atm_give(request):
	
	# define the allowed papers
	allowed_papers	=	[100,50,10,5,1]
	switch 					=	0
	repeat 					=	0
	give						= []
	
	#in a loop
	#get the request to match the conditions
	while request	> 0:
		
		#get the request mod divided by the biggest allowed number to get remain
		remain	=request % allowed_papers[switch]
		if request-remain >= 5:
			result	=(request-remain)/allowed_papers[switch]
			while repeat != result:
				give.append(allowed_papers[switch])
				repeat+=1
			repeat = 0
			request	= remain
			switch	+=	1
		else:
			give.append(request)
			break
	
	print_times= len(give) 
	switch = 0
	while switch < print_times:
		print 'give',give[switch]
		switch	+= 1
		


		#check if remain equal to the same number and if not check next 

atm_give(277)
