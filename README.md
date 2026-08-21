# Experiment 9 – Image Morphological Operations Using OpenCV

## 📌 Aim

To perform basic **morphological image processing operations** such as **Erosion and Dilation** on an image using Python and OpenCV.

## 📝 Description

This program creates a blank 500 × 500 image and adds the text **"Good Morning All"** to it using the `cv2.putText()` function.

A **3 × 3 kernel** is then created and used to perform two morphological operations:

* **Erosion** – Shrinks or reduces the foreground region.
* **Dilation** – Expands or increases the foreground region.

The results are displayed using Matplotlib.

## 🛠️ Technologies Used

* Python
* OpenCV (`cv2`)
* NumPy
* Matplotlib
* Jupyter Notebook / VS Code

## 📦 Requirements

Install the required libraries using:

```bash
pip install opencv-python numpy matplotlib
```

## 💻 Complete Code

```python
#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Create a blank image
# ---------------------------------------------------------
image = np.zeros((500, 500, 3), dtype=np.uint8)

# ---------------------------------------------------------
# 2. Add text on the image using cv2.putText
# ---------------------------------------------------------
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(
    image,
    'Good Morning All',
    (100, 250),
    font,
    1,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

# ---------------------------------------------------------
# 3. Display the input image
# ---------------------------------------------------------
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Input Image with Text")
plt.axis('off')
plt.show()

# ---------------------------------------------------------
# 4. Create a simple square kernel (3x3)
# ---------------------------------------------------------
kernel = np.ones((3, 3), np.uint8)

# ---------------------------------------------------------
# 5. Apply erosion (shrinking effect)
# ---------------------------------------------------------
eroded_image = cv2.erode(image, kernel, iterations=1)

# ---------------------------------------------------------
# 6. Display the eroded image
# ---------------------------------------------------------
plt.imshow(cv2.cvtColor(eroded_image, cv2.COLOR_BGR2RGB))
plt.title("Eroded Image")
plt.axis('off')
plt.show()

# ---------------------------------------------------------
# 7. Apply dilation (expanding effect)
# ---------------------------------------------------------
dilated_image = cv2.dilate(image, kernel, iterations=1)

# ---------------------------------------------------------
# 8. Display the dilated image
# ---------------------------------------------------------
plt.imshow(cv2.cvtColor(dilated_image, cv2.COLOR_BGR2RGB))
plt.title("Dilated Image")
plt.axis('off')
plt.show()
```

## 🔍 Explanation

### 1. Creating the Image

```python
image = np.zeros((500, 500, 3), dtype=np.uint8)
```

Creates a **500 × 500 black image** with 3 color channels.

### 2. Adding Text

```python
cv2.putText(image, 'Good Morning All', ...)
```

Adds the text **"Good Morning All"** to the image using OpenCV.

### 3. Creating the Kernel

```python
kernel = np.ones((3, 3), np.uint8)
```

Creates a **3 × 3 kernel** containing ones. This kernel is used for morphological operations.

### 4. Erosion

```python
eroded_image = cv2.erode(image, kernel, iterations=1)
```

Erosion reduces the boundaries of the foreground object. In this program, the white text becomes thinner.

### 5. Dilation

```python
dilated_image = cv2.dilate(image, kernel, iterations=1)
```

Dilation expands the boundaries of the foreground object. In this program, the white text becomes thicker.

## 📊 Operations Performed

| Operation    | Function        | Effect                     |
| ------------ | --------------- | -------------------------- |
| Text Overlay | `cv2.putText()` | Adds text to the image     |
| Erosion      | `cv2.erode()`   | Shrinks foreground objects |
| Dilation     | `cv2.dilate()`  | Expands foreground objects |

## 📁 Project Structure

```text
Experiment-9/
│
├── Ex 9.py
└── README.md
```

## 🎯 Result

The program successfully:

1. Created a blank image.
2. Added **"Good Morning All"** to the image.
3. Applied **erosion** using a 3 × 3 kernel.
4. Applied **dilation** using a 3 × 3 kernel.
5. Displayed the original, eroded, and dilated images.

## INPUT 
<img width="454" height="467" alt="image" src="https://github.com/user-attachments/assets/cd56ebff-71ff-4bdf-a727-253bb70af530" />

## OUTPUT
### Eroded Image
<img width="444" height="459" alt="image" src="https://github.com/user-attachments/assets/f961af9c-8f7b-4f25-9815-a0ed4614ee77" />


### Dilated Image
<img width="442" height="461" alt="image" src="https://github.com/user-attachments/assets/59badbd9-796f-4f89-9cb4-e26ee3292923" />

## 📚 Conclusion

Thus, basic morphological operations **Erosion and Dilation** were successfully implemented using OpenCV in Python.
