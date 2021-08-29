from django import forms
from .models import Tag
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title','sug']
        
        widgets = {
            'title': forms.textinput(attrs={'class': 'form-control'}),
            'slug': forms.textinput(attrs={'class': 'form-control'}),
        }
    
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        
        if new_slug == 'create':
            raise ValidationError('Slug may not be "created"')
        if Tag.objects.filter(slug__iexact = new_clug).count():
            raise ValidationError('Slug must be unique, we have "{}" slug already'.format(new_slug) )
        
        return new_slug
    
    
    #def save(self):
    # new_tag = Tag.objects.create(title = self.cleaned_data['title'], slug = self.cleaned_data['slug'])
    # return new_tag
                    