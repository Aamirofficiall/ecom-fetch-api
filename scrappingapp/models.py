from django.db import models
import re 


class CompetitorLink(models.Model):
    link  = models.CharField(max_length=500)
    name  = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        
        s = self.link
        s = re.sub(r"(?<=\w)([A-Z])", r" \1",s)
        self.name = s.split('/')[-1]
        
        super().save(*args, **kwargs)
