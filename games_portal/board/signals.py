from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Comment
from .tasks import notify_user_for_new_comment, notify_user_for_accept_comment


@receiver(post_save, sender=Comment)
def new_comment_or_approved(sender, instance, created, **kwargs):

    if created:
        notify_user_for_new_comment.delay(instance.post.id, instance.text)

    if instance.is_accept:
        notify_user_for_accept_comment.delay(instance.post.id, instance.text, instance.user.id)
