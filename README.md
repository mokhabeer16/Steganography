🔐 Image Steganography: Message Encryption and Decryption
This project demonstrates image steganography, where a secret message is hidden inside an image using encryption and later retrieved using decryption.

📁 Project Structure
pgsql
Copy
Edit
.
├── encryption.py        # Encrypts a secret message into an image
├── decryption.py        # Decrypts the message from the encrypted image
├── mypic.jpg            # Source image for encryption (Replace with your image)
└── README.md            # Project documentation
🚀 How to Use
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/image-steganography.git
cd image-steganography
2. Install Required Libraries
Make sure you have OpenCV installed:

bash
Copy
Edit
pip install opencv-python
3. Run Encryption Script
bash
Copy
Edit
python encryption.py
Input: Secret message and a passcode.
Output: encryptedImage.jpg with the hidden message.
4. Run Decryption Script
bash
Copy
Edit
python decryption.py
Input: Passcode for decryption.
Output: Displays the hidden message if the passcode is correct.
📸 Example
Encryption:

Message: Hello, World!
Passcode: 1234
Result: encryptedImage.jpg is created.
Decryption:

Enter the correct passcode (1234).
Output: Decrypted message: Hello, World!
⚠️ Important Notes
Ensure mypic.jpg is present in the project directory before running encryption.py.
The passcode used in decryption must match the passcode used during encryption.
🎯 Future Improvements
Add support for longer messages.
Enhance security with advanced encryption methods.
Implement a GUI for better usability.
