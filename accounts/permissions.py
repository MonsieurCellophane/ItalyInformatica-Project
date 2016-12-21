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

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

    
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
