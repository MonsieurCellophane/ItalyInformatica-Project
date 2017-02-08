## Descrizione

### Prima richiesta - rilascio del token

Ottenere un token tramite un post alla URL /api/auth/token specificando username, password, e.g.:

`$ http -b POST http://127.0.0.1:8000/api/auth/token/ username="admin" password="Cellophane"`

### Prima richiesta - uso del token

Effettuare la richiesta inserendo lo header HTTP `X-Token: <token value>`, e.g.:  

`http -v GET http://127.0.0.1:8000/test/ 'X-Token:224bc...hTlIifQ=='`

### Richieste successive

Il token ottenuto per la prima richiesta può essere riusato per ulteriori richieste fino alla sua scadenza (TBD).

## Esempio

Utilizzando lo script auth-request.sh che si trova nel folder bin/, per il server di sviluppo **lanciato sulla porta 8008**:


    $ bin/auth-request.sh  -v -b http://127.0.0.1:8008   admin Cellophane /test/
    Acquired token: 2e34f395c1c9b88048967eb5298073625859521382efc6e8e1a4b3a8bd636dfa,eyJ1c2VybmFtZSI6ICJhZG1pbiIsICJ0aW1lc3RhbXAiOiAiMTQ4MTQ4MjcwMi43NyIsICJzZXNzaW9ua2V5IjogIjhXdUVOMUtQbGtrdjVURmoifQ==
    GET /test/ HTTP/1.1
    Accept: */*
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Host: 127.0.0.1:8008
    User-Agent: HTTPie/0.9.9
    X-Token: 2e34f395c1c9b88048967eb5298073625859521382efc6e8e1a4b3a8bd636dfa,eyJ1c2VybmFtZSI6ICJhZG1pbiIsICJ0aW1lc3RhbXAiOiAiMTQ4MTQ4MjcwMi43NyIsICJzZXNzaW9ua2V5IjogIjhXdUVOMUtQbGtrdjVURmoifQ==



    HTTP/1.0 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Date: Sun, 11 Dec 2016 18:58:23 GMT
    Server: WSGIServer/0.1 Python/2.7.12
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN

    {
    "auth": "None", 
    "user": "admin"
    }
