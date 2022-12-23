import os
import numpy as np
import random as r

def get_path(filename):
    my_dir = os.getcwd()
    file_path = my_dir + filename
    return file_path

class Friend_setup:
    def __init__(self):
        self.dataDict = {}
        self.titles, self.data = [], []
        self.cat = ''
        self.mood_score = 50
        self.mood = ''

    def get_dic(self,file_path):
        file = open(get_path(file_path),'r')
        contents = file.readlines()
        for line in contents:
            line = line.strip()
            lst = line.split('\t')
            for string in range(len(lst)):
                if lst[string] == '':
                    lst.remove(lst[string])
            if len(lst) == 1:
                self.titles.append(lst)
            else:
                self.data.append(lst)
        for i in range(len(self.titles)):
            self.dataDict[self.titles[i][0]] = self.data[i]
        return self.dataDict

    def Mood(self):
        if self.mood == "happy":
            self.mood_score += 1
        elif self.mood == "sad":
            self.mood -= 2
        elif self.mood == "angry":
            self.mood_score -= 5
        elif self.mood == "bored":
            self.mood_score += 0
        elif self.mood == "pissed":
            self.mood_score -=10
            
        pass

    def SayingHi(self):
        intro = self.dataDict['Introduction_Words']
        rn = r.randint(0, len(intro)-1)
        return intro[rn] #+ ", I'm a contruct of my master \"Joseph Thompson\""

    def Category(self):
        put = input("So are you a student, working adult, or here to talk\nAnswer with student, working adult, here to talk\n")
        self.cat += put
        return self.cat



friendSet =Friend_setup()
dict = friendSet.get_dic("/BeginnerDataForClass.txt")
print(friendSet.SayingHi())

# string = friendSet.Category()



