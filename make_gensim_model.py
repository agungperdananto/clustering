
# coding: utf-8

# In[9]:


import gensim
file = gensim.models.word2vec.Text8Corpus('data/text8')
model = gensim.models.Word2Vec(file, size=100)
model.save('data/text-8_gensim')



# In[6]:




