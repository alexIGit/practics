from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_user(**kwargs):
    print("\nпользователь создан")
    print(kwargs)
    print(kwargs.get('sender'))

    instance = kwargs['instance']
    print(instance)
    sender = kwargs['sender']
    print(sender)