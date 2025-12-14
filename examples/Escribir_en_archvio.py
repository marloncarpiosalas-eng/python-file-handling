with open("example1.txt", "a") as file:
    file.write("Adding new text at the end of the file.\n")
    file.write("Appending keeps old content intact.\n")
print("Texto agregado al archivo sin sobrescribirlo.")
