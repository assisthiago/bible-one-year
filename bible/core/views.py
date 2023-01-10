from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, resolve_url as r

from bible.core.forms import SignInForm, SignUpForm
from bible.core.models import Book, Lection, Task


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)

        if not form.is_valid():
            return render(request, 'sign_in.html', {'form': form})

        user = authenticate(
            request,
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password'])

        if not user:
            messages.error(request, 'E-mail ou senha incorreta.')
            return render(request, 'sign_in.html', {'form': form})

        login(request, user)
        return HttpResponseRedirect(r('home'))

    return render(request, 'sign_in.html', {'form': SignInForm()})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if not form.is_valid():
            return render(request, 'sign_up.html', {'form': form})

        try:
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'])

            lection = Lection.objects.get(order=1)
            Task.objects.create(user=user, lection=lection)

        except:
            messages.error(request, 'Usuário já existe.')
            return render(request, 'sign_up.html', {'form': form})

        messages.success(request, 'Conta criada com sucesso.')
        return HttpResponseRedirect(r('sign-in'))

    return render(request, 'sign_up.html', {'form': SignUpForm()})


def sign_out(request):
    logout(request)
    return HttpResponseRedirect(r('sign-in'))


def reset_password(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if not form.is_valid():
            return render(request, 'reset-password.html', {'form': form})

        try:
            user = get_object_or_404(User, email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()

            messages.success(request, 'Senha atualizada com sucesso.')
            return HttpResponseRedirect(r('sign-in'))

        except:
            messages.error(request, 'Usuário não encontrado.')
            return render(request, 'reset-password.html', {'form': form})

    return render(request, 'reset-password.html', {'form': SignUpForm()})


@login_required
def home(request):
    context = {'tasks': []}

    tasks = Task.objects.all().order_by('-lection__order')
    for task in tasks:
        books = task.lection.versicle_set.values_list(
            'book__name', flat=True).order_by('book__order').distinct()

        display_chapters = ''
        for book in books:
            chapters = set(
                task.lection.versicle_set.filter(book__name=book).values_list(
                    'chapter', flat=True).order_by('chapter'))

            chapters = ', '.join(str(ch) for ch in sorted(chapters))
            if display_chapters:
                display_chapters += ' - ' + chapters
            else:
                display_chapters += chapters

        context['tasks'].append({
            'obj': task,
            'books': books,
            'chapters': display_chapters,
        })

    context['progress'] = str(0.30 * len(tasks)).replace(',', '.')
    return render(request, 'index.html', context)


@login_required
def detail(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        task.completed = True
        task.completed_at = datetime.now()
        task.save()

        # Create next task
        try:
            next_lection_order = task.lection.order + 1
            lection = get_object_or_404(Lection, order=next_lection_order)

            Task.objects.create(user=request.user, lection=lection)
            messages.success(request, 'Próxima tarefa disponível.')

        except Http404:
            pass

        return HttpResponseRedirect(r('home'))


    books = task.lection.versicle_set.values_list(
        'book__name', flat=True).order_by('book__order').distinct()

    lections = []
    for book in books:
        chapters = task.lection.versicle_set.filter(
            book__name=book).order_by('chapter', 'number')

        lections.append({book: chapters})

    context = {'task': task, 'lections': lections}
    return render(request, 'detail.html', context)


@login_required
def book(request, abbreviation):
    try:
        book = get_object_or_404(Book, abbreviation=abbreviation)
        return render(request, 'book.html', {'book': book})

    except Http404:
        messages.error(request, f'Livro não encontrado.')
        return HttpResponseRedirect(r('sign-in'))
