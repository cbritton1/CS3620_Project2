from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StoryOneForm, StoryTwoForm, StoryWarForm, StoryDragonsForm, StoryWalmartForm,\
    StoryLoveLetterForm, StorySmellyCatForm
from .models import StoryOne, StoryTwo, StoryWar, StoryDragons, StoryWalmart, StoryLoveLetter,\
    StorySmellyCat


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


def story_walmart(request, item_id):
    item = StoryWalmart.objects.get(pk=item_id)
    return render(request, 'story_time/story_walmart.html', {'item': item})


def story_love_letter(request, item_id):
    item = StoryLoveLetter.objects.get(pk=item_id)
    return render(request, 'story_time/story_love_letter.html', {'item': item})


def story_smelly_cat(request, item_id):
    item = StorySmellyCat.objects.get(pk=item_id)
    return render(request, 'story_time/story_smelly_cat.html', {'item': item})


def story_one_form(request,):
    form = StoryOneForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = StoryOne.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = StoryOne.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_one.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def story_two_form(request,):
    form = StoryTwoForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = StoryTwo.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = StoryTwo.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_two.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def story_war_form(request,):
    form = StoryWarForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = StoryWar.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = StoryWar.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_war.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def story_dragons_form(request):
    form = StoryDragonsForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = StoryDragons.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = StoryDragons.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_dragons.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def story_walmart_form(request):
    form = StoryWalmartForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = StoryWalmart.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = StoryWalmart.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_walmart.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def story_love_letter_form(request):
    form = StoryLoveLetterForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = StoryLoveLetter.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = StoryLoveLetter.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_love_letter.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def story_smelly_cat_form(request):
    form = StorySmellyCatForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = StorySmellyCat.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = StorySmellyCat.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_smelly_cat.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def all_stories(request):
    story_list1 = StoryOne.objects.all()
    story_list2 = StoryTwo.objects.all()
    story_list3 = StoryWar.objects.all()
    story_list4 = StoryDragons.objects.all()
    story_list5 = StoryWalmart.objects.all()
    story_list6 = StoryLoveLetter.objects.all()
    story_list7 = StoryLoveLetter.objects.all()
    context = {
        'story_list1': story_list1,
        'story_list2': story_list2,
        'story_list3': story_list3,
        'story_list4': story_list4,
        'story_list5': story_list5,
        'story_list6': story_list6,
        'story_list7': story_list7,
    }
    return render(request, 'story_time/all_stories.html', context)

