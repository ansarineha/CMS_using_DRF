from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from drf_api.models import User, Content
from drf_api.serializers import UserSerializer, ContentSerializer
from .permissions import OnlyForAuthor, IsCreator
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter




@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
    
    
@api_view(['GET'])
@permission_classes((IsAuthenticated, IsCreator))
def contentList(request):
    if request.user.profile.roles == "Admin":
        contents = Content.objects.all()
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)
    elif request.user.profile.roles == "Author":
        contents = Content.objects.filter(created_by=request.user)
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)
    else:
        return Response("You are not authenticated to view this page.")




@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def contentDetail(request, pk):
    content = Content.objects.get(id=pk)
    serializer = ContentSerializer(content, many=False)
    if request.user.profile.roles in [content.created_by.profile.roles, "Admin"]:
        return Response(serializer.data)
    else:
        return Response("You are not authenticated to view contets which are not created by you...")
        
        
        
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def contentCreate(request):
    serializer = ContentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.data)




@api_view(['POST','GET'])
@permission_classes((IsAuthenticated,))
def contentUpdate(request, pk):
    content = Content.objects.get(id=pk)
    serializer = ContentSerializer(instance=content, data=request.data)
    if request.user.profile.roles in [content.created_by.profile.roles, "Admin"]:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)
    else:
        return Response("You are not authenticated to update contents which are not created by you...")




@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def contentDelete(request, pk):
    content = Content.objects.get(id=pk)
    if request.user.profile.roles in [content.created_by.profile.roles, "Admin"]:
        content.delete()
        return Response("Content successfully deleted!")
    else:
        return Response("You are not authenticated to delete contents which are not created by you...")




class ContentSearchView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes=[IsAuthenticated]
    filter_backends = ( SearchFilter, OrderingFilter)
    search_fields = ('title', 'body', 'categories', 'created_by__email')

