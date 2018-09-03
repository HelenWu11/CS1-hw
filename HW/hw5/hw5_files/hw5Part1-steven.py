import hw5util
file = input("Enter the filename => ")
print(file)
if __name__ == "__main__":
    games, players, predictions = hw5util.read_predictions(file) 
    
#The list used to store player's score
player_point = []
i_point = []
sum_point = []
point = 0
print("Player points:") # general information
for p in range(0,len(players)):
    #determine the amount of players
    for i in range(0,len(games)):
        #To determine the result of the matches first and then the details of it
        if games[i][-2] > games[i][-1] and predictions[p][i][-2] > predictions[p][i][-1]:
            point += 2 
            #two points for correctness
        elif games[i][-2] == games[i][-1] and predictions[p][i][-2] == predictions[p][i][-1]:
            point += 2
        elif games[i][-2] < games[i][-1] and predictions[p][i][-2] < predictions[p][i][-1]:
            point += 2
        
        if games[i][-1] == predictions[p][i][-1]:
            point += 1
        if games[i][-2] == predictions[p][i][-2]:
            point += 1
        
        i_point.append(point)
        point = 0
        #return point to 0, prepare for the next loop
    print(players[p],":","\t",sum(i_point))
    sum_point.append(sum(i_point))
    player_point.append(i_point)
    i_point = []
print()
print("Winner(s): (max points: {:d})".format(max(sum_point)))
for i in range(0, len(players)):
    if sum(player_point[i]) == max(sum_point):
        print(players[i])
# print the name of maximum point
print()
isum = []
sum_p = 0
#add the specific term of the list
for p in range(0, len(games)):
    for i in range(0, len(players)):
        sum_p += player_point[i][p]
    isum.append(sum_p)
    sum_p = 0
print("Game points:")
for i in range(0,len(games)):
    print(games[i][3], "vs", games[i][4], ":","\t", isum[i])
print()
print("Hardest game(s) (min points: {:d})".format(min(isum)))

for i in range(0, len(games)):
    if isum[i] == min(isum):
        print(games[i][3], "vs", games[i][4])