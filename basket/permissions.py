from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsBasketOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.basket == request.user.basket
