from django.db import models
from django.urls import reverse


def directory_path_images(instance, filename):
    """
    Funcion que crea el filepath en el server donde se guardara la imagen
    """
    return '{0}{1}'.format(instance.id, filename)


class Post(models.Model):
    """
    Modelo de cada Post
    """
    image = models.ImageField(default=None, blank=True, upload_to=directory_path_images)
    dateCreated = models.DateTimeField(auto_now_add=True)
    likes = models.BigIntegerField(default=0)
    dislike = models.BigIntegerField(default=0)
    score = models.IntegerField(default=0)
    postText = models.CharField(max_length=10000)

    def __str__(self):
        """
        String representing the model
        """
        return self.postText

    def hasImage(self):
        return bool(self.image)

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk])


class Comment(models.Model):
    """
    Clase que asociada a un Post
    """
    likes = models.BigIntegerField(default=0)
    dateCreated = models.DateTimeField(auto_now_add=True)
    commentText = models.CharField(max_length=10000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representing the model
        """
        return self.commentText

