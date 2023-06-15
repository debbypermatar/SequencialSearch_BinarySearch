def find_phone_number(name, phone_book):
    for contact_name, phone_number in phone_book.items():
        if contact_name == name:
            return phone_number
    return None

# Daftar Buku telepon
phone_book = {
    "John Doe": "081234567890",
    "Jane Smith": "089876543210",
    "Michael Johnson": "087811223344",
    "Emily Davis": "082122232425"
}

# Nama yang ingin dicari nomor teleponnya
name = "Jane Smith"

# Menemukan nomor telepon Jane
phone_number = find_phone_number(name, phone_book)

# Menampilkan nomor telepon Jane
if phone_number:
    print("Nomor telepon", name, "adalah", phone_number)
else:
    print("Nomor telepon", name, "tidak ditemukan.")
