
# coding: utf-8

# In[1]:


import requests
import matplotlib.pyplot as plt
arr1 = []
for i in range(10):
    #print(i)
    str0 = 'https://api.hh.ru/vacancies/?per_page=100&page='+str(i)+'&text=machine+learning+OR+big+data+OR+data+science+OR+data+analytics'
    #print(str0)
    req0 = requests.get(str0)
    if req0.status_code != requests.codes.ok:
        print("Error: server return status code: " + str(req.status_code))
    arr1 += (req0.json()['items'])
print(arr1)
#len(arr2)


# In[2]:


vac_sal = {}
for i in arr1:
    if ((i['salary'] != None) and (i['salary']['currency'] == 'RUR')):
        if i['salary']['to'] == None:
            vac_sal[i['name']] = (i['salary']['from']) 
        elif i['salary']['from'] == None:
            vac_sal[i['name']] = (i['salary']['to']/2)           
        elif ((i['salary']['from'] != None) and (i['salary']['to'] != None)):
            vac_sal[i['name']] = ((i['salary']['to'] + i['salary']['from']) / 2)
    elif ((i['salary'] != None) and (i['salary']['currency'] == 'USD')):
        if i['salary']['to'] == None:
            vac_sal[i['name']] = (i['salary']['from'] * 57) 
        elif i['salary']['from'] == None:
            vac_sal[i['name']] = ((i['salary']['to'] / 2) * 57)           
        elif ((i['salary']['from'] != None) and (i['salary']['to'] != None)):
            vac_sal[i['name']] = (i['salary']['to'] + i['salary']['from'] / 2) * 57    
    elif   ((i['salary'] != None) and (i['salary']['currency'] == 'EUR')):
        if i['salary']['to'] == None:
            vac_sal[i['name']] = (i['salary']['from'] * 71) 
        elif i['salary']['from'] == None:
            vac_sal[i['name']] = ((i['salary']['to'] / 2) * 71)           
        elif ((i['salary']['from'] != None) and (i['salary']['to'] != None)):
            vac_sal[i['name']] = (i['salary']['to'] + i['salary']['from'] / 2) * 71      
vac_sal            


# In[3]:


data_science = []
for i  in vac_sal:
    if (('ata' in i) and ('cien' in i)):
        data_science.append(vac_sal[i])
data_science.sort() 
print(data_science)
med_ds = (data_science[len(data_science)//2])
print('медиана=', med_ds)


# In[4]:


machine_learning = []
for i  in vac_sal:
    if (('achine' in i) or ('earning' in i)):
        machine_learning.append(vac_sal[i])
machine_learning.sort() 
print(machine_learning)
med_ml = (machine_learning[len(machine_learning)//2])
print('медиана=', med_ml)


# In[5]:


programmer = list()
for i  in vac_sal:
    if ('рограммист' in i):
        programmer.append(vac_sal[i])
programmer.sort() 
print(programmer)
med_prg = (programmer[len(programmer)//2])
print('медиана=', med_prg)


# In[6]:


analyst = list()
for i  in vac_sal:
     if (('нали' in i) or ('naly' in i)) :
        analyst.append(vac_sal[i])
analyst.sort() 
print(analyst)
med_anl = (analyst[len(analyst)//2])
print('медиана=', med_anl)


# In[7]:


developer = list()
for i  in vac_sal:
     if (('азработ' in i)or ('evelop' in i)) :
        developer.append(vac_sal[i])
developer.sort() 
print(developer)
med_dvp = (developer[len(developer)//2])
print('медиана=', med_dvp)


# In[8]:


names = ['Data science', 'Developer', 'Analyst', 'Programmer', 'Machine learning']
x = [0, 1, 2, 3, 4]
med = [med_ds, med_dvp, med_anl, med_prg, med_ml]
plt.bar(x, med)
plt.xticks(x, names, rotation = 30)
plt.show()


# In[9]:


a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
print(len(vac_sal))
for i  in vac_sal:
    if (vac_sal[i] < 80000):
        a += 1
    elif ((vac_sal[i] >= 80000) and (vac_sal[i] < 120000)):
        b += 1
    elif ((vac_sal[i] >= 120000) and (vac_sal[i] < 150000)):
        c += 1  
    elif ((vac_sal[i] >= 150000) and (vac_sal[i] < 200000)):
        d += 1
    elif ((vac_sal[i] >= 200000) and (vac_sal[i] < 300000)):
        e += 1    
    elif (vac_sal[i] >= 300000):
        f += 1
print(a , b, c, d, e, f)

         


# In[10]:


names2 = ['<80k', '80k-120k', '120k-150k', '150k-200k', '200k-300k', '>300k']
x2 = [0, 1, 2, 3, 4, 5]
count = [a, b, c, d, e, f]
plt.bar(x2, count)
plt.xticks(x2, names2, rotation = 30)
plt.show()

