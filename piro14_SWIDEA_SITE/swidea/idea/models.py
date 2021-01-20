from django.db import models


class DevTool(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    desc = models.TextField()

    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Ideas(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to="idea_image/%Y/%m/%d/")
    content = models.TextField()
    interest = models.IntegerField()
    devtool = models.ForeignKey(
        DevTool, related_name="ideas", on_delete=models.CASCADE)

    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
