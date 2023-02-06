from django.http import	JsonResponse
from ..models import Baqueros, FloraFauna, Post

def routes(request):
    routes= [
        'GET /api/posts',
        'GET /api/post/:id',
        'GET /api/baqueros',
        'GET /api/florafauna',
    ]
    return JsonResponse(routes, safe=False)

def posts(request):
    posts = Post.objects.all()
    posts_dict=[]
    for p in posts:
        posts_dict.append({
            'id': p.id,
            'title': p.title,
            'text': p.text,
        })
      
    return JsonResponse(posts_dict, safe=False)

def post(request, id):
    post = Post.objects.get(id=id)
    posts_dict={
        'id': post.id,
        'title': post.title,
        'text': post.text,
        
    }
    return JsonResponse(posts_dict, safe=False)

def baqueros(request):
    posts = Baqueros.objects.all()
    posts_dict=[]
    for p in posts:
        posts_dict.append({
            'id': p.id,
            'name': p.name,
            'description': p.description,
        })
      
    return JsonResponse(posts_dict, safe=False)

def florasfaunas(request):
    posts = FloraFauna.objects.all()
    posts_dict=[]
    for p in posts:
        posts_dict.append({
            'id': p.id,
            'name': p.name,
            'type': p.tipo,
            'description': p.description,
        })
      
    return JsonResponse(posts_dict, safe=False)
