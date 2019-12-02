#!/usr/bin/Python

"""
Project 1 From Project Euler:

        Multiples of 3 and 5.
Problem:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
    
                                                #Make Empty Array
multiples = []

                                                #Create a loop in the variable N that ranges from 1 - 1000
for n in range(1, 1000):
    
                                                #If variable N has no remainder than it is a multiple of 3
        if n % 3  == 0:
           
                                                #If it is 0 (Being a Multiple and having no remainder) Print The number is a multiple of 3.
            print "The number " + str(n) + " (is a multiple of 3) "
            
                                                #Place the number where N has no remainder and is a multiple of 3 inside our Array
            multiples.append(n)
           
                                                #in the second case make sure that the number 5 has no remainder as well. If it has no Remainder than it is a multiple of 5. 
        elif n % 5 == 0:
            
                                                #print the number is a multiple of 5.
                                                
                print "The number" + str(n) + " (Is a multiple of 5) "
                
                                                #add number to array
                multiples.append(n)
                                                #If there is a remainder than it is a multiple.
        else:
                                                # loop fell through without finding a multiple. Print Not A multiple
            print str(n) + " (not a multiple) "
           
                                                #Print Multiples added to the array
print multiples 
                                                #Print Sum of multiples and that is the answer!
print sum(multiples)



