from django.shortcuts import render, HttpResponse
from .models import Category, product
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.

from django.contrib.auth.decorators import user_passes_test

def no_permissions(request):
    return render(request,'products/no_permission.html',{})


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)


@login_required(login_url='login/')
@permission_required('products.read_product', login_url='/no_permissions/')
#@group_required('seller', 'admin')
def products_list(request):
    #user = request.user
    # if user.has_perm('product.read_product'):
    queryset = product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/products_list.html", context)
    # else:
    #     return HttpResponse("You don't have permissions to view the product list")
