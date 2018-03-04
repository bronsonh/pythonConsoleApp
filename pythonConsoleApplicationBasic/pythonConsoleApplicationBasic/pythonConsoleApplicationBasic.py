
print("Thank you for viewing my code!\nThis application is to show off some basic Python skills while also learning about Python 3.x as i had previously only used 2.x\n") #Print a little information on screen about purpose of this application


def optionMenuFunct(): #Create a function to be called for the option menu



    try:
        print("Choose an option:\n%s\n%s\n" % ("1, The very basic calculator", "2, NotSureYet"))#Give the user some options to choose from
        option = int(input("Please enter a number: ")) #Get the input from the user and make it an integer

        if option == 1: #If the user presses 1 go to the calculator function
            print("hi")

        elif option == 5: #Clear the Console and reload the option menu

             print("\n" * 50) #Apparently this is the only way without calling os commands
             optionMenuFunct()

        else: #Error catch, Just incase anyone presses anything thats not listed or accepted.
             print("Please make sure you type in another between 1 and x")
             optionMenuFunct()
    except:
        print("Please make sure you entered a number between 1 and x")

optionMenuFunct() #call the optionMenuFunct to bring up the option menu