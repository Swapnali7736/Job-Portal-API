from rest_framework.permissions import BasePermission

class JobPermission(BasePermission):
    def has_permission(self,request,view):
        if request.method=="GET":
            return True
        else:
            return request.user.is_authenticated

    def has_object_permission(self,request,view,obj):
        if request.method=="GET":
            return True
        else:
            return obj.postedby == request.user