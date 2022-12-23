import os
import numpy as np
import csv
from pytest import skip
filename = "PokemonGOData.csv"
file = open(filename,'r')
contents = file.readlines()
pokemon  = {}
topics, pokenames = [], []
c = 0
for line in contents[0:-1]:
    line = line.strip()
    lst = line.split(',')
    infoNtuples = []
    Pokemon_name = lst.pop(0)
    d = 0
    string=''
    if c ==0:
        while(d<9):
            topics.append(lst[d])
            d+=1
        skip
    if c <594:
        string = lst[0]+lst[1]
        CPstr =''
        for b in range(len(string)):
            if '"' != string[b]:
                CPstr+=string[b]      
        lst[0] = CPstr
        lst = lst[:1] + lst[2:]        
    a=0
    while(a<9 and c !=0):
        infoNtuples.append((topics[a],lst[a]))
        a+=1
    pokemon[Pokemon_name] = infoNtuples
    c+=1
    pokenames.append(Pokemon_name)
pokenames.pop(0)
pokemon.pop('Pokemon',None)
file.close()

exit_cmd = ["e","E","ex","exit","q","Q","quit"]

def askForPokemon():
    print("Enter the name of the pokemon you want the info data to")
    PokemonName_input = input()
    while(1):
        if PokemonName_input in pokenames:
            break
        else:
            print("Please enter in the correctly spelled pokemon name")
            PokemonName_input = input()
    print("Enter the pokemon CP value")
    Pokemon_CP_input = int(input())
    Max_CP_input = int(pokemon[PokemonName_input][0][1])
    output = (Pokemon_CP_input/Max_CP_input)*100
    print("The Pokemon entered is {0} percent".format(round(output,1)))
    print("IS THE NAME OF THE POKEMON THE SAME or q for QUIT")
    sameornot = input()
    if sameornot == "yes":
        return 1,PokemonName_input
    elif sameornot in exit_cmd:
        return 2,PokemonName_input
    else:
        return 0,PokemonName_input

def samePokemon(PokemonName_input):
    print("Enter the pokemon CP value")
    Pokemon_CP_input = int(input())
    Max_CP_input = int(pokemon[PokemonName_input][0][1])
    output = (Pokemon_CP_input/Max_CP_input)*100
    print("The Pokemon entered is {0} percent".format(round(output,1)))
    print("IS THE NAME OF THE POKEMON THE SAME or q for QUIT")
    sameornot = input()
    if sameornot == "yes":
        return 1
    elif sameornot in exit_cmd:
        return 2
    else:
        return 0
        
#Running LOOP
cnt = 0
while(1):
    cnt, name = askForPokemon()
    if cnt == 0:
        cnt, name = askForPokemon()
    if cnt == 1:
        cnt = samePokemon(name)
    if cnt == 2:
        break
    cnt = 0
