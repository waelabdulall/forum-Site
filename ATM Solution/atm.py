# allowed papers: 100, 50, 10, 5, and rest of request

money = 500

request = 277

def atm_give(request):
	
	allowed_papers	=	[100,50,10,5,1]
	switch 					=	0
	repeat 					=	0
	give						= []
	
	if request <= money:
		
		while request	> 0:
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
	else:
		print 'Credit is NOT Enough '
		


atm_give(501)
