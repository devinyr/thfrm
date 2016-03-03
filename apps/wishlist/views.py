from django.contrib.auth import login, authenticate, forms, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from apps.wishlist.models import Item, WishList

# class Dashboard(View):
#     template = 'wishlist/dashboard.html'
#     user = ''
#     context = {'templateData' : user,}
#     def get(self, request):
#         dictionary = {
#             "wishlist": WishList.objects.filter(username=request.user)
#         }
       
#         return render(request, self.template, self.context, dictionary)
# itid = Item.objects.get(itemname="item")
# Wishlist.objects.create(username="test1", item_id=itid  )


class Dashboard(View):
    def get(self, request):
        print '*'*100
        print request.user.id
        print Item.objects.all()
        print WishList.objects.all()
        print WishList.objects.filter(id=request.user.id)
        dictionary = {
            "item": Item.objects.all(),
            "wishlist": WishList.objects.filter(uname=request.user),
            "otherlist": WishList.objects.exclude(uname=request.user)
        }
       
        return render(request, "wishlist/dashboard.html", dictionary)



