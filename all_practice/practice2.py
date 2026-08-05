lis=[4,-1,5,-7,8,-2,6,-6,1]
pl=[]
nl=[]
sum_pl=0
sum_nl=0
for x in lis:
    if x>0:  
        pl.append(x)
        sum_pl+=x
    else:
        nl.append(x)
        sum_nl+=x 
print("store +ve=",pl)
print("store -ve=",nl)
print("sum +ve =",sum_pl)
print("sum -ve =",sum_nl)        