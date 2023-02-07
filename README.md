# Progetto-Editoria-2023
## Introduzione

Questo progetto nasce dalla volontà di preservare e condividere le ricette della tradizione familiare in un formato moderno e accessibile.

Il tutto è iniziato da un libro di ricette posseduto in famiglia da molto tempo (il quale anch'esso derivato a sua volta da un progetto con lo stesso scopo). 

La digitalizzazione delle ricette familiari rappresenta un progetto ambizioso, ma sono convinto che il risultato sia all'altezza delle aspettative. Il ricettario digitale sarà un tesoro di ricordi da conservare per le generazioni future e un prezioso alleato in cucina per tutti gli appassionati.

Grazie alla digitalizzazione, sarà accessibile a chiunque, in qualsiasi momento e luogo, e potrà essere condiviso facilmente con amici e familiari. Siamo certi che questo progetto rappresenterà un contributo importante per la conservazione delle ricette della tradizione familiare e per la diffusione della cultura culinaria.

## Utilizzo

### Fase 1 : Trasformazione

Puoi trovare nella cartella ` Utility`  tutto il necessario per effettuare la conversione, a questo per procedere bisogna aprire una finestra del terminale (possibilmente nella cartella utility) e seguire i seguenti passaggi:

> NB. è necessario aver installato pandoc per poter utilizarre il programma ([pandoc install](https://pandoc.org/installing.html))

1. il primo passo consiste nel mandare in esecuzione il programma python 

   ```
   python /percorso/convertitore.py
   ```

2. una volta premuto invio il programma entrà in esecuzione a questo punto basterà inserire il percorso del file che si vuole convertire :

   ```
   esempi/polpettone-marinara.md
   ```

A questo punto il programma restituisce due output (.html e .xhtml) a questo punto la conversione è completata

### Fase 2 : Inserimento pagina e-book

Per procedere con l'inserimento di una nuova ricetta bisogna eseguire questi semplici passaggi:

> N.B Le istruzioni date qui di seguito si riferiscono al software Sigil,  è un programma consigliato, si può utilizzare un qualsiasi altro editor. [clicca qui](https://sigil-ebook.com/sigil/download/) per andare alla pagina di download

1. Avviare l'editor Sigil
2. Una volta avviata cliccare sull'icona `apri`  a forma ti cartella e selezionare il ricettario.
3. Aprire la cartella `Text `  e col cusore selezionera il punto dove si vuole aggiungere la pagina
4. Una volta evidenziata la posizione bisogna cliccare sull'icona *"aggiungi file esistenti"* a forma di più e selezionare la pagina .xhtml (quella che abbiamo prodotto nella Fase precedente ) che si vuole aggiungere.

### Extra

#### Estrarre contenuto ePub

Sì, puoi estrarre il contenuto di un file epub anche tramite linea di comando utilizzando un tool come "unzip". Se hai un sistema operativo basato su Unix come Linux o macOS, puoi aprire il terminale e utilizzare il seguente comando:

```shell
unzip nome_file.epub
```

#### Unisco file - ePub 

Per creare un file epub a partire da file separati, devi prima raccogliere tutti i file che vuoi includere nel file epub in una cartella. La struttura della cartella deve seguire le specifiche del formato epub, che prevede una struttura di file e cartelle ben definita.

Una volta che hai organizzato i file nella cartella, puoi creare il file epub utilizzando il seguente comando da terminale:

```shell
zip -X0 nome_file.epub mimetype
zip -rDX9 nome_file.epub * -x mimetype
```

