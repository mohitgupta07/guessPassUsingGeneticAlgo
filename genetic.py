import random
import datetime
# In[43]:

def _guess(length,geneSet):
    newgene=[]
    while length>0:
        sampleSize=min(length,len(geneSet))
        newgene.extend(random.sample(geneSet,sampleSize))
        length-=sampleSize
    return ''.join(newgene)


# In[46]:

def _mutate(gene,geneSet):
    index=random.randrange(0,len(gene))
    childGene=list(gene)
    new,alt=random.sample(geneSet,2)
    if childGene[index]==new:
        childGene[index]=alt
    else:
        childGene[index]=new
    return ''.join(childGene)


# In[47]:


def get_best(geneSet,targetlen,get_fitness,display):
    random.seed()
    startTime=datetime.datetime.now()
    bestGene=_guess(targetlen,geneSet)
    bestFitness=get_fitness(bestGene)
    counter=1
    display(counter,bestGene)
    
    while bestFitness != targetlen:
        counter+=1
        newGene=_mutate(bestGene,geneSet)
        newFitness=get_fitness(newGene)
        if(newFitness>bestFitness):
            bestFitness=newFitness
            bestGene=newGene
            display(counter,bestGene)
    return bestGene
