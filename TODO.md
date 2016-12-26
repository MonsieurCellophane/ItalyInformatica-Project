# Auth

* For token authenticated requests, how do we override the request.user ?
check, for instance, https://docs.djangoproject.com/en/1.10/topics/auth/customizing/

# Registration

* Now we have a Registration that can be sensibly saved. In model's save, need to set a token. AND the token needs to be a verification token (so maybe extend methods in bauth to take a variable payload). 

* The registration field needs to yield a validation_url which incorporates the vaildation token, and the validation token must be memorized as such.

* design a sensible URL schema. Need to look at get_absolute_url in models.py, which uses reverse. Needs by_id, by_token views.

* When using routers:

	URL pattern: ^registrations/$ Name: 'registration-list'
	URL pattern: ^registrations/{pk}/$ Name: 'registration-detail'
	
	@detail_route(methods=['get'], permission_classes=[(IsAdminOrIsSelf)])
	def set_password(self, request, pk=None):
	

	# The router will match lookup values containing any characters except slashes and period characters.
	# So we can use this, with pk being actually a token. 
	URL pattern: ^registrations/{pk}/set_password/$ Name: 'registration-verify'
	
	
