# Q: find out sum of 1+2+.....+10 using python programming?

num =  "1+2+...+10"

splitNum = num.split("+")
LastNum = int(splitNum[-1])
sum_of_n_num = LastNum*(LastNum+1)/2
print(sum_of_n_num)


