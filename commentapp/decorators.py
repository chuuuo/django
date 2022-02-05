from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articleapp.models import Article
from profileapp.models import Profile

def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Comment.objects.get(pk=kwargs['pk'])
        if not comment.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated