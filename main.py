import numpy as np
import matplotlib.pyplot as plt

# Định nghĩa kích thước ảnh
rows, cols = 8, 8

# Tạo ma trận COLS và ROWS (vị trí pixel)
cols_idx, rows_idx = np.meshgrid(np.arange(cols), np.arange(rows))

# Tần số ngang và dọc
u0, v0 = 2, 2

# Tạo ảnh I1 theo công thức
I1 = 0.5 * np.exp(1j * 2 * np.pi * (u0 * cols_idx + v0 * rows_idx) / 8)

# Lấy phần thực và phần ảo
real_part = np.real(I1)
imag_part = np.imag(I1)

# Hiển thị phần thực và phần ảo
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(real_part, cmap='gray', vmin=-0.5, vmax=0.5)
plt.title('Real Part of I1')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(imag_part, cmap='gray', vmin=-0.5, vmax=0.5)
plt.title('Imaginary Part of I1')
plt.colorbar()

plt.tight_layout()
plt.show()

# Tính DFT và trung tâm nó
I1_dft = np.fft.fftshift(np.fft.fft2(I1))

# Lấy phần thực và phần ảo của DFT
real_dft = np.real(I1_dft)
imag_dft = np.imag(I1_dft)

# In ra phần thực và phần ảo của DFT
print("Real part of DFT(I1):")
print(np.round(real_dft, 4))

print("\nImaginary part of DFT(I1):")
print(np.round(imag_dft, 4))
