source_file = open(r"C:\Users\eszal\Documents\projekty\tabelka_repo\tabelka.html","r")

code_tabelki = source_file.read()

source_file.close()

target_file = open("tabelka2.html","w")

target_file.write(code_tabelki)

target_file.close()




# for line in code_tabelki:


