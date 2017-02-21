from rest_framework import permissions as rfp


class IsOwnerOrReadOnly(rfp.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in rfp.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner 
        try:
            return request.user == obj.owner
        except AttributeError:
            pass
        return False

    
class IsAdminOrReadOnly(rfp.BasePermission):
    """
    Custom permission to only allow admins to edit an object.
    """


    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in rfp.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return request.user.is_staff

class IsAdminOrIsSelf(rfp.BasePermission):

     def has_object_permission(self, request, view, obj):
        if not request.user: return False
        if request.user.is_anonymous: return False
        if request.user.is_staff: return True
        try:
            return request.user == obj.owner
        except AttributeError:
            pass

        try:
            return request.user.username == obj.username
        except AttributeError:
            pass
        return False
         
