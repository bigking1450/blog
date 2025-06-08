from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'cover_image',
                  'intro_images', 'body_images', 'tags']

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['title'].widget.attrs.update({'class': 'form-control'})
            self.fields['excerpt'].widget.attrs.update(
                {'class': 'form-control'})
            self.fields['content'].widget.attrs.update(
                {'class': 'form-control'})
            self.fields['cover_image'].widget.attrs.update(
                {'class': 'form-control-file'})
            self.fields['intro_images'].widget.attrs.update(
                {'class': 'form-control'})
            self.fields['body_images'].widget.attrs.update(
                {'class': 'form-control'})
            # self.fields['tags'].widget.attrs.update({'multiple': 'multiple'})
            self.fields['tags'].widget.attrs.update(
                {'class': 'form-control select2'})
