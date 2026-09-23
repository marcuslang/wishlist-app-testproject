import uuid

from django.conf import settings
from django.db import models


class Wishlist(models.Model):
    """One wishlist per user, shareable via a secret UUID link."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist'
    )
    title = models.CharField(max_length=200, default='My Wishlist')
    share_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='items')
    text = models.CharField(max_length=300)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.text
