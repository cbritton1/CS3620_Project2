from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StoryOneForm, StoryTwoForm, StoryWarForm, StoryDragonsForm
from .models import StoryOne, StoryTwo, StoryWar, StoryDragons


# Create your views here.
def home(request):
    context = {}
    return render(request, 'story_time/home.html', context)


def story_one(request, item_id):
    item = StoryOne.objects.get(pk=item_id)
    context = {'item': item}
    return render(request, 'story_time/story_one.html', context)


def story_two(request, item_id):
    item = StoryTwo.objects.get(pk=item_id)
    context = {'item': item}
    return render(request, 'story_time/story_two.html', context)


def story_war(request, item_id):
    item = StoryWar.objects.get(pk=item_id)
    context = {'item': item}
    return render(request, 'story_time/story_war.html', context)


def story_dragons(request, item_id):
    item = StoryDragons.objects.get(pk=item_id)
    return render(request, 'story_time/story_dragons.html', {'item': item})


def story_one_form(request,):
    form = StoryOneForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('story_time:all_stories')
    return render(request, 'story_time/story_one_form.html', {'form': form})


def story_two_form(request,):
    form = StoryTwoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('story_time:all_stories')
    return render(request, 'story_time/story_one_form.html', {'form': form})


def story_war_form(request,):
    form = StoryWarForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('story_time:all_stories')
    return render(request, 'story_time/story_one_form.html', {'form': form})


def story_dragons_form(request):
    form = StoryDragonsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('story_time:all_stories')
    return render(request, 'story_time/story_one_form.html', {'form': form})


def all_stories(request):
    story_list1 = StoryOne.objects.all()
    story_list2 = StoryTwo.objects.all()
    story_list3 = StoryWar.objects.all()
    story_list4 = StoryDragons.objects.all()
    context = {
        'story_list1': story_list1,
        'story_list2': story_list2,
        'story_list3': story_list3,
        'story_list4': story_list4,
    }
    return render(request, 'story_time/all_stories.html', context)

