#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np


# # Задание 1
# Импортируйте библиотеку Numpy и дайте ей псевдоним np.
# Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов. Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7. Будем считать, что каждый столбец - это признак, а строка - наблюдение. Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. Результат запишите в массив mean_a, в нем должно быть 2 элемента.
#

# In[35]:


a = np.array([[1, 2, 3, 3, 1,],
            [ 6, 8, 11, 10, 7]])
a = a.T
a


# In[36]:


mean_a = a.mean(axis = 0)
mean_a


# # Задание 2
# Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков, содержащиеся в массиве mean_a. Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.
#

# In[38]:


a_centered = (a - mean_a)
a_centered


# # Задание 3
# Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp. Затем поделите a_centered_sp на N-1, где N - число наблюдений.
#

# In[48]:


a_centered_sp = np.dot(a_centered.T[0], a_centered.T[1])
a_centered_sp


# N - число наблюдений-
# не понял что это такое






