from __future__ import unicode_literals

from colorful.fields import RGBColorField
import matrix_settings
import pypurdypixels

from django.contrib.auth.models import User
from django.db import models

Strand = pypurdypixels.Strand


# Create your models here.
class LightManager(models.Manager):
    def get_strand(self):
        num_pixels = matrix_settings.strand_length
        debug = matrix_settings.debug
        self.get_queryset().values('position', 'color')
        pixels = map(Strand.rgb2px, )
        strand = Strand(strand_length=num_pixels, debug=debug)

    def get_matrix(self):
        cols = matrix_settings.cols
        rows = matrix_settings.rows
        mapping = matrix_settings.mapping
        return pypurdypixels.Matrix(strand=self.get_strand())


class Light(models.Model):
    class Meta:
        ordering = ('position',)

    position = models.IntegerField(unique=True)
    assigned_user = models.ForeignKey(User, null=True, blank=True)
    color = RGBColorField()

    def color_as_pixel(self):
        r = self.color[1:3]
        g = self.color[3:5]
        b = self.color[5:7]
        return map(lambda x: int(x,16), (r,g,b))