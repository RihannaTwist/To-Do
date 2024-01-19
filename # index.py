#Main
MovieList = ["Star Wars", "Barbie", "A Ballad of Songbirds and Snakes", "Night School"]
print("Welcome to your Movie List")
print("Please choose option: (Type in a number between 1-5)")
print("1. View List \n2. Add to list \n3. Check as Complete \n4. Remove movie \n5. Clear List \n6. Aphabletize\n 7. Print Num of Movies\n 8. Quit")
option = int(input("Option:"))

if (option == 1):#prints list
    print(MovieList)
elif (option == 2):#adds new movie
    MovieList.append(input("What would you like to add to your list?"))
    print(MovieList)
elif (option == 3):#marks movie as watched
    MovieList = ["Star Wars", "Barbie", "A Ballad of Songbirds and Snakes", "Night School"]
    ans= input ("what movie would you like to check off your list?")
    i= MovieList.index (ans)
    MovieList[i]= ans + "X"
    print (MovieList)
elif (option == 4):#deletes movie off list
    MovieList.pop(int(input("What movie # on the list do you want to remove?")))
    print(MovieList)
elif (option == 5):#clears List
    MovieList.clear()
    print (MovieList)
elif (option == 6):#sorts list alphabetically
    MovieList.sort()
    print (MovieList)
elif(option == 7):#prints movies on list
    print (len (MovieList))
elif (option == 8):#quits program
    quit()