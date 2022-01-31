from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)

    def form_valid(self, form):
        # 임시 user 데이터!
        # (다른 사람의 프로필을 만들 수 있는 가능성을 제거하기 위해 forms에 user 정보를 받지 않아 생기는 오류를 해결하기 위해
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)