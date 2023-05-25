def search_definition(word, dictionary):
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        mid = (left + right) // 2

        if dictionary[mid][0] == word:
            return dictionary[mid][1]
        elif dictionary[mid][0] < word:
            left = mid + 1
        else:
            right = mid - 1

    return "Definisi tidak ditemukan."


# Kamus dalam bentuk daftar yang sudah diurutkan berdasarkan kata kunci
dictionary = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

# Kata yang ingin dicari definisinya
word = "Duck"

# Mencari definisi kata
definition = search_definition(word, dictionary)

# Menampilkan definisi kata
print("Definisi dari kata", word, "adalah:", definition)
