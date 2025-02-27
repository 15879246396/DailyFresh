import time
import os
from django.conf import settings
from django.http.response import StreamingHttpResponse, HttpResponse, FileResponse
# from django.core.servers.basehttp import
from wsgiref.util import FileWrapper
from django.core.cache import cache
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.permissions import IsAuthenticated

from account.permissions import IsLogin
from common.decorator import common_api, file_response_common_api
from common.utils import generate_bsc
from base.exceptions import ValidateException
from upload.models import FileUpload
from upload.serializers import FileUploadSerializer
from upload.utils import update_file_data


class FileAPIViewSet(GenericViewSet, CreateModelMixin):
    # permission_classes = (IsAuthenticated, )
    permission_classes = (IsLogin, )
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, JSONParser)
    queryset = FileUpload.objects.all()
    pagination_class = None

    @common_api
    def create(self, request, *args, **kwargs):
        request.data['uploader'] = request.user.id
        instance = super(FileAPIViewSet, self).create(request, *args, **kwargs)
        update_file_data(instance.data)
        return instance


class CMSFileAPIViewSet(GenericViewSet, CreateModelMixin):
    permission_classes = (IsAuthenticated, )
    # permission_classes = (IsLogin, )
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, JSONParser)
    queryset = FileUpload.objects.all()
    pagination_class = None

    @common_api
    def create(self, request, *args, **kwargs):
        request.data['uploader'] = request.user.id
        instance = super(FileAPIViewSet, self).create(request, *args, **kwargs)
        update_file_data(instance.data)
        return instance


@api_view(['GET', ])
@file_response_common_api
def file_download(request):
    file_name = request.query_params.get('file_name')
    if not file_name:
        raise ValidateException().add_message("error:params error", "缺少文件名")
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    if not os.path.exists(file_path):
        raise ValidateException().add_message("error:file not found", "未找到对应文件")
    file_info = FileUpload.objects.filter(file=file_name).first()
    if file_info:
        file_name = file_info.file_name
    # fw = FileWrapper(open(file_path, 'rb'))
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
    return response






