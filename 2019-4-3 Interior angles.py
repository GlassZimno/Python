# Dominik Zimny
#3/4/2019
#set up loop
loop = True
while loop == True:
    #ask user for number of sides of the shape
    print("program to find interior and exterior angles of regular polygons")
    Sides=input("How many sides does your shape have? ")
    #convert variable to float
    Sides = float(Sides)
    #check if Sides is valid
    if Sides < 1 or Sides > 9999999999:
        loop = True
    else:
        #calculate each angle
        InteriorAngle=(Sides-2)*180
        Angles=InteriorAngle/Sides
        ExteriorAngle = 360-Angles
        #output the answer and ask the user if they want to go again, if so, loop, if not, end program
        print("Your interior angle is ",InteriorAngle,"degrees, and each angle is",Angles,"degrees and each exterior angle is",ExteriorAngle, "degrees")
        again=input("Again? [Y/N] ")
        if again == "Y":
            loop = True
        else:
            loop = False
