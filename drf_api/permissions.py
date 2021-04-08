from rest_framework import permissions
from django.conf import settings



class IsCreator(permissions.BasePermission):
    message = 'You must be the creator of this object.'
    
    def has_permission(self, request, view):
        if request.user.profile.roles == "Author":
            return True
        else:
            return False



class OnlyForAuthor(permissions.BasePermission):
    message = 'You must be either or creator of this content.'
    
    def has_permission(self, request, view):
        return True
        
    def has_object_permission(self, request, view, obj):
        if request.user.profile.roles == "Admin":
            return True 
        elif request.user.email == obj.created_by:
            return True
        else:
            return False

