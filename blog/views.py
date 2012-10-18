from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Article
from datetime import datetime

def list(request):
    # all blog posts
    now = datetime.now()
    articles = Article.objects.filter(status='live', date_published__lte=now).order_by('-date_published')
    variables = RequestContext(request, {'articles' : articles, 'now': now})
    return render_to_response('home.html', variables)

