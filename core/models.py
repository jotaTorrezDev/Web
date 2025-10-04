from django.db import models
from stdimage import StdImageField

#SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify



class Base(models.Model):
    criado_at = models.DateField('Data de criacao', auto_now_add=True)
    modificado_at = models.DateField('Data de atualizacao',auto_now=True)
    ativo = models.BooleanField('ativo', default=True)

    class Meta:
        abstract = True
# Create your models here.

class Produto(Base):
    nome = models.CharField('Nome',max_length=100)
    preco = models.DecimalField('Preco',decimal_places=2,max_digits=10)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produto', variations={'thumb': (124, 124)})
    #imagem = models.ImageField('Imagem',upload_to='produto/')
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance,sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)