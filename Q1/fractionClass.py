class fraction:
    def __init__(self, nom, dom):
        self.nom = nom
        self.dom = dom
    def simplify(self):
        gcf = fraction.greatestCommonFactor(self.nom, self.dom)
        x= int(self.nom/gcf)
        y = int(self.dom/gcf)
        return fraction(x,y)
    def printfraction(self):
        print("{}/{}".format(self.nom, self.dom))
    def getFraction(self):
        return self.nom, self.dom
    def findFactors(frac1):
        possibleFactorsT = []
        for i in range(1,frac1+1):
            if (frac1/i).is_integer():
                possibleFactorsT.append(i)
        return possibleFactorsT
    def greatestCommonFactor(num1, num2):
        num1P = fraction.findFactors(num1)
        num2P = fraction.findFactors(num2)
        gcf = 0
        for i in range(len(num1P)):
            for j in range(len(num2P)):
                if num1P[i] == num2P[j]: gcf = num1P[i]
        if gcf == 0: gcf = 1
        return gcf
    def leastCommonDom(frac1, frac2):
        x = frac1.dom * frac2.dom
        lcd = x/ fraction.greatestCommonFactor(frac1.dom, frac2.dom)
        return int(lcd)      
    def __imul__(frac1,self):
        newnom = (frac1.nom*self.nom)
        #newdom =(frac1.dom*self.dom)
        x = fraction(newnom, newdom)
        return fraction.simplify(x)
    def __add__(frac1,frac2):
        f1 =fraction.multiply(frac1, fraction(frac2.dom,frac2.dom))
        f2 =fraction.multiply(frac2, fraction(frac1.dom,frac1.dom))
        nomSum = f1.nom + f2.nom
        x = fraction(nomSum, f1.dom)
        return fraction.simplify(x)
    def __divide__(frac1, frac2):
        inverse = fraction(frac2.dom,frac2.nom)
        x = fraction.multiply(frac1, inverse)
        return fraction.simplify(x)
world = ['r','g','r','g','g']
belief_ = [fraction(1, len(world)) for i in range(len(world))]
testFrac = fraction(3,6)
for i in belief_:
    i.printfraction()
#test =fraction.add(testFrac,testFrac)
#test.printfraction()

#print(belief_)
def prob_of_belief(sensor, worldP, belief_):
    world_ = worldP
    # top half of Bayes formula
    for i in range(len(world_)):
        if sensor == world_[i]:
            belief_[i] *= fraction(9/10)
        elif sensor != world_[i]:
            belief_[i] = fraction.multiply(belief_[i], fraction(10,100)) 
    sum = fraction(0,1) 
    #find bottom half of Bayes formula (normalizer)
    for i in belief_:
        sum += i
    #complete Bayes Formula
    sum.printfraction()
    for i in range(len(belief_)):
        belief_[i]  = fraction.divide(belief_[i], sum)
    return belief_
x = prob_of_belief('r',world, belief_)
for i in x:
    i.printfraction()