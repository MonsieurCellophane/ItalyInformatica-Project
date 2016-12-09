# Prototipo per backend progetto Italy-Informatica.

Vedi: https://www.reddit.com/r/ItalyInformatica/search?q=progettone&restrict_sr=on&sort=relevance&t=all


## Stato di avanzamento e descrizione

 * In Django
  * Al momento è uno stub di autenticazione
  * Modellato^1 su JWT con considerevoli semplificazioni
  * L'endpoint accetta^2 username/password, restituisce un token
  * il token è composto da:
     * hmac/sha256 di un payload concatenato (con una virgola) a 
     * payload consistente di un array json codificato in hex
     * l'array json contiene username, sessionkey per aggiungere rumore, e timestamp
  * il token è da usare^2 per le richieste seguenti
  * in fase di verifica:
     * vengono separati hmac e payload
     * si verifica l'esistenza e dello username nel backend auth di Django
     * si controlla^3 l'età del token e...(TBD)

Cosa fa:

  * Espone due API browsabili per [ottenere](http://localhost:8000/api/auth/token/) e [verificare](http://localhost:8000/api/auth/verify/) un token.
  

Cosa manca:

  * Test
  * Browsable APIs
  * Endpoint per registrazione, lettura e creazione profilo...
  * Tutto il resto

---

1) A shameless rip from django-rest-jwt, really

2) Ma ancora non è deciso come

4) Ma è da scrivere

5) Ma anche senza test, quindi qualche runtime è assicurato.


## Rapidi cenni d'installazione (linux) in un virtualenv.

(Su sistemi redhat-like, i comandi mkvirtualenv e workon sono nel pacchetto virtualenv-wrapper)

     $ https://github.com/MonsieurCellophane/ItalyInformatica-Project
     $ cd ItalyInformatica-Project
     $ mkvirtualenv IIP
     $ workon IIP
     (IIP)$ pip install -r requirements.txt
     (IIP)$ python manage.py runserver

Effettuare il browse di:

http://localhost:8000/api/auth/token/
http://localhost:8000/api/auth/verify/

usare utente admin, password Cellophane.
