from rest_framework.serializers import ModelSerializer, SerializerMethodField

from issues.models import Issue


class IssuesSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'uid', 'description', 'serial', 'indicator1', 'indicator2', 'indicator3',
                  'date_time', 'response']


"""
response = SerializerMethodField()
    
    def save(self, **kwargs):
        print(self.validated_data)
        return super().save(**kwargs)
"""
