from annoying.functions import get_object_or_None
from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

from config import constants
from core.mixins import CustomLoginRequiredMixin, OwnerRequiredMixin
from users.models import User
from .models import Video, Tag


class VideoListMixin(ListView):
    model = Video
    paginate_by = constants.PAGINATE_BY

    def __url_params(self):
        model_kwargs = {}

        # user
        user = self.request.GET.get('user', '')
        if user != '':
            model_kwargs['user'] = User.objects.filter(username=user)

        # title
        title = self.request.GET.get('title', '')
        if title != '':
            model_kwargs['title__contains'] = title

        # tags
        tags = self.request.GET.get('tags', '')
        if tags != '':
            model_kwargs['tags'] = Tag.objects.get_videos_by_tags(tags)

        return model_kwargs

    def get_queryset(self):
        queryset = self.model.objects.filter(**self.__url_params())
        return queryset


class VideoDetailMixin(DetailView):
    model = Video

    @transaction.atomic
    def get_object(self, queryset=None):
        object = super(VideoDetailMixin, self).get_object(queryset)
        object.analytic.views += 1
        object.analytic.save()
        return object


class VideoUserListMixin(ListView):
    model = Video
    paginate_by = constants.PAGINATE_BY

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        queryset = self.model.objects.filter(user=user)
        return queryset


class VideoByTagListMixin(ListView):
    model = Tag
    paginate_by = constants.PAGINATE_BY

    def get_queryset(self):
        tags = self.kwargs['tags'].split(',')
        queryset = Video.objects.none()
        for tag in tags:
            tag_queryset = get_object_or_None(self.model, name=tag)
            if tag_queryset is not None:
                queryset = queryset | \
                           self.model.objects.get(name=tag).videos.all()
        return queryset.distinct()


class TagListMixin(ListView):
    model = Tag
    paginate_by = constants.PAGINATE_BY


class VideoCreateMixin(CustomLoginRequiredMixin, CreateView):
    model = Video

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VideoCreateMixin, self).form_valid(form)


class VideoEditMixin(OwnerRequiredMixin, UpdateView):
    model = Video


class VideoDeleteMixin(OwnerRequiredMixin, DeleteView):
    model = Video
