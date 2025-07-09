from rest_framework import viewsets, permissions, exceptions
from .serializator import CustomUser_Serializator, ProfileCustomUser_Serializator
# удалили импорт нашей модели и делаем более универсальный способ к обращению к модели пользователя
from django.contrib.auth import get_user_model

# в этом куске кода уже включены и описаны все CRUD-операций (Create, Read, Update, Delete). В урлз тоже подобный кусок
class CustomUser_Viewha(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUser_Serializator
    permission_classes = [permissions.IsAdminUser] # пользоваться разрешено только Админу. Если не залогиниться, то выскочит сообщение "Учетные данные не были предоставлены"



class ProfileCustomUser_Viewha(viewsets.ReadOnlyModelViewSet): # ReadOnlyModelViewSet - означает, что мы возвращаем данные только для чтения
    serializer_class = ProfileCustomUser_Serializator
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user:
            user = get_user_model().objects.filter(pk=self.request.user.pk)
            if user is None:
                raise exceptions.AuthenticationFailed('Пользователь не найден')
            return user