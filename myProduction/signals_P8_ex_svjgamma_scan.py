flist = []
#        self.mPseudo = self.mPiOverLambda * self.lambdaHV
#        self.mVector = self.calcLatticePrediction(self.mPiOverLambda,self.mPseudo)
#        mVectorOvermPseudo = (1.0/mPiOverLambda)*math.pow(5.76 + 1.5*math.pow(mPiOverLambda,2) ,0.5) 
#        mVector = mVectorOvermPseudo*mPseudo

mPseudo = 8.0 #from above should be 1.0*[2.0, 20.0]
mVector = 15 #from above is something else entirely

mPiOverLambda = 1.0
for MZp in [3000,6000]:
        for rinv in [0.3,0.5]:
                for brgamma in [0.5,0.9]:       
                        for lambdaHV in [2.0,10,20.0]:
                                flist.append({"channel": "s", "svjgamma": 1 , "mMediator": MZp,"mPseudo": mPseudo, "mVector": mVector, "rinv": rinv, "alpha": "peak", "lambdaHV": lambdaHV, "mPiOverLambda": mPiOverLambda, "BRGamma": brgamma })
