'''
Views
'''
import datetime as dt
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Article,NewsLetterRecipients
from .forms import NewsLetterForm
from .email import send_welcome_email

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('news_of_day')
    else:
        form = NewsLetterForm()
    return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})
    

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

# View Function to present news from past days
def past_days_news(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html',{"date": date,"news":news})

def search_results(request):
    # print(dict(request.GET))
    print(type(request.GET))
    

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})