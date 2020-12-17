from house.models import Group_Field, Assignment, Group_Category
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        User = UserSerializer()
        model = Group_Field
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        User = UserSerializer()
        model = Assignment
        fields = '__all__'

class GroupCategorySerializer(serializers.ModelSerializer):
    class Meta:
        User = UserSerializer()
        model = Group_Category
        fields = '__all__'
