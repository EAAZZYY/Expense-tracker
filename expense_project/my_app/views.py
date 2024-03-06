from django.shortcuts import render,redirect
from .models import MyExpense
from .forms import ExpenseForm
from django.db.models import Sum
import datetime

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ExpenseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    else:
        expense = MyExpense.objects.all()
        total_expense = expense.aggregate(Sum("amount"))
        
        form = ExpenseForm()
        
        today = datetime.date.today()
        year = datetime.timedelta(days=365)
        month = datetime.timedelta(days=30)
        week = datetime.timedelta(days=7)
        
        # Yearly spending Logic
        year_diff = today - year 
        yearly_spending = MyExpense.objects.filter(date__gt = year_diff)
        yearly_sum = yearly_spending.aggregate(Sum("amount"))
        
        # Monthly spending Logic
        month_diff = today - month
        monthly_spending = MyExpense.objects.filter(date__gt = month_diff)
        monthly_sum = monthly_spending.aggregate(Sum("amount"))
        
        # Weekly spending Logic
        week_diff = today - week
        weekly_spending = MyExpense.objects.filter(date__gt = week_diff)
        weekly_sum = weekly_spending.aggregate(Sum("amount"))
        
        # daily_spend Logic
        daily = MyExpense.objects.filter().values("date").order_by("date").annotate(sum=Sum("amount"))
        
        # categorical spend Logic
        category = MyExpense.objects.filter().values("category").order_by("category").annotate(sum=Sum("amount"))
        
        context = {
            "expense":expense,
            "form":form, 
            "total_expense":total_expense,
            "yearly_sum":yearly_sum,
            "monthly_sum":monthly_sum,
            "weekly_sum":weekly_sum,
            "daily":daily,
            "category":category
            }
    return render(request, "my_app/home.html", context)

def edit(request,id):
    if request.method == "POST":
        model = MyExpense.objects.get(id=id)
        edit_form = ExpenseForm(data=request.POST,instance=model)
        if edit_form.is_valid():
            edit_form.save()
            return redirect("home")
    else:
        model = MyExpense.objects.get(id=id)
        edit_form = ExpenseForm(instance=model)
        
    return render(request, "my_app/edit.html",{"edit_form":edit_form})

def delete(request,id):
    
    if request.method == "POST":
        model = MyExpense.objects.get(id=id)
        model.delete()
        return redirect("home")
    else:
    
        return render(request, "my_app/delete.html")    