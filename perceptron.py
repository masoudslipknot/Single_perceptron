import random
class perceptron:
    bias = 0.2
    weights = [None] * 5

def funcperc(f):
    if f < 0:
        return 0
    elif f >= 0:
        return 1

def insideperceptron(p=perceptron(), inputs=[None]*5):
    sum = 0
    for i in range(0,5):
        sum = sum + p.weights[i]*inputs[i]
    sum = sum - p.bias
    return funcperc(sum)

def createperceptron():
    i =0
    curp = perceptron()
    for i in range(0,5):
        curp.weights[i]= random.randint(1,20)
    curp.bias = random.randint(1,20)

    return curp


def adjust(delta,learningRate,p=perceptron(),inputs=[None]*5):
    for i in range(0,5):
        p.weights[i]=p.weights[i]+ inputs[i]*delta*learningRate

    p.bias = p.bias + learningRate*delta

def decidepassornot(inputs=[None]*5):
    sum = 0
    for i in range(0,5):
        sum = sum + inputs[i]

    mean = sum/5

    if mean >=14:
        return 1
    elif mean < 14:
        return 0


def train(learningrate,p = perceptron()):
    inputs = [None] * 5
    for k in range(0,1000):
     for i in range(0,20):

        for j in range(0,5):
            inputs[j]=random.randint(1,20)

        actual = insideperceptron(p,inputs)
        expected = decidepassornot(inputs)
        delta = expected - actual
        adjust(delta,learningrate,p,inputs)

def test():
    p = createperceptron()
    count =0
    inputs = [None] * 5
    for i in range(0, 20):

        for j in range(0, 5):
            inputs[j] = random.randint(1, 20)
        train(0.01,p)
        result = insideperceptron(p,inputs)
        if result == decidepassornot(inputs):
            count = count +1

    return count

def main():
    res = test()
    print("numbers were correct",res)

if __name__== "__main__":
  main()