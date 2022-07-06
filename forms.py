from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators, IntegerField, SelectField, RadioField, FloatField
from wtforms.widgets import HiddenInput
from wtforms import MultipleFileField, SelectMultipleField, widgets, TextAreaField
import json
import re
from wtforms.fields.html5 import DateTimeLocalField, DateField,TimeField
from datetime import datetime, timedelta
from flask_wtf.file import FileField
from wtforms.widgets import TextArea

f = open('contacts.json')
columns = json.load(f)
con = columns["users"]
users = []
for i in con:
    users.append(tuple(i.values()))

com = columns["ABD"]
communities = []
communities.append(("9999","None"))
file_data = str(columns["ABD"][0]).replace('{','').replace('}','').replace(', ',',').replace(': ',':')
file_data = re.sub("'","",file_data).split(',')
for i in file_data:
    communities.append(tuple(i.split(':')))



fea = columns["Features"]
features = []
file_data = list(fea[0].values())
for i in file_data:
    features.append(tuple((i,i)))

ame = columns["Amenities"]
amenities = []
file_data = list(ame[0].values())
for i in file_data:
    amenities.append(tuple((i,i)))

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class LoginForm(FlaskForm):
    username = StringField('USERNAME', [validators.Length(min=4, max=50)])
    password = PasswordField('PASSWORD', [validators.DataRequired()])


class AddUserForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    password = StringField('Password', [validators.DataRequired()])
    number = IntegerField('Contact Number', [validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=4, max=80),validators.DataRequired()])
    job_title = StringField('Job Title', [validators.Length(min=4, max=25), validators.DataRequired()])
    department = StringField('Department', [validators.Length(min=4, max=25), validators.DataRequired()])
    

class AddPropertyForm(FlaskForm):
    status = SelectField(u'Status',choices = [('Available', 'Available'), ('Archive', 'Archive'), ('Expired', 'Expired'),('Blocked', 'Blocked'), ('Pending', 'Pending'), ('Moved In', 'Moved In'), ('Rented', 'Rented'), ('Reserved', 'Reserved'), ('Owner Occupied','Owner Occupied'), ('Sold', 'Sold'), ('Upcoming', 'Upcoming')])
    city = SelectField(u'Emirate *',[validators.DataRequired()],choices = [('Abu Dhabi', 'Abu Dhabi'), ('Dubai', 'Dubai'), ('Al Ain', 'Al Ain'), ('Sharjah', 'Sharjah'), ('Fujairah', 'Fujairah'), ('Ras Al Khaimah', 'Ras Al Khaimah'), ('Umm Al Quwain', 'Umm Al Quwain')])
    type = RadioField('Purpose',[validators.DataRequired()], choices=[('Rent','Rent'),('Sale','Sale')], default=0)
    subtype = SelectField(u'Type *',[validators.DataRequired()],choices = [('Villa', 'Villa'), ('Apartment', 'Apartment'),('Loft Apartment', 'Loft Apartment'), ('Residential Floor', 'Residential Floor'), ('Residential Plot', 'Residential Plot'), ('Townhouse', 'Townhouse'), ('Residential Building', 'Residential Building'), ('Penthouse', 'Penthouse'), ('Villa Compound', 'Villa Compound'), ('Hotel Apartment', 'Hotel Apartment'), ('Office', 'Office'),('Land','Land'), ('Other', 'Other')])
    title = StringField('Title *',[validators.DataRequired()])
    description = TextAreaField('Description *',[validators.DataRequired()], widget=TextArea())
    unit = StringField('Unit *', [validators.DataRequired(),validators.Length(min=4, max=50)])
    plot = StringField('Unit Floor/Plot', [validators.Length(min=4, max=50)])
    street = StringField('Street', [validators.Length(min=4, max=50)])
    size = FloatField('Build Area *', [validators.DataRequired()])
    plot_size = FloatField('Plot Size')
    price = IntegerField('Price *', [validators.DataRequired()])
    price_per_area = FloatField('Price Per Area')
    rentpriceterm = SelectField(u'Frequency',choices = [('Yearly', 'Yearly'), ('Monthly', 'Monthly'), ('Quaterly','Quaterly'),('Weekly', 'Weekly'), ('Daily', 'Daily')])
    #pricecurrency = StringField('Currency', [validators.Length(min=4, max=50)])
    commission = IntegerField('Commission (%)')
    deposit = IntegerField('Deposit (%)')
    bedrooms = SelectField(u'Beds *',[validators.DataRequired()],choices = [('ST', 'ST'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),('10+', '10+'),(0,'Other')])
    locationtext = SelectField(u'Community *',[validators.DataRequired()],choices = communities)
    furnished = RadioField('Furnished', choices=[(0,'No'),(1,'Yes')], default=0)
    building = SelectField(u'Location *',[validators.DataRequired()],choices = [])
    privateamenities = MultiCheckboxField('Property Features', choices=features)
    commercialamenities = MultiCheckboxField('Commercial Amenities',choices=amenities)
    photos = MultipleFileField('File(s) Upload')
    new_files = RadioField('Delete Uploaded Images',[validators.DataRequired()], choices=[(0,'No'),(1,'Yes')], default=0)
    geopoint = StringField('GeoPoint (LAT,LON) *')
    bathrooms = SelectField(u'Baths',choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'),(0,'Other')])
    permit_number = StringField('Permit Number', [validators.Length(min=4, max=50)])
    view360 = StringField('View 360', [validators.Length(min=4, max=50)])
    video_url = StringField('Video URL', [validators.Length(min=4, max=100)])
    completion_status = SelectField(u'Completion Status',choices = [('offplan', 'Off-Plan'), ('completed', 'Completed Property')])
    offplan_status = SelectField(u'Construction Status (if offplan)',choices = [('', ''),('not started', 'Not Started'), ('under construction', 'Under Constrution')])
    completion_date = DateField('Completion Date (If offplan)', format='%Y-%m-%d')
    source = SelectField(u'Source',choices = [('Cold Call', 'Cold Call'),('Client Referral','Client Referral'),('Direct Client','Direct Client'), ('Whatsapp', 'Whatsapp'), ('Email', 'Email'), ('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Company Website', 'Company Website'), ('Dubizzle', 'Dubizzle'), ('Google', 'Google'), ('Agent', 'Agent'), ('Bayut', 'Bayut'), ('Property Finder', 'Property Finder'), ('Walk-In', 'Walk-In')])
    owner = StringField('Owner *',[validators.DataRequired()],render_kw={"style":"pointer-events: none;"})
    tenant = StringField('Tenant')
    owner_name = StringField('Name *', [validators.DataRequired(),validators.Length(min=4, max=100)],render_kw={"style":"pointer-events: none;"})
    owner_contact =IntegerField('Contact *',[validators.DataRequired()],render_kw={"style":"pointer-events: none;"})
    owner_email = StringField('Email *', [validators.DataRequired(),validators.Length(min=4, max=100)],render_kw={"style":"pointer-events: none;"})
    expiry_date = DateField('Expiry Date', format='%Y-%m-%d')
    assign_to = SelectField(u'Assign To',choices = [])
    tenure = SelectField(u'Tenure',choices = [(0, 'Leasehold'), (1, 'Freehold')])
    featured = SelectField(u'Featured',choices = [(0, 'No'), (1, 'Yes')])
    parking = SelectField(u'Parking',choices = [(None,'-'),(1, '1'), (2, '2'), (3, '3')])
    portal = SelectField(u'Add to Portals',choices = [(0, "Yes"), (1, "No")])

class AddContactForm(FlaskForm):
    title = SelectField(u'Title',choices = [('','Select'),('Mr', 'Mr'),('Mrs','Mrs'),('Ms','Ms'),('Miss','Miss'),('Sir','Sir')])
    first_name = StringField('First Name *', [validators.Length(min=4, max=25), validators.DataRequired()])
    last_name = StringField('Last Name *', [validators.Length(min=4, max=25), validators.DataRequired()])
    number = IntegerField('Phone Number *', [validators.DataRequired()])
    alternate_number = IntegerField('Alternate Number')
    email = StringField('Email *', [validators.Length(min=4, max=25),validators.DataRequired()])
    role = SelectField(u'Role',choices = [('Landlord', 'Landlord'), ('Investor', 'Investor'), ('Tenant', 'Tenant'), ('Buyer', 'Buyer'), ('Developer', 'Developer'), ('Seller', 'Seller'), ('Agent', 'Agent'), ('Other', 'Other')])
    nationality = StringField('Nationality', [validators.Length(min=4, max=25)])
    contact_type = SelectField(u'Type of Contact',choices = [('Individual', 'Individual'), ('Company', 'Company')])
    source = SelectField(u'Source',choices = [('Cold Call', 'Cold Call'),('Client Referral','Client Referral'),('Direct Client','Direct Client'), ('Whatsapp', 'Whatsapp'), ('Email', 'Email'), ('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Company Website', 'Company Website'), ('Dubizzle', 'Dubizzle'), ('Google', 'Google'), ('Agent', 'Agent'), ('Bayut', 'Bayut'), ('Property Finder', 'Property Finder'), ('Walk-In', 'Walk-In')])
    assign_to = SelectField(u'Assign To',choices = [])
    gender = SelectField(u'Gender',choices = [('','Select'),('Male', 'Male'),('Female','Female')])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d')
    religion = SelectField(u'Religion',choices = [('','Select'),('Muslims','Muslims'),('Christian','Christian'),('Irreligious/atheist','Irreligious/atheist'),('Hindus','Hindus'),('Buddhists','Buddhists'),('Taoists/Confucianists/Chinese traditional religionists','Taoists/Confucianists/Chinese traditional religionists'),('Ethnic/indigenous','Ethnic/indigenous'),('Sikhism','Sikhism'),('Spiritism','Spiritism'),('Judaism','Judaism'),('Jainism','Jainism')])
    language = SelectField(u'Language',choices = [('','Select'),('Arabic','Arabic'),('English','English'),('Urdu','Urdu'),('Albanian','Albanian'),('Burmese','Burmese'),('Haitian Creole','Haitian Creole'),('Karen','Karen'),('Mandarin','Mandarin'),('Russian','Russian'),('Tigrigna','Tigrigna'),('Amharic','Amharic'),('Cantonese','Cantonese'),('Hebrew','Hebrew'),('Khmer','Khmer'),('Nepali','Nepali'),('Somali','Somali'),('Turkish','Turkish'),('Armenian','Armenian'),('Farsi','Farsi'),('Hindi','Hindi'),('Korean','Korean'),('Polish','Polish'),('Spanish','Spanish'),('Vietnamese','Vietnamese'),('French','French'),('Hmong','Hmong'),('Laotian','Laotian'),('Portuguese','Portuguese'),('Swahili','Swahili'),('Bengali','Bengali'),('German','German'),('Italian','Italian'),('Lithuanian','Lithuanian'),('Punjabi','Punjabi'),('Tagalog','Tagalog'),('Bosnian','Bosnian'),('Greek','Greek'),('Japanese','Japanese'),('Malay','Malay'),('Romanian','Romanian'),('Thai','Thai'),('American Sign Language','American Sign Language'),('British Sign Language','British Sign Language')])
    comment = TextAreaField('Comment', render_kw={"style":"height:200px !important;font-size: 10pt !important;padding-top:10px !important;border-radius:0px !important;"})

class AddLeadForm(FlaskForm):
    contact = StringField('Contact *', [validators.DataRequired(),validators.Length(min=4, max=100)],render_kw={"style":"pointer-events: none;"})
    contact_name = StringField('Name *', [validators.DataRequired(),validators.Length(min=4, max=100)],render_kw={"style":"pointer-events: none;"})
    contact_number =IntegerField('Number *',[validators.DataRequired()],render_kw={"style":"pointer-events: none;"})
    contact_email = StringField('Email *', [validators.DataRequired(),validators.Length(min=4, max=100)],render_kw={"style":"pointer-events: none;"})
    nationality = StringField('Nationality', [validators.Length(min=4, max=100)])
    role = SelectField(u'Role *',[validators.DataRequired()],choices = [('Landlord', 'Landlord'), ('Investor', 'Investor'), ('Tenant', 'Tenant'), ('Buyer', 'Buyer'), ('Developer', 'Developer'), ('Seller', 'Seller'), ('Agent', 'Agent'), ('Other', 'Other')])
    time_to_contact = DateField('Time to contact', format='%Y-%m-%d')
    agent = SelectField(u'Agent',choices = [])
    enquiry_date = DateField('Enquiry Date', format='%Y-%m-%d')
    purpose = SelectField(u'Purpose',choices = [('Live in','Live in'),('Investment','Investment')])
    propertyamenities = MultiCheckboxField('Property Features', choices=features)
    created_by = StringField('Created By')
    status = SelectField(u'Status *',[validators.DataRequired()],choices = [('Open', 'Open'), ('Closed', 'Closed')])
    sub_status = SelectField(u'Sub Status *',[validators.DataRequired()],choices = [])
    property_requirements = StringField('Property',render_kw={"style":"pointer-events: none;"})
    locationtext = SelectField(u'Community',choices = communities)
    building = SelectField(u'Location',choices = [])
    subtype = SelectField(u'Type',choices = [('Villa', 'Villa'), ('Apartment', 'Apartment'),('Loft Apartment', 'Loft Apartment'), ('Residential Floor', 'Residential Floor'), ('Residential Plot', 'Residential Plot'), ('Townhouse', 'Townhouse'), ('Residential Building', 'Residential Building'), ('Penthouse', 'Penthouse'), ('Villa Compound', 'Villa Compound'), ('Hotel Apartment', 'Hotel Apartment'), ('Office', 'Office'), ('Other', 'Other')])
    min_beds = SelectField(u'Beds',choices = [('ST', 'ST'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),('10+', '10+'),(0,'Other')])
    max_beds = SelectField(u'Max Beds',choices = [('', ''),('ST', 'ST'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),('10+', '10+'),(0,'Other')])
    min_price = IntegerField('Price | Budget')
    max_price = IntegerField('Max Price')
    unit = StringField('Unit No *', [validators.DataRequired(),validators.Length(min=4, max=50)])
    plot = StringField('Unit Floor/Plot', [validators.Length(min=4, max=50)])
    street = StringField('Zip Code', [validators.Length(min=4, max=50)])
    size = FloatField('Build Area')
    source = SelectField(u'Source *',[validators.DataRequired()],choices = [('Cold Call', 'Cold Call'), ('Lead Assigned', 'Lead Assigned') ,('Client Referral','Client Referral'), ('TikTok','TikTok') , ('Whatsapp', 'Whatsapp'), ('Email', 'Email'), ('Facebook', 'Facebook'), ('Instagram', 'Instagram'),('Tiktok','Tiktok'), ('Company Website', 'Company Website'), ('Dubizzle', 'Dubizzle'), ('Google', 'Google'), ('Agent', 'Agent'), ('Bayut', 'Bayut'), ('Property Finder', 'Property Finder'), ('Walk-In', 'Walk-In')])

class BuyerLead(AddLeadForm):
    lead_type = SelectField(u'Lead Type',choices = [('Buy','Buy'),('Rent','Rent')])


class DeveloperLead(AddLeadForm):
    lead_type = SelectField(u'Lead Type',choices = [('Buy','Buy')])


class AddDealForm(FlaskForm):
    transaction_type = SelectField(u'Transaction Type',choices = [('Sale', 'Sale'), ('Resale', 'Resale'), ('Leased', 'Leased'), ('Renew Leased', 'Renew Leased'),('Reserved','Reserved'),('Offplan','Off Plan')])
    created_by = StringField('Created By')
    listing_ref = StringField('Listing Ref',render_kw={"style":"pointer-events: none;"})
    lead_ref = StringField('Lead Ref',render_kw={"style":"pointer-events: none;"})
    emi_id = FileField("Emirates ID *",render_kw={'class':'upload'})
    passport = FileField("Passport *",render_kw={'class':'upload'})
    developer_doc = FileField("Developer Document *",render_kw={'class':'upload'})
    emi_id = FileField("Emirates ID *",render_kw={'class':'upload'})
    contact_buyer = StringField('Contact Buyer *', [validators.DataRequired(),validators.Length(min=4, max=100)],render_kw={"style":"pointer-events: none;"})
    contact_buyer_name = StringField('Name Buyer *', [validators.DataRequired(),validators.Length(min=4, max=100)],render_kw={"style":"pointer-events: none;"})
    contact_buyer_number =IntegerField('Number Buyer *',[validators.DataRequired()],render_kw={"style":"pointer-events: none;"})
    contact_buyer_email = StringField('Email Buyer *', [validators.DataRequired(),validators.Length(min=4, max=100)],render_kw={"style":"pointer-events: none;"})
    contact_seller = StringField('Contact Seller *', [validators.DataRequired(),validators.Length(min=4, max=100)],render_kw={"style":"pointer-events: none;"})
    contact_seller_name = StringField('Name Seller *', [validators.DataRequired(),validators.Length(min=4, max=100)],render_kw={"style":"pointer-events: none;"})
    contact_seller_number =IntegerField('Number Seller *',[validators.DataRequired()],render_kw={"style":"pointer-events: none;"})
    contact_seller_email = StringField('Email Seller *', [validators.DataRequired(),validators.Length(min=4, max=100)],render_kw={"style":"pointer-events: none;"})
    source = SelectField(u'Source',choices = [('Cold Call', 'Cold Call'),('Client Referral','Client Referral'),('Direct Client','Direct Client'), ('Whatsapp', 'Whatsapp'), ('Email', 'Email'), ('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Company Website', 'Company Website'), ('Dubizzle', 'Dubizzle'), ('Google', 'Google'), ('Agent', 'Agent'), ('Bayut.com', 'Bayut.com'), ('Property Finder', 'Property Finder'), ('Walk-In', 'Walk-In')])
    status = SelectField(u'Status *',choices = [('Closed', 'Closed'), ('Open', 'Open')])
    sub_status = SelectField(u'Sub Status *', [validators.DataRequired()],choices = [])
    priority = SelectField(u'Priority',choices = [('Normal', 'Normal'), ('Low', 'Low'), ('High', 'High'), ('Urgent', 'Urgent')])
    deal_price = IntegerField('Deal Price *', [validators.DataRequired()])
    deposit = IntegerField('Deposit *', [validators.DataRequired()])
    agency_fee_seller = IntegerField('Agency Fee Seller')
    agency_fee_buyer = IntegerField('Agency Fee Buyer')
    gross_commission = IntegerField('Gross Commission *', [validators.DataRequired()])
    include_vat = SelectField(u'Include VAT',choices = [('yes', 'Yes'), ('no', 'No')])
    total_commission = IntegerField('Total Commission')
    split_with_external_referral = SelectField(u'Split with Externl Referral',choices = [('yes', 'Yes'), ('no', 'No')])
    agent_1 = SelectField(u'Sales Agent *', [validators.DataRequired()],choices = [])
    commission_agent_1 = StringField('Commission')
    agent_2 = SelectField(u'Listing Agent',choices = [])
    commission_agent_2 = StringField('Commission')
    
    estimated_deal_date = DateField('Estimated Deal Date')
    actual_deal_date = DateField('Actual Deal Date *',[validators.DataRequired()])
    unit_no = StringField('Unit No *',[validators.DataRequired()])
    unit_category = SelectField(u'Type *',[validators.DataRequired()],choices = [('Villa', 'Villa'), ('Apartment', 'Apartment'),('Loft Apartment', 'Loft Apartment'), ('Residential Floor', 'Residential Floor'), ('Residential Plot', 'Residential Plot'), ('Townhouse', 'Townhouse'), ('Residential Building', 'Residential Building'), ('Penthouse', 'Penthouse'), ('Villa Compound', 'Villa Compound'), ('Hotel Apartment', 'Hotel Apartment'), ('Office', 'Office'), ('Other', 'Other')])
    unit_beds = StringField('Unit Beds *',[validators.DataRequired()])
    unit_location = SelectField(u'Community *',[validators.DataRequired()],choices = communities)
    unit_sub_location = SelectField(u'Location *',[validators.DataRequired()],choices = [])
    unit_floor = StringField('Unit Floor/Plot')
    unit_type = StringField('Unit Type')


    buyer_type = SelectField(u'Buyer Type',choices = [('Investor','Investor'),('End User','End User')])
    
    
    
    tenancy_start_date = StringField('Tenancy Start Date')
    tenancy_renewal_date = StringField('Tenancy Renewal Date')
    cheques = SelectField(u'Cheques',choices = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')])

    
    #justadded
    #just for buy
    finance_type = SelectField(u'Finance Type *',[validators.DataRequired()],choices = [('Cash','Cash'),('Mortgage','Mortgage')])
    down_payment_available = SelectField(u'Down Payment Available *',[validators.DataRequired()],choices = [('Yes','Yes'),('No','No')])
    down_payment = IntegerField('Down Payment amount')
    #
    client_referred_bank = StringField('Client Referred Bank', [validators.Length(min=4, max=50)])
    bank_representative_name = StringField('Bank Representative Name', [validators.Length(min=4, max=50)])
    bank_representative_mobile = StringField('Bank Representative Mobile', [validators.Length(min=4, max=50)])
    referral_date = DateField('Date of Referral', format='%Y-%m-%d')

    #rent
    number_cheque_payment = SelectField(u'Number of cheque payment',choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')])
    cheque_payment_type = SelectField(u'Cheque payment type',choices = [('Self','Self'),('Company','Company')])
    move_in_date = DateField('Move in Date', format='%Y-%m-%d')
    


    #developer
    plot_size = FloatField('Plot Size')
    floor_no = StringField('Floor No', [validators.Length(min=4, max=50)])
    project = StringField('Project', [validators.Length(min=4, max=50)])
    unit_price = IntegerField('Unit Price')
    percentage = IntegerField('Percentage')
    amount = IntegerField('Amount')
    pre_approval_loan = SelectField(u'Pre Approval Available *',[validators.DataRequired()],choices = [('Yes','Yes'),('No','No')])
    loan_amount = IntegerField('Loan amount *', [validators.DataRequired()])


class AddFile(FlaskForm):
    files = MultipleFileField('File(s) Upload', [validators.DataRequired()])
    password = StringField('Encrypt Password', [validators.DataRequired(),validators.Length(min=4, max=50)])
    send = SelectField(u'Send To', [validators.DataRequired()],choices = [])

class AddEmployeeForm(FlaskForm):
    Status = SelectField(u'Status',choices = [('Active', 'Active'), ('Cancel', 'Cancel')])
    Employee_Status = StringField('Employee Status')
    Employee_ID = StringField('Employee ID')
    Name = StringField('Name')
    Position = StringField('Position')
    Nationality = StringField('Nationality')
    UID = StringField('UID')
    Date_of_Birth = DateField('Date of Birth', format='%Y-%m-%d')
    Date_of_Joining = DateField('Date of Joining', format='%Y-%m-%d')
    Emirates_ID = StringField('Emirates ID')
    Card_No = StringField('Card No')
    Emirates_Card_Expiry = DateField('Emirates Card Expiry', format='%Y-%m-%d')
    Mobile_No = StringField('Mobile No')
    MOL_Personal_No = StringField('MOL Personal No')
    Labor_Card_No = StringField('Labor Card No')
    Labor_Card_Expiry = DateField('Labor Card Expiry', format='%Y-%m-%d')
    Insurance_No = StringField('Insurance No')
    Insurance_Effective_Date = DateField('Insurance Effective Date', format='%Y-%m-%d')
    Insurance_Expiry_Date = DateField('Insurance Expiry Date', format='%Y-%m-%d')
    Date_of_Submission = DateField('Date of Submission', format='%Y-%m-%d')
    Residence_Expiry = DateField('Residence Expiry', format='%Y-%m-%d')
    Remarks = StringField('Remarks')