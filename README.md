# Digital Signature Tool
Python application for generating and verifying digital signatures of files using RSA encryption.

## Dependencies
- customtkinter
- rsa
- hashlib
- tkinter
## Usage
1. Clone the repository to your local machine
2. Install the dependencies using pip
3. Run the digital_signature_tool.py file to launch the application
## Functionality
The application offers two main functionalities:

**Signing**: Upload a file and a private key, and the application will generate a digital signature for the file using RSA encryption.

**Verification**: Upload a file, a signature file, and a public key, and the application will verify if the signature matches the file using RSA decryption.
## Signing
To sign a file:

1. Click the "Upload file for signing" button and select the file to sign
2. Click the "Upload private key" button and select the private key file associated with the file
3. Click the "Download file's signature" button to generate the digital signature of the file. The signature will be saved to a file called signature.txt
## Verification
To verify a signature:

1. Click the "Upload file for verification" button and select the file that was signed
2. Click the "Upload public key" button and select the public key file associated with the signature
3. Click the "Verify signature" button to verify if the signature matches the file. The application will display a message indicating whether the signature is valid or invalid.
## Planned Changes
- Remove all global variables in the button functions
- Add functionality to download and upload signature files
- Improve the user interface to make it more intuitive and user-friendly
- Change the color scheme to better represent each action message
- Increase the file size limit
