import json
if __name__ == "__main__":
    movies = json.loads(open("movies.json").read())
    
    ratings = json.loads(open("ratings.json").read())

#ask user for input
minyear = int(input("Min year => "))
print(minyear)
maxyear = int(input("Max year => "))
print(maxyear)
w1 = input("Weight for IMDB => ")
print(w1)
w2 = input("Weight for Twitter => ")
print(w2)

#list that use to store movies that achieve the requirements
movie_list = []
#ratings of movies with the provided function
crating = 0

for n in movies:
    #exclude movies that are in 'movies' but not in 'ratings'
    if n not in ratings:
        continue
    else:
        #exclude movies that have less than three ratings
        if len(ratings[n])<3:
            continue
        #find movies that are between years the user input
        if movies[n]['movie_year'] >= minyear and movies[n]['movie_year'] <= maxyear:
            imdb_rating = movies[n]['rating']
            atr = 0 #average_twitter_rating
            sumtr = 0 #sum of ratings
            count = 0 #number of ratings
            for i in ratings[n]:
                sumtr += i
                count += 1
            atr = sumtr/count
            crating = (float(w1)* imdb_rating + float(w2) * atr)/(float(w1)+float(w2))
            movie_list.append((crating,n))

movie_list.sort()
movie_list.reverse() 
#find the 10 movies with 10 highest rates
print("10 Highest rated movies")
for n in range(10):
    print(movies[movie_list[n][1]]['name']+' '+\
          '('+str(movies[movie_list[n][1]]['movie_year'])+')')
    print(' '*10+"Rating: {:.2f}".format(movie_list[n][0]))
    print(' '*10+'Genres: '+', '.join(movies[movie_list[n][1]]['genre']))
    
print()
movie_list.reverse()
#find the 10 movies with 10 lowest rates
print("10 lowest rated movies")
for n in range(10):
    print(movies[movie_list[n][1]]['name']+' '+\
          '('+str(movies[movie_list[n][1]]['movie_year'])+')')
    print(' '*10+"Rating: {:.2f}".format(movie_list[n][0]))
    print(' '*10+'Genres: '+', '.join(movies[movie_list[n][1]]['genre']))