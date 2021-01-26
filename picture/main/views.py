from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm, ResizeForm
from django.views.generic import DetailView
from urllib.parse import urlparse
import requests
from django.core.files.base import ContentFile
import PIL
import os


def index(request):
    images = Image.objects.all()
    return render(request, 'main/index.html', {'images': images})


class ImagesView(DetailView):
    model = Image

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = ResizeForm
        data = {
            'image': context['image'],
            'form': form,
        }
        template_name = 'main/picture.html'
        return render(request, template_name, data)

    def post(self, request, *args, **kwargs):
        template_name = 'main/picture.html'
        form = ResizeForm(request.POST)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        path = self.get_object().image.path
        img = PIL.Image.open(path)
        height = form.data['height']
        width = form.data['width']
        if height != '' and width != '':
            height = int(height)
            width = int(width)
            error = 'Измененный размер {}*{}'.format(width, height)
        elif height != '':
            height = int(height)
            width = int(img.width) * height / int(img.height)
            error = 'Измененный размер {}*{}'.format(width, height)
        elif width != '':
            width = int(width)
            height = int(img.height) * width / int(img.width)
            error = 'Измененный размер {}*{}'.format(width, height)
        else:
            height = int(img.height)
            width = int(img.width)
            error = 'Оригинальный размер {}*{}'.format(width, height)
        path = path.split('\\')[-1]
        if int(width) == int(img.width) and int(height) == int(img.height):
            try:
                os.remove('media/images/resize/' + path)
                self.object.image_url = None
            except FileNotFoundError:
                error = 'Введите ширину и высоту'
        else:
            img = img.resize((int(width), int(height)), PIL.Image.ANTIALIAS)

            img.save('picture/media/images/resize/' + path)

            self.object.image_url = '/media/images/resize/' + path
        self.object.save()
        data = {
            'image': context['image'],
            'form': form,
            'error': error
        }
        return render(request, template_name, data)


def new(request):
    error = ''
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if len(form.files) == 1 and form.data['image_url'] == '' and form.is_valid():
            form.save()
            id = Image.objects.last().id
            return redirect('image', id)
        elif len(form.files) == 0 and form.data['image_url'] != '' and form.is_valid():
            img_url = form.data['image_url']
            name = urlparse(img_url).path.split('/')[-1]
            photo = Image()
            ignored_extensions = '.png', '.gif', '.jpg', '.jpeg'
            if img_url.endswith(ignored_extensions):
                response = requests.get(img_url)
                if response.status_code == 200:
                    photo.image.save(name, ContentFile(response.content), save=True)
                    id = Image.objects.last().id
                    return redirect('image', id)
            else:
                error = 'Неправильный URL'
        else:
            error = 'Неправильные данные'
    form = ImageForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/new.html', data)
