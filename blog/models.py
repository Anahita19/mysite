from django.db import models

# Create your models here.
class Post(models.Model):
    #title
    title = models.CharField(max_length=250)
    #content
    content=models.TextField()
    #image
    #category
    #author
    #tag
    #content_view
    content_view= models.IntegerField(default=0)
    #status
    status= models.BooleanField(default=True)
     #published_date
    published_date= models.DateTimeField(null=True)
    #created_date
    created_date= models.DateTimeField(auto_now_add=True)
    #updated_date  2026-05-26 23:39:36.664533    2026-05-26 23:42:18.238704p2
    updated_date= models.DateTimeField(auto_now=True)

    class Meta:
       ordering= ['-created_date']
       verbose_name_plural = "پست ها"

    def __str__(self):
      return "{}".format(self.title)
     