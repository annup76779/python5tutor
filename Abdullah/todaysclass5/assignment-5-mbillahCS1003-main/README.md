# Assignment 5
**Released on** Wednesday, December 1  
**Due on** Tuesday, December 7 (1 Week)  

**Modules Covered:** 1 - 12

## Preparation Steps:

- Watch all modules

## Submission: 

Your code should be completed individually. Make sure that every submitted file has a comment at the top with your name, section and student number. 

## Additional:

Only use the programming skills that you have learned in modules for this assignment. While there sometimes may exist solutions that are “better” through using other skills, we ask that you only use what you have been taught in the modules up to this point. We must make sure that you understand the taught material for full marks. 
 
## Useful Example

Recall the crate pushing example from Module 4.4 (the code for this example can be found on D2L). For this assignment, you will be asked to answer a parametric modelling question like that one. Along with this, you will also be asked to create a program that reads input from a .csv file and creates graphs around various statistical questions. 

### Part 1:

A box is being pushed along a concrete floor with a coefficient of friction of 0.525. The normal force of the box is 300N. The box has a mass of 40kg, and the acceleration of the box is 0.333m/s<sup>2</sup>. Remember the mass of gravity is -9.8m/s<sup>2</sup>. What is the Force applied on the box? Use parametric modelling to solve this question.

#### Useful Formulas:

![image](https://user-images.githubusercontent.com/1709150/144664718-edab34e9-6aa6-43bc-a46c-720634d73005.png)


 
### Part 2: 

Three students (Alf, Benny, and Claire) are in an intro to physics class and are working together on an assignment with 10 questions. Questions are like the question in Part 1 where they are given F<sub>N</sub>, acceleration and mass of a box, and a coefficient of friction and must calculate the Force being exerted (F<sub>A</sub>). They decide that each person should answer all 10 questions and then they can compare their answer afterwards. 

When the students meet up to compare, none of the students are have the same answer on any question. It is your job to decide which student has the closest answers on average. You are given a .csv file with 6 columns being the variables (F<sub>N</sub>, a, m, μ) followed by the student’s name and their guess for F<sub>A</sub>.

Write a program that shows all 30 answers of students on a scatterplot graph where x-values represent the question number and y-values represent the answers for each question. (For each x-value, there should be 3 y-values). Scatterplot should have proper labels for each axis and a title.

This program should then find the mean error for each student and the standard deviation of errors for each student. Remember to use ```abs()``` when caculating errors (i.e., there should be no negative values). You should NOT be using any functions that have not been introduced in class. This means you must calculate means, standard deviations, etc. using loops.

The mean errors should be displayed in a bar chart that is properly labelled. Each tick should be a student’s name, each bar should be a different colour, title, axis labels, etc. Standard deviations should be printed using ```print()``` using the following message:

    Student’s standard deviation of errors was: 1.6

#### Standard Deviation can be calculated using: 

![image](https://user-images.githubusercontent.com/77299347/123688854-ecea4680-d828-11eb-9af7-e74f920b5a26.png)

The final graph the program should display a pie chart that shows the percentage of errors that were within 10% of the correct answer. This graph should be labelled properly with a title and a legend.

The program should end by outputting a message about which student’s answers should be chosen based on who had the lowest mean error:

    Student’s answers should be used due to them having the lowest average error

