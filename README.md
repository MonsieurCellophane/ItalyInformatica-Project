# Prototipo per backend progetto Italy-Informatica.

Vedi: https://www.reddit.com/r/ItalyInformatica/search?q=progettone&restrict_sr=on&sort=relevance&t=all


## Stato di avanzamento e descrizione

 * In Django
  * Al momento è uno stub di autenticazione
  * Modellato(1) su JWT con considerevoli semplificazioni
  * L'endpoint accetta username/password, restituisce un token
  * il token è composto da:
     * hmac/sha256 di un payload concatenato (con una virgola) a 
     * payload consistente di un array json codificato Base64
     * l'array json contiene username, sessionkey per aggiungere rumore, e timestamp
  * il token [viene utilizzato per le richieste seguenti](wiki/Come-effettuare-una-richiesta-autenticata)
  * in fase di verifica:
     * vengono separati hmac e payload
     * si verifica l'esistenza e dello username nel backend auth di Django
     * si controlla(2) l'età del token e...(TBD)

Cosa fa:

  * Espone due API browsabili per [ottenere](http://localhost:8000/api/auth/token/) e [verificare](http://localhost:8000/api/auth/verify/) un token.
  

Cosa manca la funzionalità minima:

  * Endpoint per registrazione, lettura e creazione profilo...

---

1) A shameless rip from django-rest-jwt, really

2) Ma ancora non è deciso come



##  Installazione e setup (linux).

E' richiesta una macchina Linux con python2.7 e git.

Le istruzioni che seguono presuppongono l'uso di [virtualenv](http://virtualenv.readthedocs.io/en/stable/) e del comodo [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/). Fare senza è (forse) possibile, ma sconsigliato (ad esempio perchè è impossibile o scomodissimo il freeze delle versioni, che per i vari pacchetti sono le latest alla data 2016-12-02).

Per sistemi redhat-like (RH, CentOS, Fedora) il setup dei predetti si fa come segue:

     $ sudo yum install pip python-virtualenv python-virtualenvwrapper 
     $ source /etc/profile.d/virtualenvwrapper.sh

ovvero:

     $ sudo dnf install pip python2-virtualenv python2-virtualenvwrapper 
     $ source /etc/profile.d/virtualenvwrapper.sh

Per Ubuntu (e altri debian-like: ma chi usa debian non sta neanche leggendo questo paragrafo, giusto?), vedere ad esempio [questo link](http://askubuntu.com/questions/244641/how-to-set-up-and-use-a-virtual-python-environment-in-ubuntu).

     $ cd [some-development-dir]
     $ git clone https://github.com/MonsieurCellophane/ItalyInformatica-Project
     $ cd ItalyInformatica-Project
     $ mkvirtualenv IIP
     $ workon IIP
     (IIP)$ pip install -r requirements.txt
     (IIP)$ python manage.py runserver

## Come provarlo

In una finestra di shell:

    (IIP) $ python manage.py runserver

In un'altra finestra, sempre dal folder di progetto:

    (IIP) $ bin/test-token.sh admin Cellophane

output atteso:

    ****************
    * Obtain token *
    ****************
    HTTP/1.0 200 OK
    Allow: POST, OPTIONS
    Content-Type: application/json
    Date: Sat, 10 Dec 2016 07:00:45 GMT
    Server: WSGIServer/0.1 Python/2.7.12
    Vary: Accept
    X-Frame-Options: SAMEORIGIN

    {
	"token": "8bb8570fb35dab82ad3653c23244d39f5eac73863c257b4aeff1d668a87cd726,7b22757365726e616d65223a202261646d696e222c202274696d657374616d70223a2022313438313335333234352e30222c202273657373696f6e6b6579223a2022664876546f62685a366336316f715845227d"
    }

    ****************
    * Verify token *
    ****************
    HTTP/1.0 200 OK
    Allow: POST, OPTIONS
    Content-Type: application/json
    Date: Sat, 10 Dec 2016 07:00:45 GMT
    Server: WSGIServer/0.1 Python/2.7.12
    Vary: Accept
    X-Frame-Options: SAMEORIGIN

    {
	"timestamp": "1481353244.46", 
	"token": "988b6ea17d49615b06d6a8dbfd4a7d0cb2cae17b112723e6b0782a8e2dec42db,7b22757365726e616d65223a202261646d696e222c202274696d657374616d70223a2022313438313335333234342e3436222c202273657373696f6e6b6579223a20224a763333674b6336793663566c51576a227d", 
	"user": {
	    "email": "plastic@glass.org", 
	    "username": "admin"
	}
    }

Oppure con un browser, effettuare il browse di:

* http://localhost:8000/api/auth/token/
* http://localhost:8000/api/auth/verify/

## Accesso admin

Con il test server acceso, si accede alla admin app tramite http://localhost:8000/admin

Esiste l'utente admin, password Cellophane. 
