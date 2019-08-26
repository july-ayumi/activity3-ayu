from django.shortcuts import render, redirect
from django.views import generic
from .forms import SearchForm, PostForm, LoginForm
from .models import Employee, Login

class IndexView(generic.ListView):
    model = Employee
    paginate_by = 5

    def get_context_data(self):
        """テンプレートへ渡す辞書の作成"""
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET)   # 空欄でも良いが、次のページでも選択内容を
        return context

    def get_queryset(self):#全てのデータを取得
        """テンプレートへ渡す「employee_list」を作成する"""
        form = SearchForm(self.request.GET)
        form.is_valid()  # required=Falseなのでifではないが、これをしないと、cleaned_dataができない!!!
        # まず、全てのタスクを取得
        queryset = super().get_queryset()
        queryset = Employee.objects.order_by("due")
        queryset = queryset.filter(complete=False)

        #completeのGET
        try:
            complete_checked = self.request.GET['complete']
            if complete_checked != "":
                change = Employee.objects.get(pk=complete_checked)
                print(555555555555,change)
                change.complete = True
                print(555555555555,change)
                change.save()

        except:
            pass

        # 部署の選択があれば、部署で絞り込み(filter)
        department = form.cleaned_data['department']
        if department != None:#部署が選択されていれば
            queryset = queryset.filter(department=self.request.GET['department'])

        #まだ検索されてない状態ではGETがないからtry exceptにする必要がある
        try:
            name = self.request.GET['name']
            if name != "":
                queryset = queryset.filter(name=self.request.GET['name'])
        except:
            print("except")
            queryset = queryset
            print(queryset)

        return queryset

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('employee:index')
    else:
        form = PostForm()
    return render(request, 'employee/post_edit.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                enter_id = request.POST['login_id']
                print(333334444444444,enter_id)
                login = Login.objects.get(login_id = enter_id)
                print(44444444444444444,login)
                return redirect('employee:index')
            except:
                form = LoginForm()
                return render(request, 'employee/login.html', {'form':form})
    else:
        form = LoginForm()

    return render(request, 'employee/login.html', {'form':form})

def detail(request):
    detail = Employee.objects.all()
    print(99999999999999,detail)
    context = {
        'detail':detail,
    }
    return render(request, 'employee/detail.html', context)
