from django.contrib import admin
from .models import *


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'lastname')


admin.site.register(Candidate, CandidateAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Skill, SkillAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Language, LanguageAdmin)


class HobbyAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Hobby, HobbyAdmin)