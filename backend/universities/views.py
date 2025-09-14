from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import University
from .serializers import UniversitySerializer


class UniversityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        if query:
            universities = University.objects.filter(
                models.Q(name__icontains=query) | 
                models.Q(chinese_name__icontains=query) |
                models.Q(location__icontains=query)
            )
        else:
            universities = University.objects.all()
        
        serializer = self.get_serializer(universities, many=True)
        return Response(serializer.data)
