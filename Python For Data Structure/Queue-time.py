# Calculate CallCenters total timing of call using queue
# general call takes average 5 minites and 
# technical person takes average 10 minites  
"""
Using pop method dequeue all the calls from the queue 
one by one and note the timing of call at the end while queue is empty count the total number of time  

"""

class CallCenter:
    def __init__(self):
        self.customer=[]
    def is_empty(self):
        return self.customer==[]
    def add(self,x) :
        self.customer.insert(0,x)
    def next(self):
        return self.customer.pop()

c=CallCenter()
while True:
    n=input()
    if n=="end":
        break
    c.add(n)
time=0
while True:
    if c.is_empty():
        break
    val=c.next()
    if val=="general":
        time+=5
    if val=="technical":
        time+=10
print(time)                               