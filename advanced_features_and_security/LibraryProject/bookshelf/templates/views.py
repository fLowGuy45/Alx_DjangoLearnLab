from django.shortcuts import render, redirect
from .forms import ExampleForm

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Handle form processing here
            return redirect('success_page')  # Replace with an actual URL or view
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
