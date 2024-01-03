import random

class Mastermind :
    mCodeToFind = []
    mNumberOfColors = 0
    mCodeLength = 0
    mNumberOfTry = 0
    mTryCount = 0
    mIsInitialize = False
    mIsSolved = False

    def __init__( self, pNumberOfColors, pCodeLength, pNumberOfTry  ) :
        self.mNumberOfColors = pNumberOfColors
        self.mCodeLength = pCodeLength
        self.mNumberOfTry = pNumberOfTry
    
    def InitializeGame( self ) :
        self.mCodeToFind = self.CreateNewCode()
        mTryCount = 0
        mIsInitialize = True

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
    
    def CheckCode( self, pCode ) :
        self.mTryCount += 1
        
        if pCode == self.mCodeToFind :
            self.mIsSolved = True
            return [1]*self.mCodeLength
       
        lResults = []
        for i in range( len( pCode ) ) :
            lColor = pCode[ i ]
            if lColor in self.mCodeToFind :
                if lColor == self.mCodeToFind[ i ] :
                    lResults.append( 1 )
                else :
                    lResults.append( 0 )

        return lResults
    
    def IsSolved( self ) :
        return self.mIsSolved
    
    def IsAllTryUsed( self ) :
        return self.mTryCount == self.mNumberOfTry
