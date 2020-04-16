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

def EnterPreferences(userName, userMap):
    ''' Allows user to enter preferences. Returns user to menu promptly after. '''
    prefs = []
    newPref = input('Enter an artist that you like (Enter to finish:)')
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
FirstOp=RunPreferences(userName, UserMap)
    while option in [e,r,p,h,m,q]:
        Option = input('''   \n Enter a letter to choose an option : \n
        e - Enter preferences \n
        r - Get recommendations \n
        p - Show most popular artists \n
        h - How popular is the most popular \n
        m - Which user has the most likes \n
        q - Save and quit''')       

#STARTING CODE SHOULD RUN BEFORE MAIN
userMap = loadUsers(PREF_FILE)
print('Welcome to the music recommender')
userName = input('Please enter your name ( put a $ symbol after your name if you wish your preferences to remain private ): ')
  

if __name__ == "__main__": main()

