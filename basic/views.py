from sts.sts import Sts
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from housekeeping_server import settings


class FileUploadViewset(ModelViewSet):

    def create(self, request):
        print(request.data.get('file'))
        return JsonResponse(data={'flag': True}, status=200)


class CredentialView(APIView):
    def get(self, request):
        config = {
            'url': 'https://sts.tencentcloudapi.com/',
            'domain': 'sts.tencentcloudapi.com',
            'ExpiredTime': 1800,
            # 临时密钥有效时长，单位是秒
            'duration_seconds': 1800,
            'secret_id': settings.SecretId,
            # 固定密钥
            'secret_key': settings.SECRET_KEY,
            # 设置网络代理
            # 'proxy': {
            #     'http': 'xx',
            #     'https': 'xx'
            # },
            # 换成你的 bucket
            'bucket': settings.Bucket,
            # 换成 bucket 所在地区
            'region': settings.Region,
            # 这里改成允许的路径前缀，可以根据自己网站的用户登录态判断允许上传的具体路径
            # 例子： a.jpg 或者 a/* 或者 * (使用通配符*存在重大安全风险, 请谨慎评估使用)
            'allow_prefix': '*',
            # 密钥的权限列表。简单上传和分片需要以下的权限，其他权限列表请看 https://cloud.tencent.com/document/product/436/31923
            'allow_actions': [
                # # 简单上传
                # 'name/cos:PutObject',
                'name/cos:PostObject',
                # 分片上传
                # 'name/cos:InitiateMultipartUpload',
                # 'name/cos:ListMultipartUploads',
                # 'name/cos:ListParts',
                # 'name/cos:UploadPart',
                # 'name/cos:CompleteMultipartUpload'
            ],

        }

        sts = Sts(config)
        response = sts.get_credential()
        return JsonResponse(data=response, status=200)
