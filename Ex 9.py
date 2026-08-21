#!/usr/bin/env python
# coding: utf-8

# In[10]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[11]:


# Create a blank image
image = np.zeros((500, 500, 3), dtype=np.uint8)


# In[12]:


# Add text on the image using cv2.putText
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Good Morning All', (100, 250), font, 1, (255, 255, 255), 2, cv2.LINE_AA)


# In[13]:


# Display the input image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for displaying
plt.title("Input Image with Text")
plt.axis('off')


# In[14]:


# Create a simple square kernel (3x3)
kernel = np.ones((3, 3), np.uint8)


# In[15]:


# Apply erosion (shrinking effect)
eroded_image = cv2.erode(image, kernel, iterations=1)


# In[16]:


# Display the eroded image
plt.imshow(cv2.cvtColor(eroded_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
plt.title("Eroded Image")
plt.axis('off')


# In[17]:


# Apply dilation (expanding effect)
dilated_image = cv2.dilate(image, kernel, iterations=1)


# In[18]:


# Display the dilated image
plt.imshow(cv2.cvtColor(dilated_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
plt.title("Dilated Image")
plt.axis('off')


# In[ ]:




