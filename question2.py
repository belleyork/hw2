# -*- coding: utf-8 -*-
string_input= input ("Please write tuples in (x,y) format. Separate each tuple with a semi-colon: ")
input_list= string_input.split(';')
print(type(input_list))
length1= len(input_list)

new_list= []
for n in range(length1):
    x= float(input_list[n][1])
    #print "x is " + x
    y= float(input_list[n][3])
    #print "y is " + y
    new_list.append([x,y])
#print "new list is " + str(new_list)
    
# you get the inputs as a nested list 

length2= len(new_list)
print(length2)
#print str(new_list[0][0]) + " equals " + str(new_list[0][1])
#print "new_list[0] is " + str(new_list[0])


at_line= []
above_line=[]
below_line= []
for r in range(1):
    #print "r is " + str(r)
    #print "x is " + str(x)
    #print new_list[r][0]
    for a in range(length2):
        #print "new_list[a][0] is " + str(new_list[a][0])
        #print "new_list[a][1] is " + str(new_list[a][1])
        if float(new_list[a][0]) == float(new_list[a][1]):
            new_list[a]= tuple(new_list[a])
            at_line.append(new_list[a])
        elif float(new_list[a][0]) < float(new_list[a][1]):
            new_list[a]= tuple(new_list[a])
            above_line.append(new_list[a])
        else:
            new_list[a]= tuple(new_list[a])
            below_line.append(new_list[a])
            


print("Tuples at the line are " + str(at_line))
print("Tuples above the line are " + str(above_line))
print("Tuples below the line are " + str(below_line))
