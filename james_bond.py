# Here I list a string of James Bond Movies 


james_bond_movies = ["License to Kill","Goldfinger",
                     "Thunderball","Diamonds are Forever",
                     "On Her Majesty's Secret Service","Live and Let Die"] 


# Here I print the movie Diamonds are Forever 

print(james_bond_movies[3]) 

# Here I call out a function to print two movies   


def james_bond_movies_two(one,two):
    print(f"The movie {one} and {two} are both good movies") 

james_bond_movies_two(james_bond_movies[2],james_bond_movies[4]) 

# Here I call out a function for six movies


def james_bond_movies_three(red,green,blue,yellow,orange,white):
    print(f"the movies {red} and {green} and {blue} and {yellow} and {orange} and {white} are also good movies") 

james_bond_movies_three(james_bond_movies[0],james_bond_movies[1],james_bond_movies[2],
                        james_bond_movies[3],james_bond_movies[4],james_bond_movies[5])  


print("Please select your favourite movie from the list below")

view = james_bond_movies[:]  



# Here I create a for loop

for view in(james_bond_movies[:]): 
    print(view)


# Here I create an input 

television = input(f"Whats your favourite movie?")   

# Here I create an If Else statement 

if television == "Thunderball": 

    print(f"This movie was shot in the Bahamas") 


elif television == "License to Kill":

    print(f"With Timothy Dalton?") 
    

elif television == "Diamonds are Forever": 

    print(f"With Sean Connery?")
 

elif television == "Goldfinger": 

    print(f"This movies music was composed by James Barry")


elif television == "On Her Majesty's Secret Service": 

    print(f"That movie was the sixth Bond Movie and came out in 1969")


elif television == "Live and Let Die": 
    
    print(f"The actor Roger Moore played James Bond in this movie")
    

else:
    print("No Wayyyys,only answer the above movies!!!!!!!!!!!!!!!!!") 


    
