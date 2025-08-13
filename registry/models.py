from django.db import models
from django.utils import timezone

# Create your models here.
class BaseModelQuerySet(models.QuerySet):
    def delete(self):
        self.update(deleted_at=timezone.now , is_active=False)

class BaseManager(models.Manager):
    def get_queryset (self):
        return BaseModelQuerySet( self.model, using=self._db).filter( deleted_at__isnull =True, is_active=True)

class BaseModel(models.Model):
    created_at = models.DateTimeField( auto_now_add =True)
    updated_at = models.DateTimeField( auto_now=True)
    deleted_at = models.DateTimeField( editable=False, blank=True, null=True)
    is_active = models.BooleanField( editable=False, default=True)
    
    objects = BaseManager()
    
    class Meta:
        abstract = True
    
    def delete(self, **kwargs):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()
        
    def hard_delete (self, **kwargs):
        super(BaseModel, self).delete(**kwargs)

class Secretaria(BaseModel):
    nome_secretaria = models.CharField(max_length=200)
    setor_secretaria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome_secretaria
    

class Cargo(BaseModel):
    nome_cargo = models.CharField(max_length=150)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome_cargo
    