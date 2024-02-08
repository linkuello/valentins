from django.db import models

class ValentineCard(models.Model):
    sender_name = models.CharField(max_length=100)
    recipient_email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
