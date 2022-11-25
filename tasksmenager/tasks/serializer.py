from .models import Tasks, Vote 
from rest_framework import serializers


class TasksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id','title','description','files','URL','priority']

class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ['tasks','usersVote']