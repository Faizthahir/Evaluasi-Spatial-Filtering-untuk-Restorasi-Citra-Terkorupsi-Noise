# Evaluasi-Spatial-Filtering-untuk-Restorasi-Citra-Terkorupsi-Noise
Proyek ini merupakan implementasi teknik spatial filtering dalam pengolahan citra digital untuk melakukan restorasi citra yang terkorupsi oleh berbagai jenis noise. Tujuan utama dari proyek ini adalah untuk membandingkan performa beberapa metode filtering dalam mengurangi noise serta mempertahankan kualitas citra.

Dalam proyek ini digunakan tiga jenis noise, yaitu Gaussian noise, salt-and-pepper noise, dan speckle noise. Untuk mengatasi noise tersebut, diterapkan beberapa metode filtering yang terdiri dari filter linear (mean filter dan Gaussian filter) serta filter non-linear (median filter dan max filter).

Evaluasi performa dilakukan menggunakan beberapa metrik, yaitu:

Mean Squared Error (MSE)

Peak Signal-to-Noise Ratio (PSNR)

Structural Similarity Index (SSIM)

Waktu komputasi

Selain evaluasi numerik, dilakukan juga analisis visual untuk melihat kualitas hasil restorasi, terutama dalam hal ketajaman citra dan kemampuan mempertahankan detail.

🚀 Fitur Utama

1. Penambahan 3 jenis noise (Gaussian, Salt & Pepper, Speckle)

2. Implementasi berbagai filter (Mean, Gaussian, Median, Max)

3. Evaluasi otomatis menggunakan MSE, PSNR, SSIM

4. Perbandingan waktu komputasi

5. Visualisasi hasil filtering

🛠️ Teknologi yang Digunakan

1. Python

2. OpenCV

3. NumPy

4. Matplotlib

5. Scikit-image

📊 Tujuan Proyek

Proyek ini bertujuan untuk memahami karakteristik berbagai jenis noise serta menentukan metode filtering yang paling efektif untuk masing-masing kasus, sekaligus menganalisis trade-off antara kualitas citra, detail, dan efisiensi komputasi.
