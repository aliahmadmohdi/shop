from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from pygments import highlight
from pygments.formatters.html import HtmlFormatter

# Create your models here.


class Mov(models.Model):
    name = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    imdb_score =  models.DecimalField(max_digits=2, decimal_places=1)
    popularity = models.DecimalField('99popularity',max_digits=3, decimal_places=1)
    owner = models.ForeignKey('auth.User',related_name='owner')
    def save(self,*args,**kwargs):
    	name = self.name
    	director = self.director
    	imdb_score = self.imdb_score
    	popularity = self.popularity
    	# self.highlighted = highlight(name,director,popularity,imdb_score)
    	super(Mov,self).save(*args,**kwargs)

class Genre(models.Model):
	genre = models.ForeignKey(Mov,related_name='genre')
	name = models.CharField(max_length=200)
	class Meta:
        # unique_together = ('name','genre')
		ordering = ('name',)
	def __unicode__(self):
		return "%s" % (self.name)