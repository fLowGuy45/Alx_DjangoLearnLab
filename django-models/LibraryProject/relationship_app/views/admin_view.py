from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required




def is_admin(user):
return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'




@login_required
@user_passes_test(is_admin)
def admin_view(request):
# context can be extended
context = {'role': 'Admin'}
return render(request, 'relationship_app/admin_view.html', context)
