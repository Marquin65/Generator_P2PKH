import os
import hashlib
import hmac
import tkinter as tk
from tkinter import ttk
from mnemonic import Mnemonic
from ecdsa import SECP256k1, SigningKey
import base58



def generate_mnemonic(num_words):
    
    mnemo = Mnemonic("english")
    return mnemo.generate(strength=(num_words // 3) * 32)

def mnemonic_to_seed(mnemonic, passphrase=""):
    
    return hashlib.pbkdf2_hmac("sha512", mnemonic.encode(), f"mnemonic{passphrase}".encode(), 2048)

def seed_to_private_key(seed):
    
    return hmac.new(b"Bitcoin seed", seed, hashlib.sha512).digest()[:32]

def private_key_to_address(private_key):
    
    sk = SigningKey.from_string(private_key, curve=SECP256k1)
    vk = sk.verifying_key
    public_key = b"\x04" + vk.to_string()  

    sha256_pk = hashlib.sha256(public_key).digest()
    ripemd160_pk = hashlib.new("ripemd160", sha256_pk).digest()
    hashed_public_key = b"\x00" + ripemd160_pk

    checksum = hashlib.sha256(hashlib.sha256(hashed_public_key).digest()).digest()[:4]
    address_bytes = hashed_public_key + checksum

    return base58.b58encode(address_bytes).decode()



def load_existing_addresses(file_path):
   
    with open(file_path, "r") as file:
        return set(line.strip() for line in file.readlines())

def save_match(mnemonic, private_key, address, output_file):
    
    with open(output_file, "a") as file:
        file.write(f"Mnemonic: {mnemonic}\n")
        file.write(f"Private Key: {private_key.hex()}\n")
        file.write(f"Address: {address}\n")
        file.write("\n")

def find_background_image(directory):
    
    for file in os.listdir(directory):
        if file.lower().endswith(('.png', '.gif')):
            return os.path.join(directory, file)
    return None



def create_interface(existing_addresses, output_file):
    
    root = tk.Tk()
    root.title("Bitcoin Address Generator")

    
    image_path = find_background_image(os.getcwd())
    if image_path:
        bg_photo = tk.PhotoImage(file=image_path)
        canvas = tk.Canvas(root, width=1200, height=800)
        canvas.pack(fill=tk.BOTH, expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor=tk.NW)
    else:
        canvas = tk.Canvas(root, width=1200, height=800, bg="black")
        canvas.pack(fill=tk.BOTH, expand=True)

    
    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 16, "bold"), foreground="#FFFFFF", background="#1C1C1C")
    style.configure("TFrame", background="#1C1C1C")
    style.configure("TListbox", font=("Courier", 12), background="#333333", foreground="#00FF00")

    # Títulos e contadores
    titles = ["12 Frases", "15 Frases", "21 Frases", "24 Frases"]
    columns = []
    counts = [0, 0, 0, 0]
    total_matches = [0]  

    
    total_found_label = ttk.Label(canvas, text="Total Matches Encontrado: 0", font=("Helvetica", 14, "bold"), background="#1C1C1C", foreground="#FFD700")
    total_found_label.place(x=500, y=10)

    for i, title in enumerate(titles):
        col_frame = ttk.Frame(canvas)
        col_frame.place(x=50 + i * 280, y=50, width=260, height=700)

        label = ttk.Label(col_frame, text=title, anchor="center")
        label.pack(pady=5)

        listbox = tk.Listbox(col_frame, height=30, width=35, bg="#333333", fg="#00FF00", font=("Courier", 10))
        listbox.pack(fill=tk.BOTH, expand=True)

        count_label = ttk.Label(col_frame, text=f"Matches: 0", anchor="center")
        count_label.pack(pady=5)

        columns.append(listbox)

    
    total_matches_label = ttk.Label(canvas, text="Total Matches: 0", font=("Helvetica", 14, "bold"), background="#1C1C1C", foreground="#FFD700")
    total_matches_label.place(x=500, y=750)

    
    start_generation(existing_addresses, output_file, root, columns, counts, total_matches_label, total_matches, total_found_label)

    
    root.mainloop()



def start_generation(existing_addresses, output_file, root, columns, counts, total_matches_label, total_matches, total_found_label):
    
    mnemonic_word_counts = [12, 15, 21, 24]

    def generate_addresses():
        for i, word_count in enumerate(mnemonic_word_counts):
            for _ in range(10):  # Ajuste o número de iterações conforme necessário
                mnemonic = generate_mnemonic(word_count)
                seed = mnemonic_to_seed(mnemonic)
                private_key = seed_to_private_key(seed)
                address = private_key_to_address(private_key)

                
                columns[i].insert(tk.END, address)
                columns[i].see(tk.END)

                
                if address in existing_addresses:
                    counts[i] += 1
                    total_matches[0] += 1
                    columns[i].insert(tk.END, f"Match Found! Count: {counts[i]}")
                    columns[i].see(tk.END)
                    save_match(mnemonic, private_key, address, output_file)

                   
                    total_matches_label.config(text=f"Total Matches Encontrados: {total_matches[0]}")

                    
                    total_found_label.config(text=f"Total Matches: {total_matches[0]}")

        # Chama novamente para continuar gerando endereços
        root.after(100, generate_addresses)

    generate_addresses()



def main():
    # Caminho para os arquivos de dados
    address_file = "P2PKH.txt"
    output_file = "matches.txt"

    
    existing_addresses = load_existing_addresses(address_file)

    
    create_interface(existing_addresses, output_file)

if __name__ == "__main__":
    main()
