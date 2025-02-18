def TowerOfHanoi(n , left, right, center):
	if n==1:
		print ("Move disk 1 from rod",left,"to rod",right)
		return
	TowerOfHanoi(n-1, left, center, right)
	print ("Move disk",n,"from rod",left,"to rod",right)
	TowerOfHanoi(n-1, center, right, left)

n = 4
TowerOfHanoi(n,'A','B','C')