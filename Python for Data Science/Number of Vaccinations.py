# Find the mean number of vaccinations of given data 
# here calculation is (0*5 + 1*8 + 2*4 + 3*3)/20 
# Find the variation of the given data 
import numpy as np
vac_nums = [0,0,0,0,0,
            1,1,1,1,1,1,1,1,
            2,2,2,2,
            3,3,3
            ]
arr=np.array(vac_nums)
# print((8+8+9)/20)
mean=np.sum(arr)/arr.size
variation=np.sum((arr-mean)**2)/arr.size
print(variation)

