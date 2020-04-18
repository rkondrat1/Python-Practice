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

def getRecommendations(currUser, prefs, userMap):
    '''Gets recommendations for a user (currUser) based
    on the users in userMap (a dictionary) and the user's
    preferences in pref (a list). Returns a list of recommend
    artists.'''

    #prefs = RunPreferences(currUser, userMap)

    bestUser = findBestUser(currUser, prefs, userMap)
    
    if bestUser == []:
        print("no recommendations at this time")
        
    print(userMap[bestUser])
    print(prefs)
    print(drop(prefs, userMap[bestUser]))
    recommendations = drop(prefs, userMap[bestUser])
    return recommendations

def mostPopular():
    '''print the artist that is liked by the most users.
    if there is a tie, print all artists with the most likes'''
    userList = []
    memo = loadUsers(PREF_FILE)

    newUserList = []
    artistList = []

    likeList = []
    mostLikes = 0
    mostPopular = []
    
    
    #load into userList the list of users
    for users in memo.keys():
        userList.append(users)
        
    #first exclude users with a $
    for i in userList:
        if i[len(i)-1] != '$' and len(i) != 0:
            newUserList += [i]

    #second make a list of artists w/o users
    # i am comparing newUserList to the base list, since that has the artists
    #then adding the artists not attached to a private user to artistList
    for user in newUserList:
        if user in memo:
            artistList += memo[user]

    #next try to get the number of likes intoa list w/ the artist
    #the list will have [artist, likes]
    for artists in artistList:
        if likeList == []:
            likeList += [[artists,1]]
        else:
            for item in likeList:
                if artists != item[0]: #item[0] is the artist
                    likeList += [[artists,1]]
                else:
                    item[1] +=1 #item[1] is the like number
                    break
                    
    #sort through likeList to find the artist with the most likes
    
    for term in likeList:
        if term[1] == mostLikes:
            mostPopular += [item[0]]
            mostPopular.sort()
        elif term[1] > mostLikes:
            mostLikes = term[1]
            mostPopular = [term[0]]
            mostPopular.sort()
            
        
    #return the most popular artists
    #also account for if there are not top artists 
    for x in mostPopular:
        if len(mostPopular) != 0:
            print(x)
        else:
            print('Sorry no artists found')

def howPopular():
    '''returns the number of likes the most popluar artists received'''

    #I just copied mostPop to get a list w/ [arist,likes]
    userList = []
    memo = loadUsers(PREF_FILE)

    newUserList = []
    artistList = []

    likeList = []
    mostLikes = 0
    mostPopular = []
    
    
    #load into userList the list of users
    for users in memo.keys():
        userList.append(users)
        
    #first exclude users with a $
    for i in userList:
        if i[len(i)-1] != '$' and len(i) != 0:
            newUserList += [i]

    #second make a list of artists w/o users
    # i am comparing newUserList to the base list, since that has the artists
    #then adding the artists not attached to a private user to artistList
    for user in newUserList:
        if user in memo:
            artistList += memo[user]

    #next try to get the number of likes intoa list w/ the artist
    #the list will have [artist, likes]
    for artists in artistList:
        if likeList == []:
            likeList += [[artists,1]]
        else:
            for item in likeList:
                if artists != item[0]: #item[0] is the artist
                    likeList += [[artists,1]]
                else:
                    item[1] +=1 #item[1] is the like number
                    break
    
              
    #Make a list of artists with the most likes
    for term in likeList:
        if term[1] > mostLikes:
            mostLikes = term[1]
    print(mostLikes)

    



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

def RunPreferences(userName, UserMap): #name 'userMap' is not defined
    if userName in UserMap:
        return
    else:
        prefs = []
        print('I see that you are a new user')
        newPref = input('Please enter the name of an artist you like: ')
    while newPref != '':
        prefs.append(newPref.strip().title())
        newPref = input('Please enter another artist or band that you like or just press Enter to see Menu:')
    UserMap[userName] = prefs
    return UserMap[userName]
    

def MostLikes(userMap):
    '''Finds and returns the user/users with the highest number of preferred
    artists.'''
    XuserMap = filter(lambda x:'$' not in x, userMap.keys()) #filters non $ users
    if len(XuserMap) == 0:
        print('Sorry no user found.')
    TopUser = [XuserMap[0]] #takes first user as base case
    for user in XuserMap:
        if len(userMap[user]) > len(userMap[TopUser[0]]): #replaces TopUser if more
            TopUser = [user]
        if len(userMap[user]) == len(userMap[TopUser[0]]) and user != TopUser[0]: #joins TopUser if equal?
            TopUser.append(user)
    TopUser.sort()
    print("\n".join(TopUser)) #prints the TopUser/users on individual lines

     
#gotta find a way to return back to menu!!!

def Quit(userName, userMap, fileName):
    '''Saves changes made to the file's content and safely exits the program.'''
    try:
        file = open(fileName, 'w')
        for user in userMap:
            toSave = str(user) + ':' + ','.join(userMap[user]) + '\n'
            file.write(toSave)
        file.close()
        quit()
    except FileNotFoundError:
        file = open(fileName, 'w+')
        for user in userMap:
            toSave = str(user) + ':' + ','.join(userMap[user]) + '\n'
            file.write(toSave)
        file.close()
        quit()
     
    
# i think this works but pop up window might not be acceptable
        
  
def main():
    ''' The main recommendation function '''

    #STARTING CODE SHOULD RUN BEFORE MAIN
    userMap = loadUsers(PREF_FILE)
    print('Welcome to the music recommender')
    userName = input('Please enter your name ( put a $ symbol after your name if you wish your preferences to remain private ): ')
    Check = RunPreferences(userName, userMap)

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
        if option == 'r':
                Recs = getRecommendations(userName, prefs, userMap)
        if option == 'p':
                MVPs = mostPopular()
        if option == 'h':
                MVPsCount = howPopular()
        if option == 'm':
                SpotifyCamper = MostLikes(userMap)
        if option == 'q':
                Terminator = Quit(userName, userMap, PREF_FILE)

if __name__ == "__main__": main()



