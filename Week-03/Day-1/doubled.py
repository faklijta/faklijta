# Create a method that decrypts the duplicated-chars.txt
def decrypt(file_name):
    decrypted = ""
    with open(file_name, "r") as f:
        file = f.read()
        for text in range(len(file)-1):
            if file[text] == file [text+1]:
                pass
            else:
                decrypted = decrypted + file[text]
        print(decrypted)
decrypt("duplicated-charts.txt")
