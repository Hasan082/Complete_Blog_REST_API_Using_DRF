from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: 
    - SAFE methods (GET, HEAD, OPTIONS) are allowed to all users.
    - EDIT methods (PUT, PATCH, DELETE) are only allowed to the owner.
    """

    def has_object_permission(self, request, view, obj):
        # Allow all safe methods
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check ownership based on 'user' or 'author.user'
        owner = getattr(obj, 'user', None)
        if owner is not None:
            return owner == request.user

        author = getattr(obj, 'author', None)
        if author is not None and hasattr(author, 'user'):
            return author.user == request.user

        # Deny by default
        return False
