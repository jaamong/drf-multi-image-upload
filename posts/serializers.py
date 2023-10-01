from rest_framework import serializers
from .models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']


class PostSerializer(serializers.ModelSerializer):
    """
    1 : N = Post : PostImage 관계
    => 1에 해당하는 model 기준으로 nested Serializer 생성 (Reverse relations)


    - many=True : for 다중 이미지 업로드
    - read_only=True <= Nested Serializer 에서는 Create, Update 지원 X
    """
    images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'text', 'images']

    def create(self, validated_data):  # validated_data : dict 형태, images_data 외에 body에서 form-data로 넘겨준 값들 (Model의 field 값들)
        images_data = self.context['request'].FILES  # 파일 형식으로 전달받은 데이터 담기
        post = Post.objects.create(**validated_data)

        for image_data in images_data.getlist('image'):
            PostImage.objects.create(post=post, image=image_data)

        return post



