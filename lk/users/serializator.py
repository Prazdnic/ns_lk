# что-то типа фабрики xdto.
# на входе получаем JSON - преобразовываем в объекты
# на входе получаем объекты - преобразовываем в JSON

import uuid

from django.contrib.auth import get_user_model

from rest_framework import serializers

class CustomUser_Serializator(serializers.ModelSerializer):

    id = serializers.UUIDField(default = uuid.uuid4) # это поле, которое хранит уникальный 128-битный идентификатор (например, 550e8400-e29b-41d4-a716-446655440000).
    password = serializers.CharField(write_only=True)


    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'full_name', 'status', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user    


class ProfileCustomUser_Serializator(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'full_name', 'status']
