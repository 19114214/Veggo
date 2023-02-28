from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile
#take the signal     
@receiver(post_save, sender=User)    
#receiver function ni siya
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    #print(sender)
    #print(**kwargs)
    if created:
        UserProfile.objects.create(user=instance)
        # print('user profile is created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the userprofile if not exist
            UserProfile.objects.create(user=instance)
            # print('Profile was not existed, but I created one')
        # print('user is updated')
    
@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass
    #print(instance.username, 'this is user is being saved')