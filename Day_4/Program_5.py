vote=[]
for _ in range(int(input('Enter number of vote counted in election : '))):
	vote.append(input('Enter name of candidates count: '))
voter=[]
for i in set(vote):
	voter.append([vote.count(i),i])
voter.sort()
y = voter[-1][0]
winner_is=[]
for i in voter:
	if i[0]==y:
		winner_is.append(i[1])
print('The winner of this election is :',sorted(winner_is)[0])