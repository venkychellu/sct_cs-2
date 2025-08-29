from PIL import Image
import numpy as np

# Simple key for pixel manipulation
KEY = 50  

def encrypt_image(image_path, output_path):
    # Open image
    img = Image.open(image_path)
    arr = np.array(img)

    # Apply encryption (simple operation: add key to pixel values)
    encrypted_arr = (arr + KEY) % 256  

    # Save encrypted image
    encrypted_img = Image.fromarray(np.uint8(encrypted_arr))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")


def decrypt_image(image_path, output_path):
    # Open encrypted image
    img = Image.open(image_path)
    arr = np.array(img)

    # Apply decryption (reverse operation: subtract key)
    decrypted_arr = (arr - KEY) % 256  

    # Save decrypted image
    decrypted_img = Image.fromarray(np.uint8(decrypted_arr))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")


# Example usage
if __name__ == "__main__":
    # Provide your own file paths
    encrypt_image("input.png", "encrypted.png")
    decrypt_image("encrypted.png", "decrypted.png")