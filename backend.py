banddict={0:'Black',1:'Brown',2:'Red',3:'Orange',4:'Yellow',5:'Green',6:'Blue',7:'Violet',8:'Gray',9:'White'}
global q,r,n,band1,band2,band3,man
print 'Enter the value of resistor '
man=input('Enter th value of mantissa : ')
exp=raw_input('Enter th value of exponent : ')
intflag=isinstance(man,int)
print intflag
if intflag==1:
	print intflag
	if man>0 and man<10:
		q=man
		r=0
		n=0
	elif man>=10 and man<100:
		q=man/10
		r=man%10
		n=0
	elif man>=100 and man<1000:
		q=man/100
		r=((man/10)%10)
		n=1
	else:
		print 'Error'
else:
	if man>0 and man<10:
		e=man*10
		f=e/10
		q=int(f)
		g=e%10
		r=int(g)
		n=-1
	else:
		print "error"
if exp=='k':
	band1=q
	band2=r
	band3=3+n
elif exp=='m':
	band1=q
	band2=r
	band3=6+n
else:
	band1=q
	band2=r
	band3=n

print 'Band 1 =',banddict[band1]
print 'Band 2 =',banddict[band2]
print 'Band 3 =',banddict[band3]

