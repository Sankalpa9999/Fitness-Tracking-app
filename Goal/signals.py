# # signals.py

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Progress, Notification

# @receiver(post_save, sender=Progress)
# def check_goal_completion(sender, instance, created, **kwargs):
#     if created:
#         goal = instance.goal
#         if goal.target_value <= instance.current_value:
#             # Check if the goal is already marked as achieved to avoid duplicate notifications
#             if not goal.achieved:
#                 goal.achieved = True
#                 goal.save()
#                 Notification.objects.create(user=goal.user, message=f'Congratulations! You have achieved your {goal.goal_type} goal.')