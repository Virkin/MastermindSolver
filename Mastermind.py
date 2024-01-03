import random

class Mastermind :
    mCodeToFind = []
    mNumberOfColors = 0
    mNumberOfTry = 0
    mCodeLength = 0

    def __init__( self, pNumberOfColors, pNumberOfTry, pCodeLength ) :
        self.mNumberOfColors = pNumberOfColors
        self.mNumberOfTry = pNumberOfTry
        self.mCodeLength = pCodeLength

        self.mCodeToFind = self.CreateNewCode()

        return
    
    def CreateNewCode( self ) :
        lNewCode = []
        lAvailableColors = []

        for i in range( self.mNumberOfColors ) :
            lAvailableColors.append( i )
        
        for i in range( self.mCodeLength ) :
            lPickedColor = random.randrange( len( lAvailableColors ) )
            lNewCode.append( lAvailableColors[ lPickedColor ] )
            del lAvailableColors[ lPickedColor ]
        
        return lNewCode
    
    def GetCode( self ) :
        return self.mCodeToFind
