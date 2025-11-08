from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

# --- Role check helpers ---
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# --- Role-based views ---
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    context = {'role': 'Admin'}
    return render(request, 'relationship_app/admin_view.html', context)


@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    context = {'role': 'Librarian'}
    return render(request, 'relationship_app/librarian_view.html', context)


@login_required
@user_passes_test(is_member)
def member_view(request):
    context = {'role': 'Member'}
    return render(request, 'relationship_app/member_view.html', context)
