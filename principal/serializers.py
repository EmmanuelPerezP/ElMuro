from rest_framework import serializers


class VotingSerializer(serializers.Serializer):
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
        """
        if value not in [1, -1, 2, -2]:
            raise serializers.ValidationError("Invalid Vote Action")
        return value
