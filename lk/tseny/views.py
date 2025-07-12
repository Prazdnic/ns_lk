from django.shortcuts import render

from rest_framework import viewsets, permissions, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


from .serializers import TsenySerializer
from katalogi.models import Nomenklatura
from tseny.models import Tseny
from .permissions import IsAdminOrReadOnly



class StandartResultSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({

            'count':self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            'current_page':self.page.number,
            'per_page':self.page.paginator.per_page,
            'result': data,

        })
    


class TsenyViewSet(viewsets.ModelViewSet):
    queryset = Tseny.objects.all()
    serializer_class = TsenySerializer
    permission_classes = [IsAdminOrReadOnly] # сначала тут была permission_classes = [permissions.IsAdminUser], затем мы создали файлик permissions.py и там написали собственные роли
    pagination_class = StandartResultSetPagination

    def create(self, request, *args, **kwargs):
        try:
            nomenk = Nomenklatura.objects.filter(pk=request.data['nomenklatura']).get()
            tsena_req = request.data['tsena']
            if nomenk:
                if tsena_req == 0: # если цена равна нулю, то удаляем эту позицию
                    self.queryset.filter(nomenklatura = nomenk).delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    tsena_nomemklatury = self.queryset.filter(nomenklatura = nomenk)
                    if tsena_nomemklatury:
                        obj = tsena_nomemklatury.get()
                        obj.tsena = tsena_req
                        obj.save()
                        return Response (status = status.HTTP_206_PARTIAL_CONTENT)
                    else:
                        obj = self.queryset.create(nomenklatura = nomenk, tsena = tsena_req)
                        obj.save()
                        return Response (status = status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(data={'error':ex.__str__}, status = status.HTTP_400_BAD_REQUEST)
