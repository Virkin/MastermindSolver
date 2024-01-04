from Mastermind import Mastermind
from Solver import Solver

gNumberOfColors = 8
gCodeLength = 5
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

    lSolver = Solver( gNumberOfColors, gCodeLength )
    lSolver.InitializeSolver()

    lResult = None

    while not ( lMastermind.IsSolved() or lMastermind.IsAllTryUsed() ) :
        #lCorrectInputGiven = False

        #while not lCorrectInputGiven :
            #lInputCode = input()
            #lCorrectInputGiven = CheckInput( lInputCode )
      
        lGivenCode = lSolver.GuessCode( lResult )
        lResult = lMastermind.CheckCode( list( map( int, lGivenCode ) ) ) 
  
        print( lGivenCode )
        print( lResult )
        
        #print( lMastermind.CheckCode( list( map( int, list( lInputCode ) ) ) ) )