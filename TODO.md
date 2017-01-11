# Accounts

* fine tune permissions for profiles (chek that a user can only edit its own: IsAdminOrOwner)

# Auth

AUTH now works (through middleware) also for @login_required decorated requests/views YAY! 




# General

* Think about using routers roather than detailed views (especially for registration)

* When using routers:

	URL pattern: ^registrations/$       Name: 'registration-list'
	URL pattern: ^registrations/{pk}/$  Name: 'registration-detail'
	
	@detail_route(methods=['get'], permission_classes=[(IsAdminOrIsSelf)])
	def set_password(self, request, pk=None):
	

	# The router will match lookup values containing any characters except slashes and period characters.
	# So we can use this, with pk being actually a token. 
	URL pattern: ^registrations/{pk}/set_password/$ Name: 'registration-verify'
	
	
