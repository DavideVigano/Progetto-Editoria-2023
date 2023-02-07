` Università degli Studi di Milano` ` Corso di Editoria Digitale`  ` 2022-2023` ` Davide Vigano' 954776`

` https://github.com/DavideVigano/Progetto-Editoria-2023`   

# Ricettario Misto

## Introduzione

Questo progetto nasce dalla volontà di preservare e condividere le ricette della tradizione familiare in un formato moderno e accessibile.

Il tutto è iniziato da un libro di ricette posseduto in famiglia da molto tempo (il quale anch'esso derivato a sua volta da un progetto con lo stesso scopo). 

Inizialmente le ricette sono state trascritte da cartacee in formato Markdown preservando la struttura semplice ma intuitiva che l'autore ha precedentemente scelto.
Successivamente i file contenenti le ricette sono stati trasformati (tramite opportuno script in Python) attraverso la libreria pandoc nel formato XHTML per poi essere riorganizzati e formattati tramite il software Sigil, per poi essere esportati nel formato di destinazione, ovvero epub3 con l'obiettivo di rendere questo ricettario facilmente consultabile su qualsiasi dispositivo digitale.

Il formato epub3 ci permette di arricchire le ricette con immagini e video, rendendo ancora più piacevole la loro consultazione.

Ovviamente il progetto non si ferma alla digitalizzazione di un singolo ricettario, ma il suo scopo è quello di rendere quest'ultimo modulabile per permettere a un qualsiasi utente di arricchirlo con le proprie ricette.

La digitalizzazione delle ricette familiari rappresenta un progetto ambizioso, ma sono convinto che il risultato sia all'altezza delle aspettative. Il ricettario digitale sarà un tesoro di ricordi da conservare per le generazioni future e un prezioso alleato in cucina per tutti gli appassionati.

Grazie alla digitalizzazione, sarà accessibile a chiunque, in qualsiasi momento e luogo, e potrà essere condiviso facilmente con amici e familiari. Siamo certi che questo progetto rappresenterà un contributo importante per la conservazione delle ricette della tradizione familiare e per la diffusione della cultura culinaria.

Qui di seguido verrano elencate più nel dettaglio le informazioni riguardanti il progetto e il suo sviluppo.

## Processo di Produzione

Il processo di produzione ha avuto inizio con lo **<u>studio e analisi del tema</u>**, in questa fase, l'obiettivo è quello di capire meglio l'argomento che si vole trattare e fare degli studi a riguardo.

Si è partiti inzanzitutto definendo ***<u>destinatari e analisi dei requisiti</u>* :**

Lo <u>scopo</u> di questo progetto è quello di preservare e condividere le ricette della tradizione familiare in un formato moderno e accessibile.

Il <u>targhet di utenti</u> a cui si fa riferimento sono coloro interessati alla cucina o coloro che vogliono preservare le memorie del passato attraverso la digitalizzazione, per questo, per dare la possibilità a tutti gli utenti di visionare l'e-book esso dovrà essere utilizzabile su dispositivi eterogenei. 

<u>Requisiti:</u>

Nel ricettario digitale dovrà essere possibile visionare le ricette, le quali dovranno essere indicizzate e catalogate, a seconda del caso si deve poter mostrare anche materiale di supporto per l'utente come immagini, ma in particolar modo video che mostrano passo passo la preparazione delle varie ricette. 

Inoltre dovrà essere possibile attraverso opportuni metodi, specificati nella guida, aggiungere ricette e materiale di supporto. 

Un aspetto importante che l'applicazione deve considerare è l'esperienza utente, ovvero l'utilizzo dell' e-book da parte dell'utente dovrà risultare dal suo punto di vista piacevole e di facile comprensione senza trascurare efficienza ed affidabilità.

Successivamente dopo la definizione dei destinatare e l'analisi dei requisiti si è passato allo studio dei **<u>*competitor*</u>** nel quale si è concluso che al momento non esistono molte realtà simili e le poche che ci sono non utilizzano a pieno le nuove tecnologie disponibili sul mercato. 

A questo punto dopo le varie analisi e la scelta degli obbiettivi da raggiungere si è scelto di puntare sulle seguenti <u>***tecnologie***</u> :

- Il liguaggio <u>Markdown</u> per la trascrizione dal formato cartaceo.
- <u>XHTML</u> per la scrittura delle pagine accompagnato da <u>CSS</u> e <u>JavaScript</u>
- la libreria <u>Pandoc</u> per la trasformazione da Markdown a XHTML
- <u>epub3</u>  come formato di destinazione 
- <u>Sigil</u> come software per la modifica e aggiunta di pagine. 

In particolar modo Il liguaggio <u>Markdown</u>, <u>XHTML</u>,  <u>CSS</u> e <u>JavaScript</u> sono stati scelti per la loro sempicità portabilità e facilità di scrittura, mentre è stato scelto <u>epub3</u> come formato di destinzazione perchè quest'ultimo (a differenza dei suoi predecessori) ci permette di arricchire il contenuto del libro con contenuti interattivi, superando la staticità di un classico ricettario. Inoltre come supporto sono stati scelti <u>Pandoc</u> e <u>Sigil</u>. Il primo permette di effettuare trasformazioni in modo rapido e preciso ma soprattutto supporta molte altre trasformazioni e questo rende il nostro progetto espandibile (come il supporto di diversi formati in input, come HTML, TXT, DOCX, ecc.. ); Mentre la scelta di  <u>Sigil</u> è dovuta dal fatto che è un software completamente open source e permette l'editing tramite un interfaccia molto ben strutturata e di facile comprensione.

Infine per il <u>***modello di business***</u> momentaneamente (per consentire la realizzazione del progetto), si è optato della libera fruizione del contenuto a tutti coloro che ne partecipino in alterntiva sarà possibile acquistare l'accesso. 

La Seconda fase è stata quella **<u>stesura della bozza</u>** qui inizialmente sono state trascritte dal formato cartaceo in md e dopo varie trasformazioni sono state trasportate nel formato di destinazione (epub3). 

È stato scelto un template da rispettare per la scrittura delle ricette e uno per come suddividere il libro (si è deciso di rispettare quello del libro originale). 

Sono stati selezionati i vari elementi dei multimedialità come la scelta delle varie immagini da inserire nelle ricette e come suddivisione delle varie categorie. 

Infine sono stati aggiunti tutti quegli elementi di navigabilità che permetono di rispettare i requisiti sopra citati.

Successivamente si è passati alla fase della <u>**revisione dei contenuti**</u> tramite la quale è stato possibile apportare correzioni alla bozza. 

In particolar modo è stata verificata la coerenza con l'analisi dei requisiti e dove quest'ultima mancava sono state aggiunte le varie funzionalità. 

In particolar modo si è tenuto conto della correttezza e dell'implementazione dei vari contenuti di navigabilità. 

Al passo successivo si è definito lo **<u>stile grafico</u>** da rispettare, esso dovrà essere garantito uguale per tutte le ricette, anche quelle inserite dagli utenti successivamente. 

una volta applicato lo stile grafico è stato creato il **<u>formato di distribuzione</u>**. 
In questo procedimento sono stati inseriti i metadati descrittivi, è stata scelta la copertina dell'e-book, redatto un breve manuale per l'utilizzo del sistema ed infine è stato compilato, il tutto tramite Sigil. 

Concluso ciò il progetto sarà pronto per la **<u>distribuzione e la promozione</u>** attraverso diversi canali, come social media o eventi culinari. 

È importante notare che vi sarà uno  **<u>sviluppo continuo</u>**, infatti il progetto non si ferma alla pubblicazione, ma prevede anche la modifica e l'arricchimento da parte degli utenti.

## Gestione documentale

Qui di seguito di può trovare un flusso di gestione, il quale illustra come viene aggiunta una ricetta all'interno del ricettario 

<img src="/Users/davidevigano/Downloads/diagram.svg" alt="diagram" style="zoom:200%;" />



## Tecnologie adottate

L'applicazione che è stata progettata è fortemente intercambiabile, quindi molte delle sue scelte tecnologiche possono essere cambiate o implementate con altre soluzioni ed è importante sottolineare che non dipende da formati propietari. 

Le tecnologie adottate sono molteplici, inanzitutto è stato scelto **markdown** come formato di scrittura, la scelta è dovuta dal fatto che questo linguaggio è semplice da utilizare e di facile comprensione oltre alla portabilità e le numerose possibilità di conversione (già implementate) quindi tramite opportune librerie (vedi pandoc) è possibile effettuare la trasformazione evitando di utilizarre XSLT. 

mentre per le pagine del libro vi erano due soluzioni (dovute al fatto che il formato di destinazione è epub3) 

- HTML
- **XHTML** 

entrambi i linguaggi sono molto simili la differenza principale tra HTML e XHTML è la sintassi: XHTML è un'evoluzione più rigorosa di HTML e segue strettamente le regole del XML (eXtensible Markup Language). Ciò significa che XHTML ha una sintassi più rigorosa e strutturata rispetto a HTML, e gli elementi devono essere chiusi correttamente.

Dato che il formato epub3 richiede che le proprie pagine siano privi di errori se no quest'ultime non vengono visualizzate correttamente in un ebook reader (a differenza di un qualsiasi browser), la scelta è ricaduta su **XHTML** il quale se la sintassi non è corretta non permette la generazione del e-book evidenziandone l'errore. 

Per la trasformazione dal formato markdown a XHTML invece si è optato per l'utilizzo di **pandoc** il quale essendo un software open source non dipende da formati propietari ma in particolar modo grazie alle sue caratteristiche di conversione, ovvero che supporta  molti formati di input e output rende il tutto modulabile e con la possibilità di ampliare il progetto con altri formati. 

Per facitare l'uso di pandoc è disponibile un piccolo programma in python il quale riceve in input il file in formato markdown e restituisce il file in formato XHTML il quale è già provvisto delle dichiarazioni di stile per uniformarmare tutte le pagine. 

> NB. è necessario aver installato pandoc per poter utilizarre il programma ([pandoc install](https://pandoc.org/installing.html))

Invece per l'aggiunta delle pagine vi erano diverse soluzioni:

- tramite linea di comando 
- creare un interfaccia apposita
- utilizzo di un softwar editor 

La prima è stata scartata dal semplice fatto che il targhet di cliente previsto non è per forza un utente esperto e l'utilizzo di questa soluzione richiedeva alcune competenze di informatica di base che molti utenti potrebbero non esserne a conoscenza. 

La seconda invece poteva essere un ottima soluzione (in futuro potrebbe essere implementata) a livello di usabilità ma sarebbe stata dispendiosa in termini di costi,tempi ed efficienza quindi si è optato per l'utilizzo di un softwar editor (anch'esso open source). La scelta è ricaduta su **Sigil**,  Sigil è un editor WYSIWYG (What You See Is What You Get) gratuito e open source per la creazione di libri elettronici in formato ePub. Con Sigil, gli utenti possono creare libri ma soprattuto modificare gli ebook senza la necessità di conoscere alcun tipo di linguaggio, basta utilizzare l'interfaccia grafica per eseguire le diverse operazioni, maggiori dettagli sono dati nel file rea dme.md del repository. 

> N.B Sigil è un programma consigliato, si può utilizzare un qualsiasi altro editor. [clicca qui](https://sigil-ebook.com/sigil/download/) per andare alla pagina di download

Infine la scelta del formato di destinazione è stata quella di utilizzare il formato **epub**, in particolar modo la versione **3**.
Questa scelta ha influenzato molto le scelte delle precedenti tencologia ed è stata optata per per le seguenti motivazioni :

- formato open source 
- ampiamente suppurtato (da pc a smartphone passando dai book reader fino ai browser con oppurtune estensioni)

In particolare la versione 3 supporta:

- audio e video integrati
- una maggiore accessibilità per i non vedenti
- la possibilità di creare libri interattivi 
- maggiore interoperabilità tra diversi dispositivi e sistemi operativi.

Inoltre la gestione del versionig è stata gestita tramite git hub. 

## Concluisoni

I risultati ottenuti in termini tecnici da questo progetto sono abbastanza soddisfacenti, la maggior parte degli obbiettivi prefissati sono stati raggiunti, i principali da evidenziare sono:

- l'indicizzate e la catalogalizzazione delle ricette
- l'introduzione di video 
- creare un esperienza utente piacevole e user-friendly 
- l'utilizzo di tecnologie open source 
- la possibilità di un utente di partecipare alla creazione del Ricettario 
- l'elevata modularità e portabilità 

Ovviamente il progetto può essere migliorato ed esteso, per esempio ampliando i formati di input che questo riceve per la trasformazione, la possibilità di aggiungere pagine e file multimediali senza l'utilizzo di Sigil ma attraverso un interfaccia web ecc.. 

Nel corso dello sviluppo del progetto sono state riscontrate alcune limitazioni in termini di compatibilità una fra tutte è quella di javascript il quale non è implementato in modo da poter utilizzare tutte le sue potenzialità a causa sia del formato epub3 che dei principali book-reader. A causa di ciò nel progetto iniziale non è stato possibile introdurre funzioni avanzate di filtro (ex mostrami una ricetta che ha i seguenti ingredienti) ma anche dei semplici bottoni cono delle funzioni annesse (ex mostra / nascondi un certo elemento). 

In conclusione, questo progetto di digitalizzazione delle ricette rappresenta un passo importante verso la preservazione e la diffusione della cultura culinaria.

 La trasformazione delle ricette dal formato cartaceo a quello digitale rende queste ultime facilmente accessibili e condivisibili, preservandole per le generazioni future. 

Il formato epub3 permette inoltre di arricchire le ricette con immagini e video, rendendole ancora più piacevoli da consultare. Il progetto non si ferma alla digitalizzazione di un singolo ricettario, ma mira a diventare uno strumento modulabile e collaborativo. 

Grazie alla sua realizzazione, la tradizione culinaria sarà conservata e condivisa con sempre maggiore facilità.

## Bibliografia e sitografia

### Bibliografia

1. Anna, Rosa. Quaderno di economia domestica. I.S. Caterina da Siena, *undefine*.

### Sitografia

1. [Markdow](https://it.wikipedia.org/wiki/Markdown)

2. [XHTML e HTML]( https://www.w3.org/International/articles/serving-xhtml/index.en.html)

3. [pandoc](https://pandoc.org/index.html)
4. [Sigil](https://sigil-ebook.com/sigil/)
5. [epub e epub3](https://it.wikipedia.org/wiki/EPub)





