from rest_framework import viewsets, permissions
from .serializator import CustomUser_Serializator
from .models import CustomUser

# в этом куске кода уже включены и описаны все CRUD-операций (Create, Read, Update, Delete). В урлз тоже подобный кусок
class CustomUser_Viewha(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUser_Serializator
    permission_classes = [permissions.IsAdminUser] # пользоваться разрешено только Админу. Если не залогиниться, то выскочит сообщение "Учетные данные не были предоставлены"
