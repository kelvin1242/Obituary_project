from django.shortcuts import redirect, render

from .forms import ObituaryForm


def submit_obituary(request):
    if request.method == "POST":
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view_obituaries")
    else:
        form = ObituaryForm()
    return render(request, "obituary_form.html", {"form": form})
