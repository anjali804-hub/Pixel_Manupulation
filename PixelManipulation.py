from PIL import Image

# Function to encrypt the image
def encrypt_image(image_path, shift_value, output_path):
    try:
        # Open the image
        img = Image.open(image_path)
        img = img.convert("RGB")  # Ensure it's in RGB mode
        
        # Load pixel data
        pixels = img.load()
        
        # Encrypt the image by modifying pixel values
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                
                # Apply the shift value to RGB channels (use modulo 256 to avoid overflow)
                r = (r + shift_value) % 256
                g = (g + shift_value) % 256
                b = (b + shift_value) % 256
                
                # Set the new pixel value
                pixels[i, j] = (r, g, b)
        
        # Save the encrypted image
        img.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to decrypt the image
def decrypt_image(image_path, shift_value, output_path):
    try:
        # Open the image
        img = Image.open(image_path)
        img = img.convert("RGB")  # Ensure it's in RGB mode
        
        # Load pixel data
        pixels = img.load()
        
        # Decrypt the image by reversing the pixel manipulation
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                
                # Reverse the shift operation (use modulo 256 to stay within valid pixel range)
                r = (r - shift_value) % 256
                g = (g - shift_value) % 256
                b = (b - shift_value) % 256
                
                # Set the new pixel value
                pixels[i, j] = (r, g, b)
        
        # Save the decrypted image
        img.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to handle user input
def main():
    print("Simple Image Encryption Tool")

    choice = input("Do you want to encrypt or decrypt an image? (E/D): ").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice. Please select 'E' for encryption or 'D' for decryption.")
        return

    # Take the image path from the user
    image_path = input("Enter the path of the image file (e.g., C:\\Users\\Anjali G\\Pictures\\PHOTO.jpg): ")
    
    # Take the shift value (integer) from the user
    shift_value = int(input("Enter the shift value (an integer): "))
    
    # Take the output path from the user for saving the modified image
    output_path = input("Enter the output path for the modified image (e.g., C:\\Users\\Anjali G\\Pictures\\PHOTO_encrypted.jpg): ")

    # Perform encryption or decryption
    if choice == 'E':
        encrypt_image(image_path, shift_value, output_path)
    elif choice == 'D':
        decrypt_image(image_path, shift_value, output_path)

if __name__ == "__main__":
    main()
