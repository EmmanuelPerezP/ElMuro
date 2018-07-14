from django.db import models


def directory_path_images(instance, filename):
    """
    Funcion que crea el filepath en el server donde se guardara la imagen
    """
    return '{0}{1}'.format(instance.id, filename)

class Comment(models.Model):
    """
    Class representing a comment or experiencia
    """
    image = models.ImageField(default=None, blank=True, upload_to=directory_path_images)
    dateCreated = models.DateTimeField(auto_now_add=True)
    likes = models.BigIntegerField(default=0)
    commentText = models.CharField(max_length=10000)

    def __str__(self):
        """
        String representing the model
        """
        return self.commentText

    def hasImage(self):
        return bool(self.image)
