## Tecchers' Result management system

##### Features 
1. Teacher can create a subject 
2. Each subject will have max marks, min marks, type(theory/Practical), and obtained marks
3. Teacher can create the result 
   1. Student name
   2. Roll number
   3. subject selection 
      1. Enter obtained marks for the object
   4. view all the result in Tabular format.
   5. summarize the result

#### Plan
1. Making functionality to create subject into the application 
2. We will make a list of the subjects created and can be accessed whenever required with their name
3. Make functionality to take as many students as there are and their subject marks
   1. we need to make a sub functionality where teacher will first create student
   2. then for that student, teacher will be entering marks of all the subjects
   3. this means each student will have a copy of the original subject list with all the details. 
4. When all of this over, we will make function that will display properly formatted result in tabular format
5. The results can be displayed in 2 formats - 
   1. Showing all the information of all the student and make card for each student. 
   2. Showing limited information of each stundent in table format.

#### Constraints 
1. Subject count cannot be more than 5
2. subject name cannot be more than 20 characters 
3. Student name cannot be more than 30 characters 
4. All subject max marks will be in 3 digits
5. Student roll number will not be greater than 16 digits 6
