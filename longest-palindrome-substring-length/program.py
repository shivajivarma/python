def maxPalindromeSubStringLen(str):
	leng = 0
	ext = 0
	while(len(str)>0):
		if(str.count(str[0])%2==0):
			leng = leng + (str.count(str[0]))
		else:
			leng = leng + (str.count(str[0])) - 1
			ext = 1
		str = str.replace(str[0],"")
	return leng + ext
 
if __name__=="__main__":
	print("Enter a string: ", end="")
	paragraph = input()
	print("Length of longest palidrome ::", maxPalindromeSubStringLen(paragraph))
