from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from celery import shared_task

from .models import Post


@shared_task
def notify_user_for_new_comment(post_id, text_comment):
    print('Hello, I am a created comment!!!')

    post = Post.objects.get(id=post_id)
    site = Site.objects.get_current()
    link_post = f'http://{site.domain}:8000/{post.id}'

    user = post.user
    first_name = user.first_name if user.first_name else user.username

    html_content = render_to_string(
        'email/email_notify_about_new_comment.html',
        {
            'name': first_name,
            'text_comment': text_comment,
            'title_post': post.title,
            'site_name': site.name,
            'link': link_post,
        }
    )

    message = EmailMultiAlternatives(
        subject=f'{site.name}! New commentary on your post',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    message.attach_alternative(html_content, 'text/html')
    message.send()


@shared_task
def notify_user_for_accept_comment(post_id, text_comment, user_id):
    print('Hello, I am a accepted comment!!!')

    post = Post.objects.get(id=post_id)

    site = Site.objects.get_current()
    link_post = f'http://{site.domain}:8000/{post.id}'

    user = User.objects.get(id=user_id)
    first_name = user.first_name if user.first_name else user.username

    html_content = render_to_string(
        'email/email_notify_about_accepted_comment.html',
        {
            'name': first_name,
            'text_comment': text_comment,
            'title_post': post.title,
            'site_name': site.name,
            'link': link_post,
        }
    )

    message = EmailMultiAlternatives(
        subject=f'{site.name}! Your commentary on the post was accepted',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    message.attach_alternative(html_content, 'text/html')
    message.send()
