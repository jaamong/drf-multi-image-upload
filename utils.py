import os
from uuid import uuid4
from django.utils import timezone


def rename_image_to_uuid(instance, filename):
    """
    @param
        - instance: Post Model에서 __str__ 로 반환해주는 값
        - filename: -
    @return: post_images/{date}/{uuid}.{ext}
    @description:
        - 이미지 업로드 시 이미지 파일 이름을 uuid로 변경
        - 이미지 저장 위치 문자열 생성 + 변경된 이름 -> 반환
    """

    date = timezone.now().strftime('%Y/%m/%d')  # 업로드 날짜에 따라 디렉토리에 저장
    upload_to = f'post_images/{date}'

    ext = filename.split('.')[-1].lower()
    uuid = uuid4().hex  # 길이 32인 uuid 값
    filename = '{}.{}'.format(uuid, ext)

    return os.path.join(upload_to, filename)
