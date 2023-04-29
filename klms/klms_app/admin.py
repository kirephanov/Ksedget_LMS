from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


# Формы CKEditor
class LessonAdminForm(forms.ModelForm):
    lesson_exercise = forms.CharField(widget=CKEditorUploadingWidget())
    lesson_homework = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Lesson
        fields = '__all__'


class ArticleAdminForm(forms.ModelForm):
    article_content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


# Подключение таблиц к сайту администратора
class CourseAdmin(admin.ModelAdmin):
    # В этом случае к курсам подключается поле course_age для создания категории Возраст
    # list_display = ('id', 'сourse_title', 'course_category', 'course_age', 'course_created_at', 'course_icon')
    # list_display_links = ('id', 'сourse_title', 'course_category', 'course_age', 'course_created_at', 'course_icon')
    
    # Стандартное подключение без поля course_age для создания категории Возраст
    list_display = ('id', 'сourse_title', 'course_category', 'course_created_at', 'course_icon')
    list_display_links = ('id', 'сourse_title', 'course_category', 'course_created_at', 'course_icon')
    search_fields = ('сourse_title',)
    list_filter = ('course_category',)


class LessonAdmin(admin.ModelAdmin):
    form = LessonAdminForm
    list_display = ('id', 'lesson_title', 'lesson_сourse', 'lesson_created_at', 'lesson_video')
    list_display_links = ('id', 'lesson_title', 'lesson_сourse', 'lesson_created_at', 'lesson_video')
    search_fields = ('lesson_title',)
    list_filter = ('lesson_сourse',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_title')
    list_display_links = ('id', 'category_title')
    search_fields = ('category_title',)


# class AgeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'age_title')
#     list_display_links = ('id', 'age_title')
#     search_fields = ('age_title',)


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'homework_title', 'homework_course', 'homework_lesson', 'homework_author', 'homework_file', 'homework_verified')
    list_display_links = ('id', 'homework_title', 'homework_course', 'homework_lesson', 'homework_author', 'homework_file')
    search_fields = ('homework_title', 'homework_author')
    list_filter = ('homework_course', 'homework_lesson')


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('id', 'article_title', 'article_category', 'article_created_at', 'article_photo')
    list_display_links = ('id', 'article_title', 'article_category', 'article_created_at', 'article_photo')
    search_fields = ('article_title',)
    list_filter = ('article_category',)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'feedback_name', 'feedback_email', 'feedback_message', 'feedback_created_at')
    list_display_links = ('id', 'feedback_name', 'feedback_email', 'feedback_message', 'feedback_created_at')
    search_fields = ('feedback_message',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Age, AgeAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Feedback, FeedbackAdmin)


admin.site.site_title = 'Управление Ksedget LMS'
admin.site.site_header = 'Управление Ksedget LMS'