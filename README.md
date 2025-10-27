# homework
a,b,c=map(int, input('enter three numbers a,b,c ').split())
print(a+b*c) #* is above + in precedence so b*c is calculated first, then added with a
print((a+b)*c) #() is above* in precedence so (a+b) is calculated first, then multiplied with c
print(a*b/c) #due to left toright associativity, a*b is calculated first, then divided by c
print(a+b-c*a/b)
'''c*a is calculated first as it is above + and - in
precedence, then divided by b due to associtivity, then
product is subtracted from sum a+b'''
