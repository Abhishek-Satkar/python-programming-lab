from easygui import *
import sys

while 1:
    msgbox("Hello, world!")

    msg ="Data?"
    title = "Data Types"
    choices = ["Pie", "Histogram", "Line Graph"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Survey Result")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if choice=="Pie":     # show a Continue/Cancel dialog
        pass# user chose Continue
        import numpy as np
        import matplotlib as plt
        import matplotlib.pyplot as plt
        %matplotlib inline
        labels='Red','Green','Yellow','Blue'
        x=int(input("Enter a value"))
        y=int(input("Enter a value"))
        z=int(input("Enter a value"))
        w=int(input("Enter a value"))
        sizes=[x,y,z,w]
        colours=['Red','Green','Yellow','Blue']
        plt.pie(sizes,labels=labels)
        plt.axis('equal')
        plt.show()
    elif choice=="Histogram":
        import matplotlib.pyplot as plt
        a=int(input("Enter a number"))
        b=int(input("Enter a number"))
        c=int(input("Enter a number"))
        d=int(input("Enter a number"))
        e=int(input("Enter a number"))
        f=int(input("Enter a number"))
        g=int(input("Enter a number"))
        h=int(input("Enter a number"))
        x1 = [a,b,c,d]
        y1 = [e,f,g,h]

        plt.bar(x,y,label='Bar1')

        plt.xlabel('x1')
        plt.ylabel('y1')
        plt.title('Histogram')
        plt.legend()
        plt.show()
    elif choice=="Line Graph":
        import matplotlib.pyplot as plt
        x = [1,2,3]
        y = [5,7,4]

        x2 = [1,2,3]
        y2 = [10,14,12]

        plt.plot(x,y,label='First Line')
        plt.plot(x2,y2,label='Second Line')
        plt.xlabel('Plot Number')
        plt.ylabel('Important Var')
        plt.title('Interesting Graph\nCheck it out')
        plt.legend()
        plt.show()
    else:
        sys.exit(0)