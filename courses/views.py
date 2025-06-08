# yourapp/views.py
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Category,Course,Course_Module,Course_Video
from .serializers import CategorySerializer,CourseSerializer,CourseModuleSerializer,CourseVideoSerializer
from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_category(request):
    if request.user.role != 'admin':
        return Response({'detail': 'Only admins can create categories.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def add_course(request):
    user = request.user
    if user.role != 'teacher':
        return Response({'detail': 'Only teachers can create courses.'}, status=status.HTTP_403_FORBIDDEN)

    data = request.data.copy()
    data['instructor'] = user.id

    serializer = CourseSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_course(request):
    """Create a new course"""
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Created
        return Response(serializer.errors, status=400)  # Bad request

@api_view(['GET'])
def list_courses(request):
    """List all courses"""
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

# Course Module Views

@api_view(['POST'])
def create_course_module(request):
    """Create a new course module"""
    if request.method == 'POST':
        serializer = CourseModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Created
        return Response(serializer.errors, status=400)  # Bad request

@api_view(['GET'])
def list_course_modules(request):
    """List all course modules"""
    course_modules = Course_Module.objects.all()
    serializer = CourseModuleSerializer(course_modules, many=True)
    return Response(serializer.data)

# Course Video Views

@api_view(['POST'])
def create_course_video(request):
    """Create a new course video"""
    if request.method == 'POST':
        serializer = CourseVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Created
        return Response(serializer.errors, status=400)  # Bad request

@api_view(['GET'])
def list_course_videos(request):
    """List all course videos"""
    course_videos = Course_Video.objects.all()
    serializer = CourseVideoSerializer(course_videos, many=True)
    return Response(serializer.data)
