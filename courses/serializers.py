from rest_framework import serializers
from .models import Course, Category,Course_Module,Course_Video
from accounts.models import CustomUser

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']




class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'course_title',
            'description',
            'instructor',
            'category',
            'content_list',
            'course_cover_image',
        ]
        read_only_fields = ['id']

    def validate_instructor(self, value):
        if value.role != 'teacher':
            raise serializers.ValidationError("Only users with role 'teacher' can be instructors.")
        return value


# Serializer for the Course_Module model
class CourseModuleSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)  
    class Meta:
        model = Course_Module
        fields = ['id', 'course', 'module_no', 'module_name']


class CourseVideoSerializer(serializers.ModelSerializer):
    module = CourseModuleSerializer(read_only=True)  
    class Meta:
        model = Course_Video
        fields = ['id', 'module', 'lecture_no', 'video_title', 'video']