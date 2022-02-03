# Student Name
# Student Number
# Section

import math

#Fill in all functions according to descriptions
#You may add additional functions if you need to

#This function is for your parametric modelling answer
def garden_cost(r1, r2, g, h, angle, gg, gf, numCT, numDT, zoneCost):
  #delete the line below to complete
  pass

def add_garden(gardenDictionary):
  print('Input the following information separated by the enter key:\nGarden ID, Garden Name, Radius of Pond, Radius of Concave, Gate Length, Hypothenuse of Triangle, Angle of Triangle, Percentage of Grass, Percentage of Flowerbeds, Number of Coniferous Trees, Number of Deciduous Trees')
  #Fill in rest of code

def export_gardens(gardenDictionary, exportFileName):
  #delete the line below to complete
  pass

def print_gardens(gardenDictionary):
  for key in gardenDictionary:
    print(key, ":", gardenDictionary[key])

def save_gardens(gardenDictionary, saveFileName):
  #delete the line below to complete
  pass
  
def remove_garden(gardenDictionary, gardenIDRemove):
  #delete the line below to complete
  pass


gardenDictionary = dict()

#Write code to read in dictionary

userSelect = ''

while userSelect != 'X':
  print('Please input a selection based on the table below')
  print('A: Add a Garden')
  print('E: Export Garden Info')
  print('P: Print Gardens Info to Terminal')
  print('R: Remove a Garden')
  print('S: Save Garden Info')
  print('X: Exit the Program')

  userSelect = input()

  if userSelect == 'A':
    add_garden(gardenDictionary)
  elif userSelect == 'E':
    print('Please name of file to export to:')
    exportFileName = input()
    export_gardens(gardenDictionary, exportFileName)
  elif userSelect == 'P':
    print_gardens(gardenDictionary)
  elif userSelect == 'R':
    print('Please input Garden ID to remove:')
    gardenIDRemove = input()
    remove_garden(gardenDictionary, gardenIDRemove)
  elif userSelect == 'S':
    print('Please name of file to save to:')
    saveFileName = input()
    save_gardens(gardenDictionary, saveFileName)

