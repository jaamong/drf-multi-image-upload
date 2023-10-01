from django.db import models
from utils import rename_image_to_uuid


class Post(models.Model):
    text = models.CharField(max_length=500)


class PostImage(models.Model):
    """
    1 : N 관계
    Post : PostImage 관계
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Post 삭제 시 이미지도 같이 삭제됨
    image = models.ImageField(upload_to=rename_image_to_uuid, blank=True, null=True)  # upload_to = 이미지 업로드 위치

    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f'{self.post.text}'
