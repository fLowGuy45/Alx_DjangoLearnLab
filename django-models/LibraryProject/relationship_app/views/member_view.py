from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required




def is_member(user):
return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'




@login_required
@user_passes_test(is_member)
def member_view(request):
context = {'role': 'Member'}
return render(request, 'relationship_app/member_view.html', context)
