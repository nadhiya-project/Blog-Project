from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

class Post(models.Model):
    author=models.ForeignKey('auth.User')
    title=models.CharField(max_length=256)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)


    def __str__(self):
        return self.title
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post=models.ForeignKey("Blog.Post",related_name="comments")
    author=models.CharField(max_length=256)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()
    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("post_list")
