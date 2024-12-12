from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone



class Drink(models.Model):
    TEA_STATUS_READY = 'r'
    TEA_STATUS_NOTREADY = 'nr'
    TEA_STATUS_OLD = 'o'

    TEA_STATUS= [
        (TEA_STATUS_READY,'Ready'),
        (TEA_STATUS_NOTREADY,'NotReady'),
        (TEA_STATUS_OLD,'Old'),
    ]
    
    title =   models.CharField(max_length=200)  
    status = models.CharField(max_length=2, choices=TEA_STATUS,default=TEA_STATUS_NOTREADY)
    teamaker = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='teamaker', )

    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True) 
    
    
    
    
    def __str__(self):
        return self.title