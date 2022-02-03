# Programming Exam

**Released on** Wednesday, December 1

**Due on** Saturday, December 11 at noon

**Modules Covered:** All Topics in the Course

## Preparation Steps:

- Watch all modules
- Review assignments and labs

## Submission: 

This final assignment is to be completed individually. 

Only one person should submit the code by pushing the code on GitHub. Make sure that every submitted file has a comment at the top with your name, section and student number. 

## Additional: 

Only use the programming skills that you have learned in modules for this assignment. While there sometimes may exist solutions that are “better” through using other skills, we ask that you only use what you have been taught in the modules. We must make sure that you understand the taught material for full marks. 

 
## Overview:

Rin Morrison is a famous gardener who is well known for her artistic gardens spread across Canada. For Summer 2022, the government of Canada wishes to hire her to plant gardens across Canada for spectators to freely view. For this project to go ahead, Rin Morrison hires you as a programmer to create two programs that makes the cost management of the gardens easier for her. 

As part of your final exam, you must help her to create two Python programs that fulfill the various requirements she needs for these gardens. The first program will load in an input txt file of the current gardens in Canada and allows a textual user interface to interact with the data. The second program finds the optimum solution to have the lowest cost to upkeep the gardens. More information about these programs can be found below.

## Parametric Modelling:
Before developing either of the programs, you must first solve a parametric modelling question to relate the given variables for each garden to the general cost of upkeep per day. Each garden is the same shape; however, the measurements of the gardens vary.
<img width="762" alt="Screen Shot 2021-06-30 at 3 03 23 PM" src="https://user-images.githubusercontent.com/77299347/124010139-d5d85f80-d9b4-11eb-9e17-9bcdb4de9f78.png">

The daily cost of upkeep as requested by local hired gardeners relates to the amount of water needed to water the garden. There are four components that make up amount out water used daily:    
<img width="577" alt="Screen Shot 2021-06-30 at 3 04 03 PM" src="https://user-images.githubusercontent.com/77299347/124010166-dffa5e00-d9b4-11eb-8ac5-61f3aa6b1450.png">

These 4 components are added together and multiplied by a zone cost (for this scenario it can be a constant of $0.55) to calculate the final cost of the garden.         
<img width="717" alt="Screen Shot 2021-06-30 at 3 04 10 PM" src="https://user-images.githubusercontent.com/77299347/124010205-ec7eb680-d9b4-11eb-9705-2e63c1a68ab3.png">

For one garden in particular, the measurements given are: theta = 30°, h = 30m, g = 20m, r<sub>1</sub> = 5m, and r<sub>2</sub> = 12.5m. The garden is made up of G<sub>g</sub> = .3 (30%) grass and G<sub>f</sub> = .55 (55%) flowerbeds., where G<sub>g</sub> and G<sub>f</sub> are the fractions of the garden area covered by each. There are 3 coniferous trees (T<sub>C</sub>) and 2 deciduous (T<sub>D</sub>). 

Based on a zone cost of $0.55, the garden described above would have a cost of $153.30.

Note: G<sub>g</sub> and G<sub>f</sub> don’t need to add up to 100% because some sections of the garden are covered by the trees or stone pathways.

Hints:
- When you draw your picture to solve this problem, you may use the picture given above, but label it with more information. 
- Remember that the area of the grass/flowerbeds is based off a percentage of the entire garden area. This means you will need to find a way to calculate the area of the garden first.
- May be easier to simplify the final equation

## Program 1:

### Step 1: Setting up the Dictionary

The first program should begin by reading a dictionary from a .txt file (Gardens.txt and should be given with the exam download) where the Garden IDs are the keys, and the other information is all saved as the value. The values within the .txt file resemble the columns in a .csv file as they are delimited by commas and each row represents a single garden. The columns are as follows:

    Garden Name, Radius of Pond, Radius of Convex, Gate Length, Hypotenuse of Triangle, Angle of Triangle, Percentage of Grass, Percentage of Flowerbeds, Number of Coniferous Trees, Number of Deciduous Trees

Each Garden ID is represented as G####XX where the #### is a number and XX represents one of the Canadian provinces/territories:

| Province/Territory      | Abbreviation | Zone |
| ----------- | ----------- | ----------- |
|Newfoundland and Labrador|	NL|	4|
|Prince Edward Island|	PE|	4|
|Nova Scotia|	NS|	4|
|New Brunswick|	NB|	4|
|Quebec|	QC|	3|
|Ontario|	ON|	3|
|Manitoba|	MB|	3|
|Saskatchewan|	SK|	2|
|Alberta|	AB|	2|
|British Columbia|	BC|	2|
|Yukon|	YT|	1|
|Northwest Territories|	NT|	1|
|Nunavut|	NU|	1|

Example: G0001NB is a garden located in New Brunswick.

All angle data input into the program will be in degrees. This means you may need to convert to radians depending on which function you wish to use. 

In the values for each key (garden), add the Zone that each garden is located in.

Calculate the daily cost of each garden and store it as another value in each key (garden). This should be using the function you created by parametric modelling. You will need to update your function to allow for the Zone Cost to be passed in as a parameter. Zone Costs should be determined based on the table below:

| Zone      | Zone Cost |
| --------- | ----------- |
| 1      | $0.55       |
| 2   | $0.70        |
| 3   | $0.90      |
| 4   | $1.20       |



By the end of this part your dictionary should story data as the following:

    Key = Garden ID

    Values: [Garden Title, Radius of Pond, Radius of Convex, Gate Length, Hypotenuse of Triangle, Angle of Triangle, Percentage of Grass, Percentage of Flowerbeds, Number of Coniferous Trees, Number of Deciduous Trees, Zone Number, Daily Cost]


### Step 2: The User Interface
After loading in all the data into a dictionary, the program should enter an input loop that will allow the user to select and perform an action of the data given. The loop is already created here, and you must not change any of the lines of code given. (You may add lines of code in between, but the given lines of code themselves cannot be changed). Your job is to write the functions used. More detail on each of these functions can be found below:

#### Step 2.1: Adding a Garden
This function takes the dictionary in as a parameter and asks the user to input all the data needed: 
Garden ID, Garden Name, Radius of Pond, Radius of Convex, Gate Length, Hypotenuse of Triangle, Angle of Triangle, Percentage of Grass, Percentage of Flowerbeds, Number of Coniferous Trees, Number of Deciduous Trees

This data should be input as a newline delimited list. You can output one message as the prompt of input. You do not need to prompt the user for each data point, assume they already know the order of input. The function will then add this Garden to the dictionary as well as its zone and its daily cost. 

![Add a Garden](https://user-images.githubusercontent.com/1709150/144321150-3db63ded-649a-4426-a904-2050f7d7ba89.png)

![Print Gardens](https://user-images.githubusercontent.com/1709150/144748973-a79a7b60-f290-422b-ad8c-e5817e57d3d7.png)

#### Step 2.2: Export Gardens
This function takes the dictionary and the name of a file the user wishes to export the gardens to in as parameters. The function then exports only specific the contents of the dictionary to another .txt file by the passed in name. The only 3 values that need to be saved to the new .txt file are: Garden ID, Garden Name, and Daily Cost. Each row should resemble:
	
    Garden ID,Garden Name,Daily Cost,
	
Pay close attention that it is saved as a comma delimited list and not just a printed key and list (e.g., you shouldn’t just save them like -  ```G0001NT: [‘Yellowknife Plot’, 325.3554])```.  

![Export](https://user-images.githubusercontent.com/1709150/144321650-8856ba20-45c6-4a33-99e8-333b270cd8af.png)


#### Step 2.3: Save Gardens
This function takes the dictionary and the name of a file the user wishes to save the gardens to in as parameters. The function then saves only all the contents of the dictionary to another .txt file by the passed in name. Each row should resemble:
	
    Garden ID,Garden Title,Radius of Pond,Radius of Concave,Gate Length, Hypothenuse of Triangle,Angle of Triangle,Percentage of Grass,Percentage of Flowerbeds,Number of Coniferous Trees,Number of Deciduous Trees,Zone Number,Daily Cost

Pay close attention that it is saved as a comma delimited list and not just a printed key and list (e.g., you shouldn’t just save them like - ```G0001NT: [‘Yellowknife Plot’, 62.5, 5.0 ... ])```.

Hint: To see if this function worked properly, you could rerun your program with the saved file as the input file.   

![Save](https://user-images.githubusercontent.com/1709150/144321716-1389057a-6de1-40cf-baeb-ba6ac462ffe4.png)
 

#### Step 2.4: Remove a Garden
This function takes in the dictionary and the ID the user wishes to remove as parameters. The function removes that garden from the dictionary. Assume the user will only type in gardens that are in the dictionary. 

Remember you can remove a key from a dictionary using:  

    if 'key' in my_dict:
        del my_dict['key']


![Remove](https://user-images.githubusercontent.com/1709150/144749078-45ec42bc-3a99-41f8-8e04-b8c99d4c7125.png)


## Program 2:

### Step 1: Setting up a New Dictionary
This program will read in an exported .txt file from your previous program (See Step 2.2 for more information). Again, this dictionary should use the Garden ID as the key and the Garden Name and Daily Cost as the values for the dictionary. The name of the file should be read in through the terminal.

Gardeners charge for 90 days of work in the summer. This means that the entire cost of the summer for each garden is equal to the daily cost * 90. Store this calculated value as another value element in each dictionary key’s list. 

### Step 2: Optimization
The cost of an automated sprinkler system to replace a gardener at one garden is $50000 (this includes the cost of water). Due to a limited supply of these sprinkler systems, there are only 3 available. Determine which gardens should be replaced with sprinklers. Output the Garden Names which gardens should have sprinklers instead of gardeners. Also output amount of money spent on the entire project and the amount of money saved by implementing sprinklers (could be 0). The final prices output should be rounded and printed using the format operator.

Output should resemble:  

![Output](https://user-images.githubusercontent.com/1709150/144749327-91b14fb3-f11f-42ee-b512-1645abd17092.png)

Assume the Export.txt above is generated from the exported file from Program 1 without making any changes

In a different example where gardens do cost more than 50000,  the output would look something like this: 

![Output 2](https://user-images.githubusercontent.com/1709150/144322196-a8c49959-40b4-4677-b2fa-bbbdd097d9df.png)


Remember, you do not need to buy all 3 sprinklers as you can choose to buy 0-3. In some cases, the most expensive gardens will be less than $50000 to upkeep by a gardener and therefore buying no sprinklers is the cheapest option. 

Hint: One way to do this easily is to first find the 3 most expensive gardens and then check which ones cost more than $50000 for the entire summer. Those 0-3 gardens could get replaced with sprinklers.


