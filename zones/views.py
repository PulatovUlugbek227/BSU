from contextlib import nullcontext
from django.db.models.deletion import ProtectedError
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, reverse
from .models import All_Area, Area, Tree, TreeKind, Owner, Group
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout    
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage

def index_chek(request):
    area = Area.objects.filter(parent__isnull=False)
    return render(request, 'index_chek.html', {'area':area})

def all_area(request):
    all_area = All_Area.objects.all()
    return render(request, 'all_area.html', {'all_area':all_area})

def all_area_detail(request, slug):
    area = Area.objects.all()
    all_area = All_Area.objects.get(slug__iexact = slug)
    return render(request, 'all_area_detail.html', {'all_area':all_area, 'area':area})

def index(request):
    if request.user.is_authenticated:
        area = Area.objects.filter(parent__isnull=True).filter(madaniyat=False).all()
        tree = Tree.objects.all()
        tree_kind = TreeKind.objects.all()
        return render(request, 'index.html',{'area':area, 'tree':tree, 'tree_kind':tree_kind})
    return redirect('login_site')

def zone_detail(request):
    if request.user.is_authenticated:
        area = Area.objects.all()
        return render(request, 'areas.html', {'area':area})

def index_detail(request):
    if request.user.is_authenticated:
        tree_kind = TreeKind.objects.all()
        owners = Owner.objects.all()
        groups = Group.objects.all()
        area = Area.objects.filter(parent__isnull=False)
    context = {'area':area, 'tree_kind':tree_kind, 'owners': owners, 'groups': groups}
    return render(request, 'index_detail.html', context)

def index_madaniyot(request):
    if request.user.is_authenticated:
        tree_kind = TreeKind.objects.all()
        area = Area.objects.filter(madaniyat = True)
        owners = Owner.objects.all()
    context = {'area':area, 'tree_kind':tree_kind, 'owners':owners}
    return render(request, 'madaniyot.html', context)

def tree_create(request):
    if request.method == 'POST':
        tree = Tree()
        tree.latitude = request.POST.get('latitude')
        tree.longitude = request.POST.get('longitude')
        tree.tree_kind = TreeKind.objects.get(id=request.POST.get('tree_kind'))
        tree.owner = Owner.objects.get(id=request.POST.get('owner'))
        tree.area = Area.objects.get(id_polygon=request.POST.get('area'))
        tree.save()
    return redirect(reverse('index_detail'))

def tree_create_mad(request):
    if request.method == 'POST':
        tree = Tree()
        tree.latitude = request.POST.get('latitude')
        tree.longitude = request.POST.get('longitude')
        tree.tree_kind = TreeKind.objects.get(id=request.POST.get('tree_kind'))
        tree.owner = Owner.objects.get(id=request.POST.get('owner'))
        tree.area = Area.objects.get(id_polygon=request.POST.get('area'))
        tree.save()
    return redirect(reverse('index_madaniyot'))

def all_zones_create(request):
    if request.method == 'POST':
        all_area = All_Area()
        all_area.title = request.POST.get('title')
        all_area.slug = translit(request.POST.get('title'))
        if request.FILES.get('image', False) != False:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            all_area.image = filename
    return redirect(reverse('all_area'))
    
def translit(text):
    dic = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'yo',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'shch',
    'ъ': 'y',
    'ы': 'y',
    'ь': '',
    'э': 'e',
    'ю': 'yu',
    'я': 'ya',
    ' ': '-',
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'Yo',
    'Ж': 'Zh',
    'З': 'Z',
    'И': 'I',
    'Й': 'Y',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'H',
    'Ц': 'Ts',
    'Ч': 'Ch',
    'Ш': 'Sh',
    'Щ': 'Shch',
    'Ъ': 'Y',
    'Ы': 'Y',
    'Ь': '',
    'Э': 'E',
    'Ю': 'Yu',
    'Я': 'Ya',}
    result = ''
    for i in text:
        if i in dic:
            result += dic[i]
        else:
            result += i
    return result



def tree_detail(request, id):
    tree = Tree.objects.get(id=id)
    context = {'tree': tree}
    return render(request, 'tree_detail.html', context)

def group_create(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        group = Group()
        group.title = request.POST.get('title')
        group.save()
        return redirect(reverse('index'))
    context = {'groups': groups}
    return render(request, 'group_create.html')

def student_create(request):
    groups = Group.objects.all()
    students = Owner.objects.all()
    if request.method == 'POST':
        student = Owner()
        student.name = request.POST.get('name')
        student.group = Group.objects.get(id=request.POST.get('group'))
        student.save()
        return redirect(reverse('index'))
    context = {'groups': groups, 'students':students}
    return render(request, 'student_create.html', context)

def student_edit(request, id):
    student = Owner.objects.get(id=id)
    groups = Group.objects.all()
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.group = Group.objects.get(id=request.POST.get('group'))
        student.save()
        return redirect(reverse('groups'))
    context = {'groups': groups, 'student': student}
    return render(request, 'student_edit.html', context)

def tree_edit(request, id):
    tree = Tree.objects.get(id=id)
    tree_kind = TreeKind.objects.all()
    area = Area.objects.all()
    students = Owner.objects.all()
    if request.method == 'POST':
        tree.latitude = request.POST.get('latitude')
        tree.longitude = request.POST.get('longitude')
        tree.tree_kind = TreeKind.objects.get(id=request.POST.get('tree_kind'))
        tree.owner = Owner.objects.get(id=request.POST.get('owner'))
        tree.area = Area.objects.get(id_polygon=request.POST.get('area'))
        tree.save()
        return redirect(reverse('index'))
    context = {'tree': tree, 'tree_kind':tree_kind, 'area':area, 'students': students}
    return render(request, 'tree_edit.html', context)

def student_delete(request, id):
    student = Owner.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect(reverse('index'))
    return render(request, 'student_delete.html', {'student': student})



def tree_delete(request, id):
    tree = Tree.objects.get(id=id)
    if request.method == 'POST':
            tree.delete()
            return redirect(reverse('index'))
    return render(request, 'tree_delete.html', {'tree':tree})

def search_group(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        query = request.POST.get('search')
        groups = Group.objects.filter(Q(title__contains=query))
        return render(request, 'search.html', {'groups': groups})
    return render(request, 'search.html',{'groups': groups})

def search_student(request):
    students = Owner.objects.all()
    if request.method == 'POST':
        query = request.POST.get('search_stud')
        students = Owner.objects.filter(Q(name__contains=query))
        return render(request, 'search_student.html', {'students': students})
    return render(request, 'search_student.html',{'students': students})

def groups(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'groups.html', context)

def students(request):
    students = Owner.objects.all()
    context = {'students': students}
    return render(request, 'students.html', context)

def student(request, id):
    student = Owner.objects.get(id=id)
    trees_lst = [tree for tree in student.tree_set.all()]
    paginator = Paginator(trees_lst, 100)
    page_number = request.GET.get('page')
    trees = paginator.get_page(page_number)
    context = {'student': student, 'trees':trees}
    return render(request, 'student.html', context)

def login_site(request):
    if request.user.is_authenticated:
        return redirect('index')
    message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            message = 'Извините, такого пользователя не существует'
            return render(request, 'login.html', {'message': message})
    return render(request, 'login.html', {'message': message})

def logout_site(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')

    