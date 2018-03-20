# allowed papers: 100, 50, 10, 5, and rest of request

money = 500

request = 277


def atm_give(request):
	# defining needed variables
	allowed_papers	=	[100,50,10,5,1]
	switch 			=	0
	repeat 			=	0
	give			= 	[]
	# checking the amount availability
	if request <= money:
		# a loop for processing the request
		while request > 0:
			remain = request % allowed_papers[switch]
			# check if the remain equal the result to move to check next paper
			if remain == request:
				switch +=1
			else:
				# if not will check if it is less than the 5 paper
				if (request-remain) >= 5:
					result = (request-remain)/allowed_papers[switch]
					# a loop to add the remain papers individually
					while repeat != result:
						give.append(allowed_papers[switch])
						repeat += 1
					request	= remain
					repeat = 0
					switch += 1
				# if less than 5 it will add the rmain to the give
				else:
					give.append(request)
					break
		# defining needed variables for print
		print_times= len(give)
		switch = 0
		# a loop for printing result
		while switch < print_times:
			print 'give',give[switch]
			switch	+= 1
	# if the amount is not available
	else:
		print 'Credit is NOT Enough '



atm_give(request)
