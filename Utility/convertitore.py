import os
from bs4 import BeautifulSoup

# Chiede all'utente il nome del file di input
input_file_name = input("Inserisci il nome del file di input (in formato Markdown): ")

# Chiede all'utente il nome del file di output
# output_file_name = input("Inserisci il nome del file di output: ");
# output_file_name = output_file_name+".html"

output_file_name = input_file_name[:-2]+"html"


# Esegue la conversione del file Markdown in HTML
os.system(f"pandoc -s {input_file_name} --metadata-file=metadata.txt -o {output_file_name}")

# Apre il file HTML
with open(output_file_name) as f:
    soup = BeautifulSoup(f, "html.parser")

# Cerca il tag style e lo rimuove
for tag in soup("style"):
    tag.decompose()

output_file_name = output_file_name[:-4]+"xhtml"

#Esegue la conversione del file HTML in XHTML
os.system(f"pandoc -s {input_file_name} --metadata-file=metadata.txt -o {output_file_name}")

# Salva il file HTML con il nuovo tag link
with open(output_file_name, "w") as f:
    f.write(str(soup))
