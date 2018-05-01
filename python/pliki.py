
def generate_html(data):
    source_file = open(r"C:\Users\eszal\Documents\projekty\tabelka_repo\tabelka.html","r")
    code_tabelki = source_file.readlines()

    source_file.close()
    target_file = open("tabelka2.html","w")
    for line in code_tabelki:
        if line == "###Table_Data###\n":
            target_file.write(generate_table_html(data))
        else:
            target_file.write(line)
    target_file.close()

def generate_table_html(rows):
    code_html = ""
    for row in rows:
        code_html += generate_row_html(row)
    return code_html

def generate_row_html(row_data):
    html_code = ''
    html_code += '<tr>' + "\n"
    for element in row_data:
        html_code += "<td>" + element + "</td>" + "\n"
    html_code += "</tr>"+ "\n"
    return html_code

# print (generate_row_html(dane[0]))



# (generate_table_html(dane))

dane = [["12.03.18", 'makaron', 'Jedzenie', '5'],
       ['30.12.18', 'jablko', 'Jedzenie', '78']]

generate_html(dane)





