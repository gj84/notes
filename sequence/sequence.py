
import pprint

class Sentence():

    def __init__(self, *args, **kwargs):
        self.expressions = [None] # Just for starting sequences with 1
        if "sequence" in kwargs:
            self.sequence = [None] + list(kwargs["sequence"])
            self.set_expressions()

    def set_expressions(self):
        self.expressions.append(str(self.sequence[1]))
    
        for m in range(2, len(self.sequence)):
            c = str((self.sequence[m] - \
                eval(self.expressions[m-1], {"n":m})) / \
                eval(self.__sub_expression(m),{"n":m}))
            f_ = self.expressions[m-1] + " + " + c + " * " + self.__sub_expression(m)
            self.expressions.append(f_)     

    def eval_expression(self, expression, **kwargs):
        return eval(expression, kwargs)
    
    def __sub_expression(self, m):
        """Helper"""
        return "*".join(["(n-{})".format(k) for k in range(1, m)])

    def __str__(self):
    	return self.expressions[-1]


seq = (1,1,3,5,9,21,35)
a = Sentence(sequence = seq)
f = a.expressions[-1]

for k in range(1, len(seq)+1):
	print(eval(f, {"n": k}))

print(a)

"""
def sub_expression(m):
    "_""Helper"_""
    return "*".join(["(n-{})".format(k) for k in range(1, m)])

a = (None, 1, 2, 3, 8, 12, 25, 28)

f = [None]

# paso 1 
f.append(str(a[1]))



# paso 3 
for m in range(2, 7):
    c = str((a[m] - eval(f[m-1], {"n":m})) / eval(sub_expression(m),{"n":m}))
    f_ = f[m-1] + " + " + c + " * " + sub_expression(m)
    f.append(f_)

"""



