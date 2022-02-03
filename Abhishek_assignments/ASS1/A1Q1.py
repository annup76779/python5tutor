"""
Name: 
Username: 
ID number: 

Description:
--

This program will find the area(rounded to two deciaml places) of a triangle based on the 3 sides given using the Heron's Formula

s = (side1 + side2 + side3)/2 # finding semi_perimeter

area = (s*(s - side1)*(s - side2)*(s - side3)) ** 0.5

"""
 
# taking the user inputs
side1 = float(input("Enter side a: "))
side2 = float(input("Enter side b: "))
side3 = float(input("Enter side c: "))

s = (side1 + side2 + side3)/2 # finding semi_perimeter

area_of_triangle = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5  # returning the are of the triangle

# rounding of the triangle area to two decimal places
rounded_area_of_triangle = round(area_of_triangle, 2)

# output
print("The area of the triangle is", rounded_area_of_triangle) 