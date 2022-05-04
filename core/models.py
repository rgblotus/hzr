from django.db import models

# Create your models here.

INDENT_DEPT =(
    ('me', 'Mechanical'),
    ('el', 'Electrical'),
    ('ci', 'Civil'),
    ('pl', 'Pipeline'),
    ('hr', 'HumanResource'),
    ('fi', 'Finance'),
    ('pr', 'Procurement'),
    ('in', 'Instrumentation'),
    ('op', 'Operation'),
    ('fi', 'Fire'),
    ('de', 'default'),
)

MODE_TENDERING = (
    ('lt', 'Limited'),
    ('op', 'Open'),
    ('gm', 'GeM'),
    ('ni', 'NIC'),
    ('bo', 'Board'),
    ('no', 'Nomination'),
    ('oe', 'OEM'),
    ('pa', 'PAC'),
    ('pe', 'Petty'),
    ('go', 'Govt'),
    ('rd', 'RD'),
)

INDENT_STATUS =(
    ('0', 'Clarification'),
    ('1', 'BEC'),
    ('2', 'TenderVetting'),
    ('3', 'TenderFloated'),
    ('4', 'TenderOpened'),
    ('5', 'TBAPrep'),
    ('6', 'CBAPrep'),
    ('7', 'VendorQuery'),
    ('8', 'RevisedTBA'),
    ('9', 'CBA'),
    ('10', 'PBO'),
    ('11', 'CSPrep'),
    ('12', 'CSVetting'),
    ('13', 'PriceReasonability'),
    ('14', 'Award'),
)

class Indentor(models.Model):
    # Fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dept = models.CharField(max_length=2, choices=INDENT_DEPT, blank=True, default='de')

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'{self.first_name} ({self.last_name})'

class Indent(models.Model):
    # Fields
    indentor = models.ForeignKey('Indentor', on_delete=models.RESTRICT, null=True)
    requisition_date = models.DateTimeField(null=True, blank=True)
    requisition_release_date = models.DateTimeField(null=True, blank=True)
    requisition_number = models.IntegerField()
    requisition_subject = models.CharField(max_length=150)
    requisition_plant = models.IntegerField()
    requisition_estimate = models.FloatField()
    requisition_release_cnp_date = models.DateTimeField(null=True, blank=True)
    requisition_mode_tendering = models.CharField(max_length=10, choices=MODE_TENDERING, blank=True, default='gm')
    requisition_contract_period = models.IntegerField()
  
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.requisition_number} ({self.requisition_subject})'


class IndentInstance(models.Model):
    # Fields
    indent = models.ForeignKey('Indent', on_delete=models.RESTRICT, null=True)
    indent_status = models.CharField(max_length=2, choices=INDENT_STATUS, blank=True, default='0')


    def __str__(self):
        """String for representing the Model object."""
        return f'{self.indent_status}'


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100)
    vendor_contact = models.IntegerField()
    vendor_address = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.vendor_name}'

class Order(models.Model):
    order_number = models.CharField(max_length=100)
    order_date = models.DateTimeField()
    order_reference = models.ForeignKey('Indent', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.order_number} ({self.order_date})'
