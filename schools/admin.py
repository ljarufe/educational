from django.contrib import admin
from django.db.models import Q

from .models import Student, School, Application


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name",)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("student", "school", "application_date", "status")
    list_filter = ("status", "application_date")
    search_fields = ("student__first_name", "student__last_name", "school__name")


class AgeFilter(admin.SimpleListFilter):
    title = 'age'
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        return [
            ('<18', 'Under 18'),
            ('18-25', '18 to 25'),
            ('26-35', '26 to 35'),
            ('36-45', '36 to 45'),
            ('46+', '46 and above'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<18':
            return queryset.filter(birth_date__gt='2006-01-01')
        if self.value() == '18-25':
            return queryset.filter(birth_date__range=['1998-01-01', '2005-12-31'])
        if self.value() == '26-35':
            return queryset.filter(birth_date__range=['1988-01-01', '1997-12-31'])
        if self.value() == '36-45':
            return queryset.filter(birth_date__range=['1978-01-01', '1987-12-31'])
        if self.value() == '46+':
            return queryset.filter(birth_date__lt='1978-01-01')
        return queryset


class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "tutor", "enrollment_date")
    search_fields = ("first_name", "last_name", "tutor__email")
    list_filter = (AgeFilter, )
    inlines = [ApplicationInline]

    def get_search_results(self, request, queryset, search_term):
        search_terms = search_term.split()
        if len(search_terms) == 2:
            queryset = queryset.filter(
                Q(first_name__icontains=search_terms[0], last_name__icontains=search_terms[1]) |
                Q(first_name__icontains=search_terms[1], last_name__icontains=search_terms[0])
            )
            return queryset, False
        return super().get_search_results(request, queryset, search_term)
