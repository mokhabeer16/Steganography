import cv2

# Load the encrypted image
image_path = "encryptedImage.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Error: Encrypted image not found!")
    exit()

password = input("Enter the original passcode: ")
original_password = input("Enter passcode for Decryption: ")

# Create ASCII-to-character mapping
c = {i: chr(i) for i in range(256)}

height, width, _ = img.shape

message = ""
index = 0

# Decryption process
if password == original_password:
    for i in range(height):
        for j in range(width):
            char = c[img[i, j, 0]]  # Retrieve from the Blue channel (0)
            if char == '\x00':  # Stop if null character is encountered (end of message)
                break
            message += char
            index += 1
    print("Decrypted message:", message)
else:
    print("Unauthorized access! Wrong passcode.")
