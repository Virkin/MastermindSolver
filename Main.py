from Mastermind import Mastermind

gNumberOfColors = 5
gCodeLength = 3
gNumberOfTry = 12

def CheckInput( pInput ) :
    lIsInputCorrect = True
    
    if not pInput.isdigit() :
        print("Only number is accepted")
        lIsInputCorrect = False
    
    if not len( pInput ) == gCodeLength :
        print("Code length must be exactly {} colors".format( gCodeLength ) )
        lIsInputCorrect = False

    return lIsInputCorrect

if __name__ == "__main__":
    lMastermind = Mastermind( gNumberOfColors, gCodeLength, gNumberOfTry )
    lMastermind.InitializeGame()

    while not ( lMastermind.IsSolved() or lMastermind.IsAllTryUsed() ) :
        lCorrectInputGiven = False

        while not lCorrectInputGiven :
            lInputCode = input()
            lCorrectInputGiven = CheckInput( lInputCode )

        print( lMastermind.CheckCode( list( map( int, list( lInputCode ) ) ) ) )