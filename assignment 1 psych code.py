# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Muhammed Munshad K 
# BAHI1230019

#QUESTION 1

#PART 1 
name = "Asha"
age = 20
life_lived = float ((age/73.49)*100)
is_student = True
print(name,"is",age,"years old,",life_lived,"% life span lived.","Student:",(is_student))
print(type(name),type(age),type(life_lived),type(is_student))   

#PART 2

age2 = age + 5
life_lived2 = float((age2/73.49)*100)
print(name,"is",age2,"years old,",life_lived2,"% life span lived.","Student:",(is_student))
      
#Both parts of the question were almost similar, Even without typing
# 'float' in the 15th line it giving float in the console. 

#Initially I had chose the way how we used in the class but then I realised 
#without even not writing like this (name = input("Enter Your Name:") ) we can give the name. 

#QUESTION 2

#STUDENT 1

quiz = 18
assignment = 35 
project = 40
Total1 = int (quiz + assignment + project)
percentage1 = ((Total1/100)*100)
passed1 = True if percentage1 >= 60 else False 
print("Student-1: Total", Total1, "/100; Percent:", percentage1, "Passed:", passed1)

#STUDENT 2

quiz2 = 10
assignment2 = 20 
project2 = 20
Total2 = int (quiz2 + assignment2 + project2)
percentage2 = ((Total2/100)*100)
passed2 = True if percentage2 >= 60 else False 
print("Student-1: Total", Total2, "/100; Percent:", percentage2, "Passed:", passed2)

# Total1 line(39) and percentage1 line(40) are expressions because they calculate values 
# using (+, /, *)
# passed1 line(41) and print line(42 and 52) are statements, 
# because passed1 uses condition to assign True/False, and print(...)
# gives the result

#QUESTION 3 

expr = 2 + 3 * 4 ** 2 // 5 % 3 
print("Original:", expr)
expr_parentheses = ((2+3)*4**2//5) % 3
print("expr parentheses", expr_parentheses)

# The first expression line(62) has no brackets, 
# so Python follows its normal order.
# The brackets which in in line(64) changed the result by 
# changing the order of steps in calculations.


#QUESTION 4

title = "Cognitive Psychology"
author = "Miller"
year = 1956
divider = "=" * 20
citation = author.upper() + "("+ str(year)+ "): "+ title
print(divider)
print(citation)

# I wrote three variables as code (title, author, year) to store 
# each part of the citation.
# Used .upper() to make the author's name capital.
# "+" combines all parts into one string.  







