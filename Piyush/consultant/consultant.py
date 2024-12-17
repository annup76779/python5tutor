# all the imports 
import pandas as pd

# reading the CSV
consultants = pd.read_csv('consultants.csv').to_dict("records")

# get the weight of skills of the consultants
def get_w(k):
    return sum(list(k.values())[1:])

# categories the consultants based on their skills set weight
zero = list(filter(lambda x: get_w(x) == 0, consultants)) # the consultants with 0 skills
single = list(filter(lambda x: get_w(x) == 1, consultants)) # the consultants with 1 skills
two = list(filter(lambda x: get_w(x) == 2, consultants)) # the consultants with 2 skills
three = list(filter(lambda x: get_w(x) == 3, consultants)) # the consultants with 3 skills
four = list(filter(lambda x: get_w(x) == 4, consultants)) # the consultants with 4 skills

# making a list of all the consultants with their skill set weight at the 
# exact index in the list as it is their weight
consultants_by_skill_weight = [zero, single, two, three, four]

# find the category with least number of 
min_ = min(consultants_by_skill_weight, key = lambda x: len(x))

def set_in_loop_min(consultants_by_skill_weight):
    """
        Function to set the minimum counted consultants_by_skill_weight
    """
    # reference to global variables min_
    global min_
    
    # min_ is only changed when there is min_ length == 0
    if len(min_) == 0:
        excluding_index = [] # list to hold the index of all the below min lists

        # remove the current min_ objects from the list
        while min_ in consultants_by_skill_weight:
            # putting the index of current min_ in the list
            excluding_index.append(consultants_by_skill_weight.index(min_))
            consultants_by_skill_weight.remove(min_)

        # finding the new min_ after removing the previous min_
        min_ = min(consultants_by_skill_weight, key = lambda x: len(x))

        # now placing the new min_ to the indexes of older min_
        for index in excluding_index:
            consultants_by_skill_weight.insert(index, min_)


# teams list
# teams are going to be the list of dictionary
teams = []

# loop for 20 teams
for i in range(20):
    # just in can case any index error orccures
    try:
        # setting the new min_ if needed
        set_in_loop_min(consultants_by_skill_weight)

        # creating  new team
        team = []
        # loop for 5 members entry
        for j in range(5):
            # rechecking if the min_ is needed to be updated
            set_in_loop_min(consultants_by_skill_weight)
            # adding the new member to the list
            team.append(
                consultants_by_skill_weight[j].pop()
            )
        # appending the team to the list of teams
        teams.append(team)
    except IndexError:
        break

# total number of teams
print("Total number of teams:", len(teams))

# pritty printing the teams with the list of their consultants
for i, consultants in enumerate(teams):
    print("Team", i)
    for consultant in consultants:
        print("\t",consultant)

# NOTE: since the no. of consultants with skills are not balanced thus the teams are also not well balanced but
# balanced to a good extend
# most of the teams are lacking analytics skills in them 