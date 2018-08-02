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

    def get_score(self):
        return self.likes - self.dislike


class Comment(models.Model):
    """
    Clase que asociada a un Post
    """
    dateCreated = models.DateTimeField(auto_now_add=True)
    likes = models.BigIntegerField(default=0)
    dislike = models.BigIntegerField(default=0)
    score = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentText = models.CharField(max_length=10000)

    def __str__(self):
        """
        String representing the model
        """
        return self.commentText

    def get_score(self):
        return self.likes - self.dislike


class HeaderImage(models.Model):
    """
    Modelo de cada header image
    """
    image = models.ImageField(default=None, upload_to=directory_path_images)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representing the model
        """
        return str(self.id)
