# i DATI    iniziano dalla linea 297
#           terminano alla linea 639905
# STRUTTURA:
# New  Distribution  Votes  Rank  Title

# REPORT FORMAT
# =============

# In this list, movies have been rated on a scale of 1 to 10, 10 being good and 1 being bad.
# For each movie, the total number of votes, the average rating, and the vote distribution are shown.
# New movies are indicated by a "*" before their entry.
# The vote distribution uses a single character to represent the percentage of votes for each ranking.
# The following characters codes can appear:
#      "." no votes cast        "3" 30-39% of the votes  "7" 70-79% of the votes
#      "0"  1-9%  of the votes  "4" 40-49% of the votes  "8" 80-89% of the votes
#      "1" 10-19% of the votes  "5" 50-59% of the votes  "9" 90-99% of the votes
#      "2" 20-29% of the votes  "6" 60-69% of the votes  "*" 100%   of the votes

# The formula used to calculate the top 250 movies is:
#   weighted rank = (v/(v+k))*X + (k/(v+k))*C
#   where:
#     X = average for the movie (mean)
#     v = number of votes for the movie
#     k = minimum votes required to be listed in the top 250 (currently 25000)
#     C = the mean vote across the whole report (currently 6.90)

fileRatingsName = "ratings.list"

with open(fileRatingsName, 'r') as fileRatings:
    linesValues = fileRatings.readlines()
fileRatings.close

linesNumber = len(linesValues)

# for line in range(linesNumber):
#     print linesValues[line]

# line = 840
line = 1189
tokens = linesValues[line].split()

print "\t\tNew  Distribution  Votes  Rank  Title"
print "tokens = ", tokens

print "->", linesValues[line][6:16], "|"  # nuovo?
print "->", linesValues[line][17:24], "|"  # voti
print "->", linesValues[line][25:30], "|"  # valutazione
print "->", linesValues[line][31:], "|"  # titolo

voteList = []
rankList = []
titleList = []
# righe sotto generano troppi token, piu' campi del necessario
# for line in range(296, 639903):
#     tokens = linesValues[line].split()
#     voteList.append(tokens[1])
#     rankList.append(tokens[2])
#     titleList.append(tokens[3])

for line in range(296, 639903):
    voteList.append(linesValues[line][17:24])
    rankList.append(linesValues[line][25:30])
    titleList.append(linesValues[line][31:])

votoDaFile = rankList[0]
print votoDaFile
print type(votoDaFile)
valoreVoto = float(rankList[0])
print type(valoreVoto)
print valoreVoto

voteList = []
rankList = []
titleList = []
for line in range(296, 639903):
    voteList.append(float(linesValues[line][17:24]))
    rankList.append(float(linesValues[line][25:30]))
    titleList.append(linesValues[line][31:])


filmsNumber = len(voteList)

print filmsNumber

# print "------------------------"
# for i in range(filmsNumber):
#     print i, "\t",voteList[i], "\t", rankList[i], "\t", titleList[i]
# print "------------------------"

# meanVote:
averageVote = 0
for film in range(filmsNumber):
    averageVote = averageVote + rankList[film]

averageVote = averageVote / filmsNumber
print "voto medio = ", averageVote

# minimum votes required to be listed in the top 250 (currently 25000)
# devo copiare la lista delle valutazioni perche nel riordinarla perdo
# coerenza con le altre 2
tmpList = list(voteList)
print "id(voteList) = ", id(voteList)
print "id(tmpList)  = ", id(tmpList)
# print tmpList[1568], voteList[1568]

# ordiniamo la lista per estrarre il valore del voto minimo per top 250
tmpList.sort(reverse=True)
# for film in range(0,250):
#     print film, tmpList[film]
minVote = tmpList[249]  # 0 based


print "-------- imdbRanking -----------"
imdbRankingList = []
for film in range(filmsNumber):
    if (voteList[film] >= minVote):
        # imdbRanking = (voteList[film] * rankList[film] + minVote * averageVote) / (voteList[film] + minVote)
        imdbRanking = ((voteList[film] * rankList[film]) / (voteList[film] + minVote)) + (
            (minVote * averageVote) / (voteList[film] + minVote))
        imdbRankingList.append([film, imdbRanking])
        # print imdbRankingList[film]

imdbFilmsInList = len(imdbRankingList)
imdbRankingList.sort(key=lambda inListFilm: inListFilm[1], reverse=True)
for film in range(imdbFilmsInList):
    print film + 1, "\t", imdbRankingList[film][1], "\t", titleList[imdbRankingList[film][0]]
