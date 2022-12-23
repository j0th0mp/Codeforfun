f = open("BeginnerDataForClass1.txt", "w")

hello ={
1:"Hello",
2:"Howdy",
3:"hi",
4:"Howdy-doody",
5:"Wassup",
6:"What's kicking",
7:"Ahoy",
8:"What's cracking",
9:"Hello-hello",
10:"Yo",
11:"Aloha",
12:"Hello there",
13:"Hiya",
14:"Greetings",
15:"Hola",
16:"Bonjour",
17:"Ciao"
}
for key in hello:
    f.write(hello[key]+"\t")
f.write("\n")
GettoKnow = {
1:"How do you like to spend your time outside of work or school?",
2:"Do you have any hobbies?",
3:"Do you collect anything?",
4:"Are you an early bird or a night owl?",
5:"How do you like to end your day?",
6:"What kinds of activities drain you?",
7:"What kinds of activities energize you?",
8:"What's one thing youre learning now or learned recently?",
9:"What's something you saw recently that made you smile?",
10:"What's something you saw recently that made you laugh?",
11:"What's something you've done, but you'll never do again?",
12:"What are you passionate about?",
13:"What's your guilty pleasure?",
14:"When you were a kid, what did you want to be when you grew up?",
15:"What's your ideal way to spend your weekends?",
16:"Are you reading anything interesting right now?", 
17:"Are you bingeing any shows?",
18:"Do you have any pets?"
}

for key in GettoKnow:
    f.write(GettoKnow[key]+"\t")
f.write("\n")
FavQuest = {
0:"Are you a dog person or a cat person (or neither)?",
1:"What's your favorite place to eat around here?",
2:"What's your favorite snack?",
3:"What's your favorite TV show or one you'd never get tired of rewatching?",
4:"Which season is your favorite?",
5:"Who's your favorite musical artist?",
6:"What's your favorite tradition (holiday or otherwise)?",
7:"What's your favorite comfort media (book, show, movie, music, or anything else)?",
8:"What's your favorite sport to watch? How about to play?",
9:"What's your favorite game to play?"
}
for key in FavQuest:
    f.write(FavQuest[key]+"\t")
f.write("\n")

studQuest ={
1:"What's your favorite subject?",
2:"What do you like to do during recess?",
3:"What's your favorite class you've ever taken?",
4:"Who's the best teacher you ever had?",
5:"What's your favorite topic to learn about?",
6:"What's your least favorite class?",
7:"Are you in any extracurricular activities?",
8:"If you could create any school club you wanted and knew people would join, what would it be?",
9:"What class do you wish this school had?",
10:"Why did you choose your major?",
11:"What drew you to this school?",
12:"What's your favorite project you ever did for a class?"
}

for key in studQuest:
    f.write(studQuest[key]+"\t")
f.write("\n")

f.close()
