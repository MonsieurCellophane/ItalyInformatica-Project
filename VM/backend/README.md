# Backend vagrant VM

## Setup
 * install vagrant
 * install virtualbox
 * From the VM/backend folder, run the command:
 
     $ vagrant plugin install vagrant-vbguest

## Running

From the VM/backend folder, run the command:

	  $ vagrant up

with a browser, connect to http://localhost:8080 (login is admin, password Cellophane, django-admin at /admin(

You can hit ^C^C in the main shell, and the backend will keep running. if you want to restart the backend, either reload the machine:

	  $ vagrant reload

Or issue the following:

      $ vagrant ssh
	  $ sudo su -
	  # pkill -f manage.py
	  # pkill -f manage.py
	  # workon project
	  # cd /opt/project
	  # python ./manage.py runserver 0.0.0.0:80

	  
