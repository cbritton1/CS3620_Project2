from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StoryOneForm, StoryTwoForm, StoryWarForm, StoryDragonsForm, StoryWalmartForm,\
    StoryLoveLetterForm, StorySmellyCatForm, StoryGreetingsEarthlingsForm, HailToTheChiefForm, HolidayFestivitiesForm,\
    PizzaParlorForm, PizzaParlor, CatAndTheFiddle, CatAndTheFiddleForm, Baseball, BaseballForm, JJRTolkien,\
    JJRTolkienForm, JackAndJill, JackAndJillForm
from .models import StoryOne, StoryTwo, StoryWar, StoryDragons, StoryWalmart, StoryLoveLetter,\
    StorySmellyCat, StoryGreetingsEarthlings, HailToTheChief, HolidayFestivities


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


def story_greeting_earthlings(request, item_id):
    item = StoryGreetingsEarthlings.objects.get(pk=item_id)
    return render(request, 'story_time/story_greeting_earthlings.html', {'item': item})


def story_hail_to_the_chief(request, item_id):
    item = HailToTheChief.objects.get(pk=item_id)
    return render(request, 'story_time/story_hail_to_the_chief.html', {'item': item})


def story_holiday_festivities(request, item_id):
    item = HailToTheChief.objects.get(pk=item_id)
    return render(request, 'story_time/story_holiday_festivities.html', {'item': item})


def story_pizza_parlor(request, item_id):
    item = PizzaParlor.objects.get(pk=item_id)
    return render(request, 'story_time/story_pizza_parlor.html', {'item': item})


def story_cat_and_the_fiddle(request, item_id):
    item = CatAndTheFiddle.objects.get(pk=item_id)
    return render(request, 'story_time/story_cat_and_the_fiddle.html', {'item': item})


def story_baseball(request, item_id):
    item = Baseball.objects.get(pk=item_id)
    return render(request, 'story_time/story_baseball.html', {'item': item})


def story_JJRTolkien(request, item_id):
    item = Baseball.objects.get(pk=item_id)
    return render(request, 'story_time/story_JJRTolkien.html', {'item': item})


def story_jack_and_jill(request, item_id):
    item = JackAndJill.objects.get(pk=item_id)
    return render(request, 'story_time/story_jack_and_jill.html', {'item': item})


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


def story_greeting_earthlings_form(request):
    form = StoryGreetingsEarthlingsForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = StoryGreetingsEarthlings.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = StoryGreetingsEarthlings.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_greeting_earthlings.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def story_hail_to_the_chief_form(request):
    form = HailToTheChiefForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = HailToTheChief.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = HailToTheChief.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_hail_to_the_chief.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def story_holiday_festivities_form(request):
    form = HolidayFestivitiesForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = HolidayFestivities.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = HolidayFestivities.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_holiday_festivities.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def story_pizza_parlor_form(request):
    form = PizzaParlorForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = PizzaParlor.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = PizzaParlor.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_pizza_parlor.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def story_cat_and_the_fiddle_form(request):
    form = CatAndTheFiddleForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = CatAndTheFiddle.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = CatAndTheFiddle.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_cat_and_the_fiddle.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def story_baseball_form(request):
    form = BaseballForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = Baseball.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = Baseball.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_baseball.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def story_JJRTolkien_form(request):
    form = JJRTolkienForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = JJRTolkien.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = JJRTolkien.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_JJRTolkien.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def story_jack_and_jill_form(request):
    form = JackAndJillForm(request.POST or None)

    if form.is_valid():
        form.save()
        story_list = JackAndJill.objects.all()
        x = len(story_list)
        story = story_list[x-1]
        last_story = story.id
        item = JackAndJill.objects.get(pk=last_story)
        context = {'item': item}
        return render(request, 'story_time/story_jack_and_jill.html', context)
    return render(request, 'story_time/story_form.html', {'form': form})


def all_stories(request):
    story_list1 = StoryOne.objects.all()
    story_list2 = StoryTwo.objects.all()
    story_list3 = StoryWar.objects.all()
    story_list4 = StoryDragons.objects.all()
    story_list5 = StoryWalmart.objects.all()
    story_list6 = StoryLoveLetter.objects.all()
    story_list7 = StorySmellyCat.objects.all()
    story_list8 = StoryGreetingsEarthlings.objects.all()
    story_list9 = HailToTheChief.objects.all()
    story_list10 = HolidayFestivities.objects.all()
    story_list11 = PizzaParlor.objects.all()
    story_list12 = CatAndTheFiddle.objects.all()
    story_list13 = Baseball.objects.all()
    story_list14 = JJRTolkien.objects.all()
    story_list15 = JackAndJill.objects.all()
    context = {
        'story_list1': story_list1,
        'story_list2': story_list2,
        'story_list3': story_list3,
        'story_list4': story_list4,
        'story_list5': story_list5,
        'story_list6': story_list6,
        'story_list7': story_list7,
        'story_list8': story_list8,
        'story_list9': story_list9,
        'story_list10': story_list10,
        'story_list11': story_list11,
        'story_list12': story_list12,
        'story_list13': story_list13,
        'story_list14': story_list14,
        'story_list15': story_list15,
    }
    return render(request, 'story_time/all_stories.html', context)

