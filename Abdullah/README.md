# Assignment 4

**Released on** Tuesday, November 23    
**Due on** Monday, November 29 6:00PM (1 Week)

**Modules Covered:** 1 - 10

## Preparation Steps:

-	Watch all modules

## Submission: 

Submit the code by pushing the code on GitHub. Be sure to complete comments in your Python files that request your name, student number, etc. Parametric modelling solutions should be uploaded to the appropriate D2L Assignment drop box.

## Additional: 

Only use the programming skills that you have learned in modules for this assignment. While there sometimes may exist solutions that are “better” through using other skills, we ask that you only use what you have been taught in the modules up to this point. We must make sure that you understand the taught material for full marks.

## Exercise for Submission:

For Assignment 4, it is your job to help the traffic collision experts at the Department of Motor Vehicles. You must read in a .csv file of values, calculate the velocities of vehicles before collisions, and store the results in two separate .txt files. 

### Part 1:

Two trucks collide in an icy intersection. Truck 1 has a mass of 3000kg and is travelling at at an unknown velocity and his heading West [W] before the collision and Truck 2 has a mass of 2250kg and is travelling at 12m/s North [N] before the collision. The collision lasts for 0.5 seconds. After the collision, the two trucks slide alongside together at a velocity of 10m/s North-West [NW]. What is the velocity of the Truck 1 before the collision? Solve this problem with the three steps of parametric modelling. We only care about velocity in m/s, and you will not need to do any calculations related to the angles (simply solve for the variables you are looking for using the provided equations; the directions can be used in your diagram), and you do not have to worry about real world factors such as drag.  

Hint: You may want to calculate the momentum of the two vehicles together first.  

We are expecting a very simplistic representation for modeling this problem. You should ONLY us the provided formulas below: 

![image](https://user-images.githubusercontent.com/1709150/143053878-ca71d3ad-e84b-42c9-ae3b-d01daade9f3f.png)

 
### Part 2:

Program the function you developed in Part 1. Assume that truck 1 is always moving West and truck 2 is always mocing North, and that they always head North-Weat after the collision (i.e., the only that will change are the speicific parameters). The function should have the following parameters: Truck 1’s mass, Truck 2’s mass and velocity, and the velocity of the collision. The returned value is the velocity that Truck 1 was travelling before the collision. Test your function using the values you used in your calculation in Part 1.

### Part 3:

Update your program to read in various collisions from a .csv file whose filename is typed in by the user (a sample csv file has been provided). The order of values in this csv file are as follows: Collision ID, Truck 1’s mass, Truck 2’s mass, Truck 2’s velocity, and the velocity of the collision. Open this file to make sure you understand its contents.

For each collision, calculate the velocity in m/s of the Truck 1 and store it into RawVelocity.txt in a \n delimited list (that is one calculation per line). 

Assume that the speed limit before the intersection is 50km/hr. Report the Collision ID and the velocity of Truck 1 in km/hr if the truck was driving over the speed limit before the collision. For these speeding vehicles, write to the file the cost of the speeding ticket which is calculated (velocity – speed limit) * 12.50. The collisions should be ordered by the amount that Truck 1 is over the speed limit (ascending order). This is all recorded in a file called Vehicle1SpeedingTickets.txt. 

Additionally you should provided messages that indicate when you have completed writing details to each of the file and when your program has completed, to let the user know. See the sample image at the bottom.

Hint: You may want to use a list and/or a dictionary for ordering the output.  

#### Each Entry of Vehicle1SpeedingTickets.txt should look like:

_In Collision ID#1003A: The Vehicle was going 60km/hr and will be charged: $125.00._

**You must use the format operator to print the above message to the output file. Money amounts must be rounded correctly and display exactly 2 decimal places.**

#### For the provided Collisions.csv file given, the contents of the two files creaed by your program should be:

RawVelocity.txt:
```
    16.0153m/s
    44.8058m/s
    13.0516m/s
    59.1608m/s
```
Vehicle1SpeedingTickets.txt:
```   
     In Collision 1524A: The Vehicle was going 57.6551km/hr and will be charged: $95.69.
     In Collision 3682H: The Vehicle was going 161.301km/hr and will be charged: $1,391.26.
     In Collision 6866F: The Vehicle was going 212.979km/hr and will be charged: $2,037.24.
```

![image](https://user-images.githubusercontent.com/1709150/142947809-77881dec-2392-4577-93df-2239abf2492d.png)

