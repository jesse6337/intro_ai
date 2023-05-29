class term:
    def __init__(self, coefficent, variable, power):
        self.coefficent = coefficent
        self.variable = variable
        self.power = power
    def display_expression(self):
        print("{}{}^{}".format(self.coefficent, self.variable, self.power))

class expresstion:
    def __init__(self, coefficent, variable, power):
        self.coefficent = coefficent
        self.variable = variable
        self.power = power

    def __add__(self, term):
        if (self.power == term.power and self.variable == term.variable):
            coef = int(self.coefficent) + int(term.coefficent)
            return expresstion(coef, self.variable, self.power)
        else:

    
    def display_expression(self):
        print("{}{}^{}".format(self.coefficent, self.variable, self.power))

term = expresstion(2,'x', 1)
term.display_expression()