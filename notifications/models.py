from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Notifications(models.Model):
    # choices = [(email.email, email.email) for email in User.objects.all()]
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=30
                             # , choices=choices
                             )
    message = models.CharField(max_length=500)
    request_amount = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    created_at = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.from_user}, {self.email}, {self.message}, {self.request_amount}" \
               f", {self.created_at}, {self.is_seen}"


