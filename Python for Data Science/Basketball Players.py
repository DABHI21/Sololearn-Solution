# The given code includes a list of heights for various basketball players.
# You need to calculate and output how many players are in the range of one standard deviation from the mean.

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

mean=sum(players)/len(players)
sd=(sum((i-mean)**2 for i in players)/len(players))**0.5

lb=mean-sd
ub=mean+sd

players_count=len([i for i in players if lb<=i<=ub])
print(players_count)


