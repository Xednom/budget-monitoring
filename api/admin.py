from django.contrib import admin

from .models import (
        Other, Income, HomeExpense, DailyLiving, Saving, Insurance,
)


class OtherInfo(admin.ModelAdmin):
    list_display = ('name', 'budget', 'expense')
    list_filter = ['created_by']
    search_fields = ('name',)
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')
    fieldsets = (
        ('Other expense information', {
            'fields': (
                'name',
                'budget',
                'expense',
            )
        }),
        ('Important information', {
            'fields': (
                'created_by',
                'updated_by',
                'created_at',
                'updated_at',
            )
        })
    )


class IncomeInfo(admin.ModelAdmin):
    list_display = ('wages_and_tips', 'interest_income', 'dividends', 'gifts_received', 'refunds_reimbursement',
                    'transfer_from_savings', 'total_income')
    list_filter = ['created_by']
    search_fields = ('users__first_name', 'users__last_name')
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')
    fieldsets = (
        ('Income information', {
            'fields': (
                'wages_and_tips',
                'interest_income',
                'dividends',
                'gifts_received',
                'refunds_reimbursement',
                'transfer_from_savings',
                'total_income',
                'users',
                'other'
            )
        }),
        ('Important information', {
            'fields': (
                'created_by',
                'updated_by',
                'created_at',
                'updated_at',
            )
        })
    )


class HomeExpenseInfo(admin.ModelAdmin):
    list_display = ('mortage', 'electricity', 'gas', 'water_sewer_trash', 'phone',
                    'cable', 'internet', 'appliances', 'garden', 'home_supplies', 'maintenance',
                    'improvements', 'total_home_expenses')
    list_filter = ['created_by']
    search_fields = ('users__first_name', 'users__last_name')
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')
    fieldsets = (
        ('Home expense information', {
            'fields': (
                'mortage',
                'electricity',
                'gas',
                'water_sewer_trash',
                'phone',
                'cable',
                'internet',
                'appliances',
                'garden',
                'home_supplies',
                'maintenance',
                'improvements',
                'total_home_expenses',
                'users',
                'other'
            )
        }),
        ('Important information', {
            'fields': (
                'created_by',
                'updated_by',
                'created_at',
                'updated_at',
            )
        })
    )


class DailyLivingInfo(admin.ModelAdmin):
    list_display = ('groceries', 'personal_supplies', 'clothing', 'cleaning_services', 'dining',
                    'dry_cleaning', 'salon', 'total_daily_expenses', 'users')
    list_filter = ['created_by']
    search_fields = ('users__first_name', 'users__last_name')
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')
    fieldsets = (
        ('Daily Living expense information', {
            'fields': (
                'groceries',
                'personal_supplies',
                'clothing',
                'cleaning_services',
                'dining',
                'dry_cleaning',
                'salon',
                'total_daily_expenses',
                'users',
                'other',
            )
        }),
        ('Important information', {
            'fields': (
                'created_by',
                'updated_by',
                'created_at',
                'updated_at',
            )
        })
    )


class SavingInfo(admin.ModelAdmin):
    list_display = ('emergency_funds', 'car_replacement_fund', 'retirement_fund', 'investments', 'education_funds',
                    'total_savings', 'users')
    list_filter = ['created_by']
    search_fields = ('users__first_name', 'users__last_name')
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')
    fieldsets = (
        ('Saving information', {
            'fields': (
                'emergency_funds',
                'car_replacement_fund',
                'retirement_fund',
                'investments',
                'education_funds',
                'total_savings',
                'users',
                'other',
            )
        }),
        ('Important information', {
            'fields': (
                'created_by',
                'updated_by',
                'created_at',
                'updated_at',
            )
        })
    )


class InsuranceInfo(admin.ModelAdmin):
    list_display = ('auto', 'health', 'home', 'life', 'total_insurance',
                    'users')
    list_filter = ['created_by']
    search_fields = ('users__first_name', 'users__last_name')
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')
    fieldsets = (
        ('Insurance information', {
            'fields': (
                'auto',
                'health',
                'home',
                'life',
                'total_insurance',
                'users',
                'other',
            )
        }),
        ('Important information', {
            'fields': (
                'created_by',
                'updated_by',
                'created_at',
                'updated_at',
            )
        })
    )


admin.site.register(Other, OtherInfo)
admin.site.register(Income, IncomeInfo)
admin.site.register(HomeExpense, HomeExpenseInfo)
admin.site.register(DailyLiving, DailyLivingInfo)
admin.site.register(Saving, SavingInfo)
admin.site.register(Insurance, InsuranceInfo)