import itertools

class Solver :
    mGameHistory = []

    mNumberOfColors = 0
    mCodeLength = 0

    mAllPossibleCodes = []
    
    def __init__( self, pNumberOfColors, pCodeLength ) :
        self.mNumberOfColors = pNumberOfColors
        self.mCodeLength = pCodeLength
    
    def InitializeSolver( self ) :
        self.mGameHistory = []

        lColorList = []

        for i in range( self.mNumberOfColors ) :
            lColorList.append( i )

        self.mAllPossibleCodes = []

        for lCode in itertools.permutations( lColorList, self.mCodeLength ):
            self.mAllPossibleCodes.append( list( lCode ) )

    def GuessCode( self, pPreviousResult = None ) :
        if pPreviousResult :
            self.mGameHistory[-1][1] = pPreviousResult 

            lLastTry = self.mGameHistory[-1]
            lLastCode = lLastTry[0]
            lLastResult = lLastTry[1]

            lLastNumberOfGoodColors = lLastResult.count( 0 )
            lLastNumberOfGoodPosition = lLastResult.count( 1 )

            lCodesToRemove = []

            for lCode in self.mAllPossibleCodes :
                lGoodColorsCount = 0
                lGoodPositionCount = 0
                for i in range( len( lCode ) ) :
                    lColor = lCode[i]

                    if lLastCode[i] == lColor :
                        lGoodPositionCount += 1
                    elif lColor in lLastCode :
                        lGoodColorsCount += 1

                if lGoodColorsCount != lLastNumberOfGoodColors or lGoodPositionCount != lLastNumberOfGoodPosition :
                    lCodesToRemove.append( lCode )
            
            for lCode in lCodesToRemove :
                self.mAllPossibleCodes.remove( lCode )

        lFirstPossibleCode = self.mAllPossibleCodes[0]
        self.mGameHistory.append( [ lFirstPossibleCode, [] ] )
        self.mAllPossibleCodes.remove( lFirstPossibleCode )

        return lFirstPossibleCode
    

