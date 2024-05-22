import matplotlib.pyplot as plt
import numpy as np

# Učitavanje slike
img = plt.imread("C:\\Users\\Ivana\\Desktop\\LV2-strojno\\tiger.png")

# a) Posvijetljivanje slike (povećanje brightnessa)
brightened_img = np.clip(img * 1.2, 0, 1)  # Množimo svaki kanal (RGB) s faktorom 1.2, a zatim ograničavamo vrijednosti na raspon [0, 1]

# b) Rotiranje slike za 90 stupnjeva u smjeru kazaljke na satu
rotated_img = np.rot90(img)

# c) Zrcaljenje slike
flipped_img = np.fliplr(img)

# d) Smanjenje rezolucije slike x puta (npr. 10 puta)
downsample_factor = 10
downsampled_img = img[::downsample_factor, ::downsample_factor]

# e) Prikazivanje samo druge četvrtine slike po širini, a prikazivanje cijele slike po visini; ostali dijelovi slike trebaju biti crni
height, width, _ = img.shape
cropped_img = np.zeros_like(img)  # Kreiramo crnu sliku istih dimenzija kao originalna slika

# Računamo granice za drugu četvrtinu slike po širini
start_x = width // 2
end_x = width

# Kopiramo drugu četvrtinu slike po širini u crnu sliku
cropped_img[:, :end_x - start_x, :] = img[:, start_x:end_x, :]

# Prikazivanje rezultata
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

axes[0, 0].imshow(img)
axes[0, 0].set_title('Originalna slika')

axes[0, 1].imshow(brightened_img)
axes[0, 1].set_title('Posvijetljena slika')

axes[0, 2].imshow(rotated_img)
axes[0, 2].set_title('Rotirana slika')

axes[1, 0].imshow(flipped_img)
axes[1, 0].set_title('Zrcaljena slika')

axes[1, 1].imshow(downsampled_img)
axes[1, 1].set_title('Smanjena rezolucija')

axes[1, 2].imshow(cropped_img)
axes[1, 2].set_title('Samo druga četvrtina po širini')

plt.tight_layout()
plt.show()
