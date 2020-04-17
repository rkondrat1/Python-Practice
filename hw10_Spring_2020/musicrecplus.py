'''
Homework10MusicRecommender
Name: Timothy Stephens,Rachael Kondrat
Date: April 14, 2020
'''

# a very complex music recommender system ;-;

from cs115 import *

PREF_FILE = 'musicrecplus.txt'


def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'.
        Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    try:
        file = open(fileName, 'r')
    except FileNotFoundError:
        file = open(fileName, 'w+')
    userDict = {}
    for line in file:
        # Read and parse a single line 
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict

def getPreferences(userName, userMap):
    ''' Allows user to enter preferences. Returns user to menu promptly after. '''
    newPref = ""
    prefs = []
    userMap[userName] = prefs

    print("Enter an artist that you like (Enter to finish): ")
    newPref = input("")
        
    while newPref != "":
        prefs.append(newPref.strip().title())
        print("Enter an artist that you like (Enter to finish):")
        newPref = input("")
        
   
    userMap[userName] = prefs
    prefs.sort()
    return prefs



def getRecommendations(currUser, prefs, userMap):
    '''Gets recommendations for a user (currUser) based
    on the users in userMap (a dictionary) and the user's
    preferences in pref (a list). Returns a list of recommend
    artists.'''

    bestUser = findBestUser(currUser, prefs, userMap)
    print(userMap[bestUser])
    print(prefs)
    print(drop(prefs, userMap[bestUser]))
    recommendations = drop(prefs, userMap[bestUser])
    return recommendations



def mostPopular():
    '''print the artist that is liked by the most users.
    if there is a tie, print all artists with the most likes'''
    userList = []
    newUserList = []
    artistList = []

    baseListofUsers = loadUsers(PREF_FILE)

    likeList = []
    mostLikes = 0
    mostPopular = []
    memo = loadUsers(PREF_FILE)
    
    #load into userList the list of users
    for users in memo.keys():
        userList.append(users)
        
    #first exclude users with a $
    for users in userList:
        if users[len(users)-1] != '$':
            newUserList += [users]

    #second make a list of artists w/o users
    # i am comparing newUserList to the base list, since that has the artists
    #then adding the artists not attached to a private user to artistList
    for users in newUserList:
        if users in baseListofUsers:
            artistList += baseListofUsers[users]

    #next try to get the number of likes intoa list w/ the artist
    #the list will have [artist, likes]
    for artists in artistList:
        if likeList == []:
            likeList += [[artists,1]]
        else:
            for item in likeList:
                if artists == item[0]: #item[0] is the artist
                    item[1] +=1 #item[1] is the like number
                    break
                else:
                    likeList += [[artists,1]]

    #sort through likeList to find the artist with the most likes
    '''
        for item in likeList:
            if term[1] > mostLikes:
                mostLikes = term[1]
            print(mostLikes)
    '''
    for term in likeList:
        if term[1] > mostLikes:
            mostLikes = term[1]
            mostPopular += [item[0]]
            mostPopular.sort()
        else:
            mostPopular += [item[0]]
            mostPopular.sort()
    '''
    for item in likeList:
        if item[1] == mostLikes:
            mostPopular = [item[0]]
            mostLikes = item[1]
            mostPopular.sort()
        if item[1] > mostLikes:
            mostPopular += [item[0]]
            mostPopular.sort()
     '''       
    #return the most popular artists
    #also account for if there are not top artists 
    for item in mostPopular:
        if len(mostPopular) != 0:
            return 'Sorry no artists found'
            
        else:
            return item

def howPopular():
    '''returns the number of likes the most popluar artists received'''

    userList = []
    newUserList = []
    artistList = []

    baseListofUsers = loadUsers(PREF_FILE)

    likeList = []
    mostLikes = 0
    mostPopular = []
    memo = loadUsers(PREF_FILE)
    
    #load into userList the list of users
    for users in memo.keys():
        userList.append(users)
        
    #first exclude users with a $
    for users in userList:
        if users[len(users)-1] != '$':
            newUserList += [users]

    #second make a list of artists w/o users
    # i am comparing newUserList to the base list, since that has the artists
    #then adding the artists not attached to a private user to artistList
    for users in newUserList:
        if users in baseListofUsers:
            artistList += baseListofUsers[users]

   #next try to get the number of likes intoa list w/ the artist
    #the list will have [artist, likes]
    for artists in artistList:
        if likeList == []:
            likeList += [[artists,1]]
        else:
            for item in likeList:
                if artists == item[0]: #item[0] is the artist
                    item[1] +=1 #item[1] is the like number
                    break
                else:
                    likeList += [[artists,1]]
              
    #Make a list of artists with the most likes
    for term in likeList:
        if term[1] > mostLikes:
            mostLikes = term[1]
    print(mostLikes - 1)

    
    
def findBestUser(currUser, prefs, userMap):
    '''Find the user whose tastes are closest to the current user.
    Return the best user's name ( a string) '''
    bestUser = None
    bestScore = -1
    print("Prefs is", prefs)
    for user in userMap.keys():
        score = numMatches(prefs, userMap[user])
    if score > bestScore and currUser != user:
            bestScore = score
            bestUser = user
    return bestUser



def drop(list1, list2):
    '''Return a new list that contains only the elements in
    list2 that were NOT in list1.'''

    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
                print("Skipping", list1[i])
                i += 1
                j += 1
        elif list1[i] < list2[j]:
                i += 1
        else:
                list3.append(list2[j])
                j += 1
    # add the rest of list2 if theres anything left
    while j < len(list2):
        list3.append(list2[j])
        j += 1

    return list3

def numMatches(list1, list2):
    '''return the number of elements that match between
    two sorted lists'''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
                matches += 1
                i += 1
                j += 1
        elif list1[i] < list2[j]:
                i += 1
        else:
                j += 1
    return matches

            
    
def saveUserPreferences(userName, prefs, userMap, fileName):
    ''' Writes all of the user preferences to the file.
        Returns nothing. '''
    userMap[userName] = prefs
    file = open(fileName, 'w')
    for user in userMap:
        toSave = str(user) + ':' + ','.join(userMap[user]) + '\n'
        file.write(toSave)
    file.close()

def RunPreferences(userName, UserMap):
    if userName in UserMap:
        Option = input('''   \n Enter a letter to choose an option : \n
        e - Enter preferences \n
        r - Get recommendations \n
        p - Show most popular artists \n
        h - How popular is the most popular \n
        m - Which user has the most likes \n
        q - Save and quit''')  
    else:
        prefs = []
        print('I see that you are a new user')
        newPref = input('Please enter the name of an artist you like: ')
        saveUserPreferences(userName, prefs, userMap, PREF_FILE)
        while newPref != '':
            prefs.append(newPref.strip().title())
            print('Please enter another artist or band that you like or just press Enter to see Menu:')
        Option = input('''   \n Enter a letter to choose an option : \n
        e - Enter preferences \n
        r - Get recommendations \n
        p - Show most popular artists \n
        h - How popular is the most popular \n
        m - Which user has the most likes \n
        q - Save and quit''')  
        
  
def main():
    ''' The main recommendation function '''

    #STARTING CODE SHOULD RUN BEFORE MAIN
    userMap = loadUsers(PREF_FILE)
    print('Welcome to the music recommender')
    userName = input('Please enter your name ( put a $ symbol after your name if you wish your preferences to remain private ): ')
    

    menuLoop = True
    while menuLoop == True:
        option = input('\n Enter a letter to choose an option :' '\n'
        'e - Enter preferences' '\n'
        'r - Get recommendations' '\n'
        'p - Show most popular artists' '\n'
        'h - How popular is the most popular' '\n'
        'm - Which user has the most likes' '\n'
        'q - Save and quit' '\n ')
        if option == 'e':
            prefs = getPreferences(userName, userMap)
        elif option == 'r':
            return getRecommendations()
        elif option == 'p':
            return mostPopular()
        elif option == 'h':
            return HowPopular()
        elif option == 'm':
            return MostLikes()
        else:
            break

if __name__ == "__main__": main()

