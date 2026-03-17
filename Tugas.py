import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
from skimage.metrics import structural_similarity as ssim

image = cv2.imread('Minggu 5/image.jpg', cv2.IMREAD_GRAYSCALE)
image = image / 255.0

def add_gaussian_noise(img, mean=0, sigma=0.05):
    noise = np.random.normal(mean, sigma, img.shape)
    noisy = img + noise
    return np.clip(noisy, 0, 1)

def add_salt_pepper_noise(img, amount=0.05):
    noisy = img.copy()
    num_salt = int(amount * img.size * 0.5)
    num_pepper = int(amount * img.size * 0.5)

    coords = [np.random.randint(0, i, num_salt) for i in img.shape]
    noisy[coords[0], coords[1]] = 1

    coords = [np.random.randint(0, i, num_pepper) for i in img.shape]
    noisy[coords[0], coords[1]] = 0

    return noisy

def add_speckle_noise(img):
    noise = np.random.randn(*img.shape)
    noisy = img + img * noise
    return np.clip(noisy, 0, 1)

gaussian_noise = add_gaussian_noise(image)
sp_noise = add_salt_pepper_noise(image)
speckle_noise = add_speckle_noise(image)

# Mean Filter
def mean_filter(img, ksize):
    return cv2.blur(img, (ksize, ksize))

# Gaussian Filter
def gaussian_filter(img, ksize, sigma):
    return cv2.GaussianBlur(img, (ksize, ksize), sigma)

# Median Filter
def median_filter(img, ksize):
    img_uint8 = (img * 255).astype(np.uint8)
    filtered = cv2.medianBlur(img_uint8, ksize)
    return filtered / 255.0

# Max Filter (Non-linear)
def max_filter(img, ksize):
    kernel = np.ones((ksize, ksize), np.uint8)
    return cv2.dilate(img, kernel)

def mse(original, processed):
    return np.mean((original - processed) ** 2)

def psnr(original, processed):
    m = mse(original, processed)
    if m == 0:
        return 100
    return 10 * np.log10(1.0 / m)

def compute_ssim(original, processed):
    return ssim(original, processed, data_range=1.0)

def evaluate_filter(original, noisy, filter_func, *args):
    start = time.time()
    result = filter_func(noisy, *args)
    end = time.time()

    return {
        "result": result,
        "MSE": mse(original, result),
        "PSNR": psnr(original, result),
        "SSIM": compute_ssim(original, result),
        "Time": end - start
    }

results = {}

noises = {
    "Gaussian": gaussian_noise,
    "SaltPepper": sp_noise,
    "Speckle": speckle_noise
}

for noise_name, noisy_img in noises.items():
    results[noise_name] = {
        "Mean_3": evaluate_filter(image, noisy_img, mean_filter, 3),
        "Mean_5": evaluate_filter(image, noisy_img, mean_filter, 5),
        "Gaussian_3_1": evaluate_filter(image, noisy_img, gaussian_filter, 3, 1),
        "Gaussian_5_2": evaluate_filter(image, noisy_img, gaussian_filter, 5, 2),
        "Median_3": evaluate_filter(image, noisy_img, median_filter, 3),
        "Median_5": evaluate_filter(image, noisy_img, median_filter, 5),
        "Max_3": evaluate_filter(image, noisy_img, max_filter, 3),
    }

for noise in results:
    print(f"\n=== Noise: {noise} ===")
    for method in results[noise]:
        r = results[noise][method]
        print(f"{method} -> MSE: {r['MSE']:.5f}, PSNR: {r['PSNR']:.2f}, SSIM: {r['SSIM']:.4f}, Time: {r['Time']:.5f}s")

def show_images(original, noisy, results_dict, title):
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 3, 1)
    plt.imshow(original, cmap='gray')
    plt.title("Original")

    plt.subplot(3, 3, 2)
    plt.imshow(noisy, cmap='gray')
    plt.title("Noisy")

    i = 3
    for method in results_dict:
        plt.subplot(3, 3, i)
        plt.imshow(results_dict[method]["result"], cmap='gray')
        plt.title(method)
        i += 1
        if i > 9:
            break

    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

# Tampilkan untuk tiap noise
show_images(image, gaussian_noise, results["Gaussian"], "Gaussian Noise")
show_images(image, sp_noise, results["SaltPepper"], "Salt & Pepper Noise")
show_images(image, speckle_noise, results["Speckle"], "Speckle Noise")