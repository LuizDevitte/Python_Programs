def moving_average(a,n=9):
	from numpy import cumsum
	ret = cumsum(a,dtype=float)
	ret[n:] = ret[n:] - ret[:-n]
	return ret[n-1:]/n