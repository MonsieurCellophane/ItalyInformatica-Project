# Project lives!. 

*Un post in forma di standard*

## Intro & verse

Come forse qualcuno ricorda, circa un mese e mezzo fa si parlava sul sub e altrove di un "progettone", proposto da /u/fen0x. Si tattava, in breve, del progetto collaborativo di app FOSS che cambiasse i paradigmi del mondo della programmazione, fosse game changing, visionaria, e un veicolo per la ricchezza dei fortunati sviluppatori. E che, magari, funzionasse anche.

##  Esposizione

### A1

Dopo un periodo di dibattito sul sub, si consolidò la consapevolezza tipica delle discussioni che sono partecipate e fruttuose: nessuno era d'accordo con nessun altro. Si fece allora coraggiosamente avanti /u/chobeat proponendo un blueprint di minima: si sarebbe fatta una app mobile, divisa in frontend e backend; sarebbe stata una app di dating con elementi di gamification con (forse) una scoreboard da compilare facendo interagire i telefoni dei fortunati *"datee"* attraverso gli NFC dei telefoni che - entrando in contatto - avrebbero confermato l'avvenuto incontro dei cuori non più solitari. Fu fatta una CFP (Call For Prototypes), io mi resi disponibile per il prototipo del backend.

### A2

Per il frontend, gli interessati si impegnarono tutti in un costruttivo dibattito, che presto si focalizzò sul punto di massimo rilievo, e cioè, *"che linguaggio usare nel frontend?"*. Dopo un periodo di fruttuoso scambio di vedute, il risultato atteso non mancò di realizzarsi: ognuno dei partecipanti si ritirò dal progetto e dal dibattito, malmostos e incazzato con tutti gli altri. /u/chobeat gettò, demoralizzato, la spugna. Io mi ritrovai con un quarto di prototipo di backend e leader per default di un progetto di cui ero anche l'unico membro. 

### Bridge

Non mi andava di mollare il lavoro fatto fino a quel punto, per quanto non fosse tanto. E poi, se un progetto di questo genere ha un senso, è quello di imparare cose con cui il tran tran quotidiano non ti farebbe nemmeno entrare in contatto (o magari ti ci fa entrare, tu le metti in un tabset del browser e dici *"Ok, appena ho tempo ci guardo"*). E in effetti, solo seguendo le discussioni già avvenute, avevo avuto modo di conoscere diverse tecnologie della cui esistenza ero totalmente o parzialmente all'oscuro (Swagger, kivy...) Per cui decisi di continuare lo sviluppo - in solitudine, visto che i miei sforzi di reclutamento non avevano avuto successo - su un github messo in campo appositamente (https://github.com/MonsieurCellophane/ItalyInformatica-Project)

### A3

A questo punto, con circa un mese di ritardo sulle tabelle di marcia, il backend dell'app è - come diciamo noi programmatori (wink) - *feature complete*. Il che non è dire molto: si tratta di un generico backend di autenticazione, registrazione e (parziale) autorizzazione. Il tutto corredato da REST API in stile swagger e coreapi. Il buono di tutto ciò e che si tratta di un oggetto sufficientemente agnostico da poter essere utilizzato virtualmente in qualunque cosa abbia bisogno di un backend che faccia user e profile management distribuito.

## Solo 

### Chorus 1

Della roadmap originale del progetto è rimasto un elemento (il backend) e un partecipante. Questo significa che, per tutti gli interessati, è possibile ridiscutere praticamente tutto -non escluso il fatto che il prodotto finale debba essere una app di dating, nonostante il fatto che io continui a pensare che, tutto sommato, si tratti di una buona idea. L'unica cosa che non vorrei fossero discussi, a questo punto, sono i linguaggi da usare e i toolset da favorire. Preferisco di gran lunga dare il mio appoggio preventivo a un processo di *"rough consensus & running code"*: chi vuole propone un contributo funzionante e si vede chi ha l'idea migliore. Per questo motivo, penso ad una fase iniziale completamente agnostica per quello che riguarda piattaforma/linguaggio/toolset (ovviamente, gli autori di ogni prototipo si assumono la responsabilità delle tecnologie relative).

### Chorus 2

Se si riesce a coagulare un rinnovato interesse sul progetto, si aprono immediati spazi per diverse attività che dovrebbero soddisfare tutti i palati, ad esempio:

  * prototipazione di vari client che si interfaccino con il backend esistente: ad esempio un sito web, un'app android, una IOS, una sarcazzo. 
  
  * sviluppo del backend esistente per recepire buone idee provenienti dall sviluppo dei client
  
  
  * prototipo della *storyboard* dell'app, che è un modo tecnico per dire che ancora non si sa bene che cazzo dovrà fare 'sta cosa e come lo farà
  
All fine si potrebbe decidere tutto il resto, non escluso chi coordina le varie aree del progetto. Le mie doti naturali di coordinatore, che tendono a trasformare in un gregge di gatti qualunque gruppo di persone di cui mi renda responsabile, suggeriscono che io non sia il punto di riferimento più adatto - ma per ora, così è. Come è naturale in un processo di questo tipo, tutto quello che si sviluppa in questa fase è sacrificabile - nel senso che si può decidere tranquillamente di buttarlo tenendo le idee positive che conteneva per reimpiegarle.

## Ripresa

## Bridge 

Se invece nemmeno questo *flatus voci* basterà a ravvivare l'interesse, non ho intenzione di fermarmi subito. Probabilmente, visto che il prototipo esistente utilizza Django 10, proverò un'implementazione alternativa con flask e SqlAlchemy, e probabilmente, qualche client: php, Phonegap/Cordova, kivy. Poi, siccome gamification e GUI non sono proprio il mio forte, è probabile che mi fermi e tenga quello che ho scritto per riusarlo in progetti di lavoro.

### A4

Spero però che l'idea di imparare tecnologie nuove e usalre per farci cose possa stuzzicare il *code bone* di un certo numero di persone, e che si possa cominciare a farne qualcosa di buono. Se così fosse, invito gli interessati a farsi sentire.

## Coda

Non lasciate quindi che paura, incertezze e dubbi fermino la vostra ambizione! Il cielo è il limite! Move fast, break ~~balls~~ things!

Fama, gloria e ricchezza vi aspettano. Per non parlare di notti passate al debugger.

## Corona

C7- Dm7 - Am69

