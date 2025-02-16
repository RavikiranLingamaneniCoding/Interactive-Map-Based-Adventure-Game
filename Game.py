# Ravikiran Lingamaneni 101266712

import pygame


def runsMapGame():

    # initializes all the variables for the a map
    
    # stores the places in a one dimensional list
    places=["Gym","Residence Commons","Room","Washroom","Convenience Store","Starbucks","Cafeteria","Tunnels","Study Room","Park","Basketball Court","Equipment Room"
    ,"Medical Clinic","Shower","Change Room","Swimming Pool","Yoga Room","Ice Ring","Football Field","Soccer Field"]
    
    # Adjacency list that stores all the allowed areas for each place
    adjacencyList=[[1,10,11,14],[0,2,4,6],[1,3],[2],[1,5,7],[4],[1,7,9],[4,6,8],[7,9],[6,8],[0],[0,12,13,18],[11],[11,14,17],[0,13,15],[14,16],[15,17],[16,18],[11,17,19],[18]]
    
    # Adjacency list that stores all the allowed directions for each place
    directionList =[['e','s','w','n'],['w','s','e','n'],['n','s'],['n'],['w','s','n'],['n'],['s','e','n'],['s','w','n'],['s','w'],['s','e'],['n'],['e','s','n','w'],
    ['n'],['s','e','w'],['s','w','n'],['s','w'],['e','w'],['e','s'],['e','n','s'],['n']]

    descriptions=["place for you to workout with weights","place to hangout with your friends","Your room in your residence","This is where you shower and use washroom thats in your room",
    "Buy any snacks","Buy hot or cold drinks","place to eat food that gets served","Underground Pathway to walk when its cold","Place to study without noise",
    "outdoor area for playing outside","Indoor basketball Court","Room with sports equipment","Place to see a doctor","Public shower afer activities","Room to change your clothes",
    "Area to swim in water in the pool","Room to do yoga sessions","indoor ring to play hockey on ice","Outdoor area to play football in the football field","Outdoor Area to play soccer in the soccer field"]
     
    # current location and description of the player
    currentArea = "Gym"
    currentDescription = descriptions[0]


    # What items the user has so far
    inventory = []
    
    # 3 items
    items = ["chips","football","ice skating shoes"]

    # counting value for the position index
    index = 0

    
    flag = True

    # post condition loop
    while flag:
        print()

        # output the current area you are in
        print("You are now in", currentArea)

        print()

        # output the current description of the area you are in
        print("Description: ",currentDescription)
        
        print()

        # runs the pickup function
        pickup(items,inventory,index)


        # stores the index of the area the player is in
        index = places.index(currentArea)

        # stores the index of the descriptions
        indexDescription = index

        # shows all possible exits at each place
        print("From this location, you could go to any of the following:")
        
        print()

        # emptys the exit list
        exits = []


        # for loop to check the possible exits at each position
        for each in adjacencyList[index]:

            print(places[each])
            exits.append(places[each])
                
        print()

        # loop to ask again if they enter the wrong direction
        flag1 = True
        while(flag1==True):
            # asks the user which direction they would like to go and also asks if they want to see the inventory
            nextLocation = input("Would you like to go 'north', 'south', 'east' or 'west'? Type 'inventory' to see the items you have, Type 'exit' to quit:  ").lower()

            if (nextLocation=="exit"):
                exit()
        
            if (nextLocation == "inventory"):

                if (len(inventory) == 0):

                    print("You have no items in your inventory")

                else:
                    # output the inventory of the player
                    print("These are the items you have in your inventory: ",inventory)
                    
            # checks which direction the user wants to go to change to the letter of the direction
            # checks if the direction is north
            if nextLocation=="north":
                nextLocation='n'
                counter=0

                # checks where the direction which lead the player according to the directionsList which stores the allowed directions
                for i in directionList[index]:

                    if nextLocation== i:
                        nextLocation=places[adjacencyList[index][counter]]
                        flag1 = False
                    counter=counter+1
               
            # checks which direction the user wants to go to change to the letter of the direction
            # checks if the direction is south
            elif nextLocation=="south":
                nextLocation='s'
                counter=0

                # checks where the direction which lead the player according to the directionsList which stores the allowed directions
                for i in directionList[index]:

                    if nextLocation== i:
                        nextLocation=places[adjacencyList[index][counter]]
                        flag1 = False
                    counter=counter+1
               
            # checks which direction the user wants to go to change to the letter of the direction
            # checks if the direction is east
            elif nextLocation=="east":
                nextLocation='e'
                counter=0

                # checks where the direction which lead the player according to the directionsList which stores the allowed directions
                for i in directionList[index]:

                    if nextLocation== i:
                        nextLocation=places[adjacencyList[index][counter]]
                        flag1 = False
                    counter=counter+1

            # checks which direction the user wants to go to change to the letter of the direction
            # checks if the direction is west
            elif nextLocation=="west":
                nextLocation='w'
                counter=0

                # checks where the direction which lead the player according to the directionsList which stores the allowed directions
                for i in directionList[index]:

                    if nextLocation== i:
                        nextLocation=places[adjacencyList[index][counter]]
                        flag1 = False
                    counter=counter+1


                
            # if the direction isnt stored in the adjacency list then the user cannot go this direction and asks for direction again
            if flag1==True:
                print()
                print(" You cannot go this Direction")
                print()
        


        # updates the current location
        currentArea = nextLocation

        # stores the new index value
        index = places.index(currentArea)
        indexDescription = index

        # updates the description 
        currentDescription = descriptions[indexDescription]

	    
        print()

# pickup function which picks up the items at specific places
def pickup(items,inventory,index):

    # checks if player is in the area of the item so they can pick it up
    
    if (index == 4):

        take = input("You found chips. Type 'take' to pick up the item: ").lower()
        print()

        # Checks to see of the item has already been taken or not
        if ("chips" not in items):
            print("This item has already been taken")
            print()

        elif (take == 'take'):

            # removes item from the items list
            items.remove("chips")

            # adds the item to the inventory 
            inventory.append("chips")
            print(inventory)
            
            print()
    
    # checks if player is in the area of the item so they can pick it up
    
    if (index == 11):

        take = input("You found the football. Type 'take' to pick up the item: ").lower()
        print()

        # Checks to see of the item has already been taken or not
        if ("football" not in items):
            print("This item has already been taken")
            print()

        elif (take == 'take'):

            # removes item from the items list
            items.remove("football")

            # adds the item to the inventory 
            inventory.append("football")
            print(inventory)
            
            print()


    # checks if player is in the area of the item so they can pick it up
    
    if (index == 17):

        take = input("You found the ice skating shoes. Type 'take' to pick up the item: ").lower()
        print()

        # Checks to see of the item has already been taken or not
        if ("ice skating shoes" not in items):
            print("This item has already been taken")
            print()

        elif (take == 'take'):

            # removes item from the items list
            items.remove("ice skating shoes")

            # adds the item to the inventory 
            inventory.append("ice skating shoes")
            print(inventory)
            
            print()
    
# main
def main():
    
    # creates pygame window
    window = pygame.display.set_mode((1000,562))
    window.fill((225,225,225))
    # blits map image to screen
    map = pygame.image.load("map.jpg")
    window.blit(map,(0,0))
    # updates the view
    pygame.display.update()

    # runs the map game function
    runsMapGame()

main()

