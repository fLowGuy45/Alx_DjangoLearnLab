rom django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required




def is_librarian(user):
return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'




@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
context = {'role': 'Librarian'}
return render(request, 'relationship_app/librarian_view.html', context)
