
# coding: utf-8

# In[2]:

import numpy as np


def perceptron(weights, inputs, bias):

    model = np.add(np.dot(inputs, weights), bias)
    logit = activation_function(model, type="sigmoid")
    return np.round(logit)


# In[3]:

def activation_function(model, type="sigmoid"):

    return {
        "sigmoid": 1 / (1 + np.exp(-model))
    }[type]


def compute(data, logic_gate, weights, bias):
    weights = np.array(weights)
    output = np.array([ perceptron(weights, datum, bias) for datum in data ])

    return output


# In[4]:

def print_template(dataset, name, data):
    # act = name[6:]
    print("Logic Function: {}".format(name.upper()))
    print("X0\tX1\tX2\tY")
    toPrint = ["{1}\t{2}\t{3}\t{0}".format(output, *datas) for datas, output in zip(dataset, data)]
    for i in toPrint:
        print(i)


# In[5]:

def main():
    dataset = np.array([
      [0, 0, 0],
      [0, 0, 1],
      [0, 1, 0],
      [0, 1, 1],
      [1, 0, 0],
      [1, 0, 1],
      [1, 1, 0],
      [1, 1, 1]
    ])
    gates = {
        "and": compute(dataset, "and", [1, 1, 1], -2),
        "or": compute(dataset, "or", [1, 1, 1], -0.9),
        "not": compute(np.array([ [0], [1] ]), "not", [-1], 1),
        "nand": compute(dataset, "nand", [-1, -1, -1], 3),
        "nor": compute(dataset, "nor", [-1, -1, -1], 1),
        # _xor = compute(dataset, "and", [1], dataset),
        # _xnor = compute(dataset, "xnor", [], dataset)
    }

    for gate in gates:
        print_template(dataset, gate, gates[gate])



if __name__ == '__main__':
    main()


# In[ ]:



