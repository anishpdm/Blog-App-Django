from rest_framework import serializers
from userblogs.models import Users,Blogs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'username', 'password','id')
        

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields=('message','userid')        