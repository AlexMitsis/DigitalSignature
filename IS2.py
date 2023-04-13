import customtkinter
import rsa
from hashlib import sha512
from tkinter import filedialog


def UploadFileToSign():
    global hash
    file_to_open = filedialog.askopenfile()
    with open(file_to_open.name, 'rb') as original_file:
        file_to_sign = original_file.read()
        print(file_to_sign)
        hash = int.from_bytes(sha512(file_to_sign).digest(), byteorder='big')
        print(hash)
    label = customtkinter.CTkLabel(master=frame_1, text="File uploaded", justify=customtkinter.LEFT)
    label.pack(pady=10, padx=10)
        
def UploadPublicKey():
    global private_key
    file_to_open = filedialog.askopenfile()
    # private_key = filedialog.askopenfile()
    with open(file_to_open.name, 'rb') as private_key_file:
        private_key = rsa.PrivateKey.load_pkcs1(private_key_file.read())
        # private_key = private_key_file.read()
        print(private_key)
    label = customtkinter.CTkLabel(master=frame_1, text="Private key uploaded", justify=customtkinter.LEFT)
    label.pack(pady=10, padx=10)
        
def DownloadFileSignature():
    global signature
    signature = pow(hash, private_key.d, private_key.n)
    print("Signature:", hex(signature))
    with open('signature.txt', 'w') as signature_file:
        signature_file.write(hex(signature))
    label = customtkinter.CTkLabel(master=frame_1, text="Signature generated", justify=customtkinter.LEFT)
    label.pack(pady=10, padx=10)

def UploadFileToVerify():
    global hash_to_verify
    file_to_open = filedialog.askopenfile()
    with open(file_to_open.name, 'rb') as original_file:
        file_to_verify = original_file.read()
        print(file_to_verify)
        hash_to_verify = int.from_bytes(sha512(file_to_verify).digest(), byteorder='big')
        print(hash_to_verify)
    label = customtkinter.CTkLabel(master=frame_1, text="File uploaded for verification", justify=customtkinter.LEFT)
    label.pack(pady=10, padx=10)

def UploadFileSignatureToVerify():
    global public_key
    file_to_open = filedialog.askopenfile()
    with open(file_to_open.name, 'rb') as public_key_file:
        public_key = rsa.PublicKey.load_pkcs1(public_key_file.read())
        print(public_key)
    label = customtkinter.CTkLabel(master=frame_1, text="Public key uploaded for verification", justify=customtkinter.LEFT)
    label.pack(pady=10, padx=10)

def VerifySignature():
    print("signature:")
    print(signature)
    print("hash to verify:")
    print(hash_to_verify)
    # print(pow(hash_to_verify, public_key.e, public_key.n))
    print("Signature valid:", hash_to_verify == pow(signature, public_key.e, public_key.n))
    if(hash_to_verify == pow(signature, public_key.e, public_key.n)):
        label = customtkinter.CTkLabel(master=frame_1, text="Valid Signature", justify=customtkinter.LEFT)
        label.pack(pady=10, padx=10)
    else:
        label = customtkinter.CTkLabel(master=frame_1, text="Invalid Signature", justify=customtkinter.LEFT)
        label.pack(pady=10, padx=10)


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("1920x1080")

app.title("CustomTkinter simple_example.py")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Digital Signature", justify=customtkinter.LEFT)
label_1.pack(pady=10, padx=10)


#!! BUTTONS
button_1 = customtkinter.CTkButton(master=frame_1, text="Upload file for signing", command= UploadFileToSign)
button_1.pack(pady=10, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, text="Upload public key", command=UploadPublicKey)
button_2.pack(pady=10, padx=10)

button_3 = customtkinter.CTkButton(master=frame_1, text="Download file's signature", command=DownloadFileSignature)
button_3.pack(pady=10, padx=10)

button_4 = customtkinter.CTkButton(master=frame_1, text="Upload file for verification", command=UploadFileToVerify)
button_4.pack(pady=10, padx=10)

button_5 = customtkinter.CTkButton(master=frame_1, text="Upload file's signature", command=UploadFileSignatureToVerify)
button_5.pack(pady=10, padx=10)

button_6 = customtkinter.CTkButton(master=frame_1, text="Check signature correctness", command=VerifySignature)
button_6.pack(pady=10, padx=10)

label_2 = customtkinter.CTkLabel(master=frame_1, text="Action messages", justify=customtkinter.LEFT)
label_2.pack(pady=10, padx=10)

app.mainloop()


# !! sources: https://cryptobook.nakov.com/asymmetric-key-ciphers/the-rsa-cryptosystem-concepts