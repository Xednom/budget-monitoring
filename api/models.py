from django.db import models

from users.models import User


class BaseModel(models.Model):
    status = models.BooleanField(default=True, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=150, null=True, blank=True)
    updated_by = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        abstract = True


class Other(BaseModel):
    name = models.CharField(max_length=150, null=True, blank=True)
    budget = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    expense = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return "%s" % (self.name)


class Income(BaseModel):
    wages_and_tips = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    interest_income = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    dividends = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    gifts_received = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    refunds_reimbursement = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    transfer_from_savings = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    total_income = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    users = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    other = models.ManyToManyField(Other)

    class Meta:
        ordering = ['-created_at']

    def calculate_total_income(self):
        overall_income = self.wages_and_tips + self.interest_income + self.dividends + \
                         self.gifts_received + self.refunds_reimbursement + self.transfer_from_savings
        return overall_income
    
    def save(self, *args, **kwargs):
        self.total_income = self.calculate_total_income()
        super().save(*args, **kwargs)                 

    def __str__(self):
        return "Total income is %s" % (self.total_income)


class HomeExpense(BaseModel):
    mortage = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    electricity = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    gas = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    water_sewer_trash = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    phone = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    cable = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    internet = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    appliances = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    garden = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    home_supplies = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    maintenance = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    improvements = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    total_home_expenses = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    users = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    other = models.ManyToManyField(Other)

    class Meta:
        ordering = ['-created_at']

    def calculate_home_expenses(self):
        total_home_expenses = self.mortage + self.electricity + self.gas + self.water_sewer_trash + self.phone + \
                              self.cable + self.internet + self.appliances + self.garden + self.home_supplies + \
                              self.maintenance + self.improvements
        return total_home_expenses
    
    def save(self, *args, **kwargs):
        self.total_home_expenses = self.calculate_home_expenses()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Total home expenses: %s" % (self.total_home_expenses)

    
class DailyLiving(BaseModel):
    groceries = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    personal_supplies = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    clothing = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    cleaning_services = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    dining = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    dry_cleaning = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    salon = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    total_daily_expenses = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    users = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    other = models.ManyToManyField(Other)

    class Meta: 
        ordering = ['-created_at']

    def calculate_total_daily_expense(self):
        total_daily_expense = self.groceries + self.personal_supplies + self.clothing + self.cleaning_services + \
                              self.dining + self.dry_cleaning + self.salon
        return total_daily_expense
    
    def save(self, *args, **kwargs):
        self.total_daily_expenses = self.calculate_total_daily_expense
        super().save(*args, **kwargs)
    
    def __str__(self):
        return "Total daily expenses: %s" % (self.total_daily_expenses)


class Saving(BaseModel):
    emergency_funds = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    car_replacement_fund = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    retirement_fund = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    investments = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    education_funds = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    total_savings = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    users = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    other = models.ManyToManyField(Other)

    class Meta: 
        ordering = ['-created_at']

    def calculate_total_savings(self):
        total_saving = self.emergency_funds + self.car_replacement_fund + self.retirement_fund + self.investments + \
                              self.education_funds
        return total_saving
    
    def save(self, *args, **kwargs):
        self.total_savings = self.calculate_total_savings
        super().save(*args, **kwargs)
    
    def __str__(self):
        return "Total savings: %s" % (self.total_savings)


class Insurance(BaseModel):
    auto = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    health = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    home = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    life = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    total_insurance = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    users = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    other = models.ManyToManyField(Other)

    class Meta: 
        ordering = ['-created_at']

    def calculate_total_insurance(self):
        total_saving = self.auto + self.health + self.home + self.life
        return total_saving
    
    def save(self, *args, **kwargs):
        self.total_savings = self.calculate_total_savings
        super().save(*args, **kwargs)
    
    def __str__(self):
        return "Total savings: %s" % (self.total_savings)