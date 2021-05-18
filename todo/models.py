from django.db import models
from authentication.models import User
from helpers.models import TrackingModel

# Create your models here.
class Todo(TrackingModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    

    # class Meta:
    #     verbose_name = _("Todo")
    #     verbose_name_plural = _("Todos")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Todo_detail", kwargs={"pk": self.pk})
