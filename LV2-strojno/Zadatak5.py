import numpy as np
import matplotlib.pyplot as plt

def alternating_squares(square_size, num_squares_height, num_squares_width):
    # Dimenzije slike
    height = square_size * num_squares_height
    width = square_size * num_squares_width
    
    # Kreiranje crne matrice
    black_square = np.zeros((square_size, square_size))
    # Kreiranje bijele matrice
    white_square = np.ones((square_size, square_size)) * 255
    
    # Inicijalizacija prazne slike
    img = np.zeros((height, width))
    
    # Popunjavanje slike s crnim i bijelim kvadratima
    for i in range(num_squares_height):
        for j in range(num_squares_width):
            if (i + j) % 2 == 0:
                img[i * square_size: (i + 1) * square_size, j * square_size: (j + 1) * square_size] = black_square
            else:
                img[i * square_size: (i + 1) * square_size, j * square_size: (j + 1) * square_size] = white_square
    
    return img.astype(np.uint8)

# Primjer korištenja funkcije
square_size = 50
num_squares_height = 8
num_squares_width = 8

img = alternating_squares(square_size, num_squares_height, num_squares_width)

# Prikaz slike
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')  # Isključuje oznake osi
plt.show()
