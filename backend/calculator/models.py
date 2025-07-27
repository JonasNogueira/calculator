from django.db.models import Model, ForeignKey, CharField, DateTimeField, CASCADE
from django.contrib.auth.models import User


class Operation(Model):

    user = ForeignKey(User, on_delete=CASCADE)
    parameters = CharField(max_length=255)
    result = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.expression} = {self.result}"
