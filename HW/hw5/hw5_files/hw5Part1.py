import hw5util

#ask user to input a filename
filename = input("Enter the filename => ")
print(filename)
filename = filename.replace('csv','txt')
games, players, predictions = hw5util.read_predictions(filename)

#count total scores for each player
print("Player points:")
scores = []
total_scores_list = []
for n in range(len(players)):
    n_scores = []
    total_scores=0
    #different kinds of scoring 
    for i in range(len(games)):
        n_sum = 0
        #guess right of the winner
        if games[i][-1]>games[i][-2] and \
           predictions[n][i][1]>predictions[n][i][0]:
            n_sum+=2
            #guess right of the scores
            if games[i][-1]==predictions[n][i][1]:
                n_sum += 1
            if games[i][-2]==predictions[n][i][0]:
                n_sum += 1
            n_scores.append(n_sum)
            total_scores += n_sum
        #guess right of the winner
        elif games[i][-1]<games[i][-2] and \
             predictions[n][i][1]<predictions[n][i][0]: 
            n_sum+=2
            #guess right of the scores
            if games[i][-1]==predictions[n][i][1]:
                n_sum +=1
            if games[i][-2]==predictions[n][i][0]:
                n_sum +=1  
            n_scores.append(n_sum)
            total_scores += n_sum
        #guess both the winner and scores right
        elif games[i][-1]==predictions[n][i][1] and \
             games[i][-2]==predictions[n][i][0]:
            n_sum+=4
            n_scores.append(n_sum)
            total_scores += n_sum
        #guess right when it is draw
        elif games[i][-1]==games[i][-2] and \
             predictions[n][i][1]==predictions[n][i][0]: 
            n_sum+=2
            if games[i][-1]==predictions[n][i][1]:
                n_sum +=1
            if games[i][-2]==predictions[n][i][0]:
                n_sum +=1  
            n_scores.append(n_sum)
            total_scores += n_sum
        #other situations
        else:
            if games[i][-1]==predictions[n][i][1]:
                n_sum +=1
            if games[i][-2]==predictions[n][i][0]:
                n_sum +=1   
            n_scores.append(n_sum)
            total_scores += n_sum
    scores.append(n_scores) 
    total_scores_list.append(total_scores)
    
    print("{0:10}".format(players[n])+':'+"{:>4}".format(str(total_scores)))           
#find the maximum scores from all players
max_list = []
MAX = []
max_name = []
for item in total_scores_list:
    if item == max(total_scores_list):
        MAX.append(item)
    else:
        MAX.append(0)
for i in range(len(MAX)):
    if MAX[i] == total_scores_list[i]:
        max_name.append(players[i])

print()
print("Winner(s): (max points: "+str(max(MAX))+')')
for name in max_name:
    print(name)
print()
print("Game points:")

#total scores from players for each game
sum_eachgame = []
number = 0
while number<len(games):
    SUM = 0 
    for i in range(len(scores)):       
        SUM = SUM + scores[i][number]
    sum_eachgame.append(SUM)
    number+=1

hardest_list = []
for i in range(len(games)):
    print("{0:30}".format(games[i][3]+" "+"vs"+" "+games[i][4])+":"+\
          "{0:>4}".format(str(sum_eachgame[i])))
    hardest_list.append(sum_eachgame[i])

#the min score from all the scores    
print()
MIN = []
min_name = []
for item in hardest_list:
    if item == min(hardest_list):
        MIN.append(item)
    else:
        MIN.append(0)
for i in range(len(MIN)):
    if MIN[i] == hardest_list[i]:
        min_name.append(games[i][3]+" "+"vs"+" "+games[i][4])
print("Hardest game(s) (min points: "+str(min(hardest_list))+')')
for name in min_name:
    print(name)