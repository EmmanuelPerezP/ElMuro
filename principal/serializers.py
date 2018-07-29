from rest_framework import serializers


class PostVotingSerializer(serializers.Serializer):
    """
    modelId: the model we are upvoting or downvoting
    action: 1,0,-1 = upvote, neutral, downvote
    """
    postId = serializers.IntegerField(required=True)
    action = serializers.IntegerField(required=True)

    # def create(self, validated_data)
    #     pass

    def validate_action(self, value):
        """
        Check that the blog post is about Django.
        """
        if value not in [1, 0, -1]:
            raise serializers.ValidationError("Invalid Vote Action")
        return value

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance