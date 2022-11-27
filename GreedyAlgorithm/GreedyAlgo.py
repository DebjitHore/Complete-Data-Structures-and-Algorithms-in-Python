#ActivitySelectionProblem

#maximum number of activities that can be performed by a single person, assuming one activity at a time

activities= [[0, 6], [3,4], [1,2], [5,8], [5,7], [8,9]]


def selectMaxActivities(activities):
	activities.sort(key= lambda x: x[1])
	i=0
	firstActivity= activities[i]
	finalActivityList=[]
	finalActivityList.append(firstActivity)
	for j in range(1, len(activities)):
		if activities[j][0]>activities[i][1]:
			finalActivityList.append(activities[j])
			i=j
		else:
			continue
	return (len(finalActivityList))



print(selectMaxActivities(activities))

#CoinChangeProblem

#minimum number of coins needed to in different denominations to reach a certain amount of money

def minimumCoins(amount, coins):
	N= amount
	coins.sort()
	index= len(coins)-1
	purse=[]
	while True:
		coinValue= coins[index]
		if N>=coinValue:
			N-=coinValue
			purse.append(coinValue)
		elif N< coinValue and index>0:
			index-=1
		elif N==0:
			break
	return (purse)

coins= [1,2,5,20,50, 100]
print(minimumCoins(1001, coins))

#FractionalKnapsackProblem
#Limited weighted knapsack, add items in knapsack to maximise value within weight constraints
#maximum density values are added first
class Item:
	def __init__(self, weight, value):
		self.weight = weight
		self.value= value
		self.ratio= value/weight


def knapSack(items, capacity):
	items.sort(key=lambda x: x.ratio, reverse=True)
	usedCapacity=0
	totalValue=0
	for i in items:
		if usedCapacity+i.weight <=capacity:
			usedCapacity+=i.weight
			totalValue+=i.value
		else:
			unusedWeight=capacity-usedCapacity
			value=i.ratio*unusedWeight
			totalValue+=value
		if usedCapacity==capacity:
			break
			
	print("Total value obtained: "+str(totalValue))


item1= Item(20,100)
item2= Item(30,120)
item3= Item(10,60)

cList= [item1, item2, item3]


knapSack(cList, 50)




	 