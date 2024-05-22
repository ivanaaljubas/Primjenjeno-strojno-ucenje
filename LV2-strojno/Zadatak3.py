import matplotlib.pyplot as plt
import numpy as np
img = plt.imread("C:\\Users\\Ivana\\Desktop\\LV2-strojno\\tiger.png")
img = img[:,:,0].copy()

print(img.shape)

imgFlipped = np.fliplr(img)
imgRotated = np.rot90(img,3)

imgResolution = img[::5,::5]
imgBrightness = img+0.8
imgBrightness[imgBrightness>1] = 1

visina, sirina = img.shape

print(sirina*0.25, sirina*0.5)

novaSlika = img

novaSlika[:,sirina//2:] = 0
novaSlika[:,:sirina//4] = 0
   

plt.figure()
plt.imshow(novaSlika, cmap="gray")
plt.show()