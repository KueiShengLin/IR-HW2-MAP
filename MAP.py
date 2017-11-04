
# coding: utf-8

# In[75]:



import re


# In[76]:


def readDoc():

    submission = []    
    solution = []

    with open('submission.txt') as submission_file:
        for line in submission_file:
            if(line != 'Query,RetrievedDocuments\n'):
                query = re.split(',| ',line)
                query.remove('\n')
                submission.append(query)
                        
    with open('solution.txt') as solution_file:
         for line in solution_file:
            if(line != 'Query,RetrievedDocuments\n'):
                query = re.split(',| ',line)
                query.remove('\n')
                solution.append(query)
            
    return(submission,solution)


# In[80]:


def MAP(submission,solution):
    AP =[]
    for query in range(len(solution)):
        relevant_Num = len(solution[query])-1
        precission = []
        num = 0
        have = 0
        for i in submission[query]:
            if (i != solution[query][0]):
                num += 1
                for j in solution[query]:
                    if(i == j):
                        have += 1
                        precission.append((have/num))
            if(have == relevant_Num):
                break
        AP.append(sum(precission)/relevant_Num)
    MAP = sum(AP) / len(solution)
    print(MAP)


# In[81]:


(submission,solution) = readDoc()
MAP(submission,solution)

