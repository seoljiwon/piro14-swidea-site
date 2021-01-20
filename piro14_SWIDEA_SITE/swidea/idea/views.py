from django.shortcuts import redirect
from django.shortcuts import render
from .models import Ideas, DevTool
from .forms import IdeasForm, DevToolForm

################### idea section #####################


def idea_list(request):
    ideas = Ideas.objects.all()
    ctx = {'ideas': ideas}

    return render(request, template_name='ideas/idea_list.html', context=ctx)


def idea_detail(request, pk):
    idea = Ideas.objects.get(pk=pk)
    ctx = {'idea': idea}

    return render(request, 'ideas/idea_detail.html', context=ctx)


def idea_create(request):
    if request.method == 'POST':
        form = IdeasForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.save()
            idea.image = request.FILES['image']
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeasForm()
        ctx = {'form': form}
        return render(request, template_name='ideas/idea_create.html', context=ctx)


def idea_edit(request, pk):
    idea = Ideas.objects.get(pk=pk)
    if request.method == "POST":
        form = IdeasForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.save()
            idea.image = request.FILES['image']
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeasForm(instance=idea)
        ctx = {'form': form}
    return render(request, 'ideas/idea_edit.html', context=ctx)


def idea_delete(request, pk):
    idea = Ideas.objects.get(pk=pk)
    idea.delete()
    return redirect('/')

################### devtool section #####################


def devtool_list(request):
    devtools = DevTool.objects.all()
    ctx = {'devtools': devtools}

    return render(request, template_name='devtool/devtool_list.html', context=ctx)


def devtool_detail(request, pk):
    devtool = DevTool.objects.get(pk=pk)
    ideas = DevTool.objects.get(pk=pk).ideas.all()
    ctx = {'devtool': devtool, 'ideas': ideas}

    return render(request, 'devtool/devtool_detail.html', context=ctx)


def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            devtool = form.save(commit=False)
            devtool.save()
            return redirect('devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm()
        ctx = {'form': form}
        return render(request, template_name='devtool/devtool_create.html', context=ctx)


def devtool_edit(request, pk):
    devtool = DevTool.objects.get(pk=pk)
    if request.method == "POST":
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            devtool = form.save(commit=False)
            devtool.save()
            return redirect('devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm(instance=devtool)
        ctx = {'form': form}
    return render(request, 'devtool/devtool_edit.html', context=ctx)


def devtool_delete(request, pk):
    devtool = DevTool.objects.get(pk=pk)
    devtool.delete()
    return redirect('/')
