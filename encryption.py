import cv2
import os

# Load the image
image_path = "C:/Users/mokhabeer/Desktop/project/mypic.jpg"  # Replace with the correct image path
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create character-to-ASCII mapping
d = {chr(i): i for i in range(256)}

height, width, _ = img.shape

# Ensure the image has enough pixels to store the message
if len(msg) > height * width:
    print("Error: Message is too long for the image size!")
    exit()

# Encrypt the message into the image
index = 0
for i in range(height):
    for j in range(width):
        if index < len(msg):
            img[i, j, 0] = d[msg[index]]  # Store in the Blue channel (0)
            index += 1

output_path = "encryptedImage.jpg"
cv2.imwrite(output_path, img)
print(f"Image saved as '{output_path}'.")
os.system(f"start {output_path}")

