from rest_framework import viewsets, permissions, exceptions, status
from .serializator import CustomUser_Serializator, ProfileCustomUser_Serializator
# удалили импорт нашей модели и делаем более универсальный способ к обращению к модели пользователя
from django.contrib.auth import get_user_model
# Вместе со status добавили в 5й части для логаута
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

# в этом куске кода уже включены и описаны все CRUD-операций (Create, Read, Update, Delete). В урлз тоже подобный кусок
class CustomUser_Viewha(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUser_Serializator
    permission_classes = [permissions.IsAdminUser] # пользоваться разрешено только Админу. Если не залогиниться, то выскочит сообщение "Учетные данные не были предоставлены"



class ProfileCustomUser_Viewha(viewsets.ReadOnlyModelViewSet): # ReadOnlyModelViewSet - означает, что мы возвращаем данные только для чтения
    # В Части 6 почти полностью переписали функцию, удалили get_queryset
    
    queryset = get_user_model().objects.all()
    serializer_class = ProfileCustomUser_Serializator
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     if self.request.user:
    #         user = get_user_model().objects.filter(pk=self.request.user.pk)
    #         if user is None:
    #             raise exceptions.AuthenticationFailed('Пользователь не найден')
    #         return user
        
    def list(self, request, *args, **kwargs):
        profil = self.get_queryset().get(pk=self.request.user.pk) # get_queryset() - это как Выборка результата запроса в 1С
        serializator = self.get_serializer(profil)

        return Response({'user': serializator.data})

# Чтобы разлогиниться - мы принимаем рефреш токен (чтобы нам прислали новый для продолжения сессии), мы его создаем и сразу же баним.
# Таким образом сессия прерывается
class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated) # Разлогиниться может только авторизованный (логично)

    def post(self, request):

        try:

            token_obnovlenia = request.data["refresh"]
            novy_token = RefreshToken(token_obnovlenia)
            novy_token.blacklist()

            return Response(status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

