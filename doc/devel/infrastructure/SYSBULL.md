# Tooling

 * Installati gitlab + apache2 su gitlab.itialyinformatica.org (MC)
 * Installato mattermost (fen0x)

## Issues

##  Mail

 * Il routing della posta (almeno, verso Google) passa per un IPv6 e quindi i messaggi richiedono SPF (inserire record in NS) e DKIM (inserire in NS e implementare tramite MILTER openKDIM.) Forse si renderà necessario anche DMARC.
 
 
### Gitlab

Installazione dai pacchetti già presenti. Il paccheggiatore è un idiota:

 * /etc/gitlab e /var/lib/gitlab contengono subset diversi di  file di configurazione con gli stessi nomi (quelli usati sono in /etc/gitlab;
 * esistono /usr/share/1gitlab-shell e /usr/share/gitlab; i rispettivi bin/ contengono gli stessi file, che fanno riferimento ad uno username sbagliato (git invece di gitlab) così check fallisce in maniere misteriose 
  * i bin/* da usare sono quelli di usr/share/gitlab **MA** la config di gitlab-shell è in /usr/share/gitlab-shell

Il risultato è che alla fine la mail non andava.
Symlinkando i file adeguati e rifacendo la config da capo ora funziona.
 

 * Problemi nel listare i runners. https://git.fosscommunity.in/debian-ruby/TaskTracker/issues/107 Applicata la patch trovata su: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=819903
 * Bug d'installazione: https://bugs.launchpad.net/ubuntu/+source/gitlab/+bug/1574349 si risolve seguendo il workaround:
 
    1. cd /usr/share/gitlab/

	2. bundler

	you may need to install some package first: 
	sudo apt-get install cmake libmysqlclient-dev automake autoconf autogen
 
