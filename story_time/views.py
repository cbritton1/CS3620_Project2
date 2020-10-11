from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StoryOneForm
from .models import StoryOne


# Create your views here.
def home(request):
    context = {}
    return render(request, 'story_time/home.html', context)


def story_one(request,):
    item = StoryOne.objects.get(pk=2)
    context = {'item': item}
    # return HttpResponse(context)
    return render(request, 'story_time/story_one.html', context)


def story_one_form(request):
    form = StoryOneForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('story_time:story_one')
    return render(request, 'story_time/story_one_form.html', {'form': form})


# def story_delete(request, id):
#     item = StoryOne.objects.get(id=id)
#
#     if request.method == 'POST':
#         item.delete()
#         return redirect('story_time:home')
#     return render(request, 'story_time/story_one_delete.html', {'item': item})
