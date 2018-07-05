import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
#Lee la imagen y la guarda en arreglos. Sugerencia: asegurese de que la imagen este en escala de grises.
moon= mpimg.imread('moonlanding.png')

plt.figure()
plt.imshow(moon, cmap = 'gray')
plt.savefig(" Moon.pdf")

#Obtiene la transformada de Fourier .
fft = np.fft.fft2(moon)# FFT Normalized
shift=np.fft.fftshift(fft)

#filtar un ruido periodico
def filtro(a):
	elim=np.where(abs(a)>2000)
	a[elim]=0
	return a
n=filtro(shift)

plt.figure()
plt.imshow(abs(shift))
plt.colorbar()
plt.show()


def inversa(n):
	return np.real(np.fft.ifft2(n))
a=inversa(n)

plt.figure()
plt.imshow(a, cmap="gray")
plt.savefig("inversa.pdf")



