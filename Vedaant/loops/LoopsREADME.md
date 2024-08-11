#### Loops
###### What are loops?
1. Loops are used to repeate the same set of instructions multiple times, and number of repetitions depends on the condition provided to loops
2. Looping statement need three things to work: 
   1. the actual task that has to repeat
   2. the condition when the execution of the task will be terminated
   3. and the same condtion should be written in the manner than it will defind the beginning of the loop


##### Example algo for loops
1. you have dragon in a game
2. that dragon is supposed to run when you click space
3. and that dragon is supposed to stop running when you clash with a cactus
4. To make a condtion that acts like start of the loops and end of the loops, we will make a variable named isRunning
5. on click of the space we will set that variable to true
6. then we will start the loop with conditio `isRunning == true` 
7. and when the dragon will clash with the cactus it, will update the value of `isRunning` to `false`, thus the condition for the loop with become false, and the loop will terminate


#### Types of loops in python
1. While loops - `while`
2. for loops - `for`