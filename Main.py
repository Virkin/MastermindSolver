from Mastermind import Mastermind

if __name__ == "__main__":
    lMastermind = Mastermind( 8, 5, 12 )
    lMastermind.InitializeGame()

    while not ( lMastermind.IsSolved() or lMastermind.IsAllTryUsed() ) :
        lInputCode = input()
        print( lMastermind.CheckCode( list( map( int, list( lInputCode ) ) ) ) )