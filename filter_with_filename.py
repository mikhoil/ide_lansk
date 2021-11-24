from PIL import Image
import numpy as np

arr = np.array(Image.open('img2.jpg'))
step, size = 50, 10
rows, columns = len(arr), len(arr[0])
for row in range(0, rows - size + 1, size):
    for col in range(0, columns - size + 1, size):
        mean = np.mean(arr[row:row + size, col:col + size])
        arr[row:row + size, col:col + size] = mean // step * step
res = Image.fromarray(arr)
res.save('res.jpg')
