
# coding: utf-8

# In[45]:

#"what do you need for genetic algo:- 1- guess function , 2- mutation, 3- fitness"


# In[36]:

import random
import datetime

import genetic
import unittest

# In[38]:

def get_fitness(gene,target):
    return sum(1 for actual,expected in zip(gene,target) if expected==actual  )




# In[40]:

def display(counter,gene,target,startTime):
    timediff=datetime.datetime.now()-startTime
    fitness=get_fitness(gene,target)
    print("{0}\t{1}\t{2}\t{3}".format(counter,timediff,gene,fitness))



# In[ ]:
def test_Hello_World():
    target = "Hello World!"
    guess_password(target)


def guess_password(target):
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()

    def fnGetFitness(genes):
        return get_fitness(genes, target)

    def fnDisplay(counter,genes):
        display(counter,genes, target, startTime)

    optimalFitness = len(target)
    genetic.get_best(geneSet, len(target),fnGetFitness, fnDisplay)

#if __name__ == '__main__':
#    test_Hello_World()

class GuessPasswordTests(unittest.TestCase):
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"

    def test_Hello_World(self):
        target = "Hello World! My name is mohit gupta. And this is genetic algo and it works so cool"
        self.guess_password(target)

    def guess_password(self, target):
        startTime = datetime.datetime.now()
        optimalFitness = len(target)
        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(counter,genes):
            display(counter,genes, target, startTime)
        best = genetic.get_best(self.geneSet, len(target),fnGetFitness, fnDisplay)
        self.assertEqual(best, target)
if __name__ == '__main__':
    unittest.main()
