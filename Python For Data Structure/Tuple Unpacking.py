
import math

points=[
    (12,55),(880,123),(64,64),(190,1024),(77,33),(42,11),(0,90)
]
    
dist=[]
for (x,y)in points:
    i=math.sqrt((x**2)+(y**2))
    dist.append(i)
print(min(dist))    
