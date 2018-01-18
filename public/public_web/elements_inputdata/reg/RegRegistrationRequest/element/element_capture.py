# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2017/10/9 0009

# # Registration Request----Capture Screen Element # #
Capture_Submission_Source = 'entity_SubmitSource'
Taxpayer_Category = 'entity_TaxpayerCategory'

Taxpayer_Type_input = 'entity_TaxpayerType_chosen'
Taxpayer_Type_CSS = 'div#entity_TaxpayerType_chosen>div>ul>li:nth-child('

Magisterial_District_input = 'entity_MagisterialDistrict_chosen'
Magisterial_District_CSS = 'div#entity_MagisterialDistrict_chosen>div>ul>li:nth-child(2)'

Activity_Sector = 'entity_MainTaxableActivity_Category'

Source_of_Income_input = 'entity_MainTaxableActivity_chosen'
Source_of_Income_CSS = 'div#entity_MainTaxableActivity_chosen>div>ul>li:nth-child(2)'

Primary_Telephone_first = 'creg01PrimaryTelephoneSecond'
Primary_Telephone_second = 'creg01PrimaryTelephoneLast'
Cellphone = 'creg01MobilePhoneSecond'
Email_Address = 'entity_Email'
Other_Telephone_first = 'creg01OtherTelephoneSecond'
Other_Telephone_second = 'creg01OtherTelephoneLast'
Fax_Fax2Email_first = 'creg01FaxSecond'
Fax_Fax2Email_second = 'creg01FaxLast'

# Postal_Address
Postal_Address_OpenButton = 'poparea1'
Postal_Address_first = 'addressLine3'
Postal_Address_second = 'addressLine3Number'
Postal_Suburb_Area = 'addressLine2'
Postal_City_Town = 'city'
Postal_Address_SaveButton_CSS = '.popover-content>button:nth-child(2)'  # Save button

# Residential/Business Address
Residential_Business_Address_OpenButton = 'poparea2'
Address_Line = 'addressLine1'
Residential_Suburb_Area = 'addressLine2'
Residential_City_Town = 'city'
Residential_Business_Address_SaveButton = '.popover-content>button:nth-child(2)'    # Save button

# Taxpayer_Category:Individual
First_Names = 'entity_FirstName'
Surname = 'entity_LastName'
Gender_Male = 'entity_Sex0'
Gender_Female = 'entity_Sex1'
Date_of_Birth = 'entity_BirthDate'
ID_Type = 'entity_IDType'
ID_Number = 'entity_IDNo'
# Residency = ''
Marital_Status_input = 'entity_MaritalStatus_chosen'
Marital_Status_CSS = 'div#entity_MaritalStatus_chosen>div>ul>li:nth-child(2)'
# Diplomat
Embassy_or_Consular_Miss = 'entitycreg01OrganizationTin'
# Individual for Farmer and Business&Individual for Business
Registered_Trade_Name = 'entity_02TradeName'

# bank account
bank_account_tab_CSS = 'li#lifrmTab2>a'
Bank_account_NewButton = 'btnAccountAdd'
Name_of_Bank = 'accounts[0].creg04BankName'
Branch_Name = 'accounts[0].creg04BranchName'
Type_of_Account = 'accounts[0].creg04AccountType'
Account_Number = 'accounts[0].creg04AccountNo'

# Tax Type
tax_type_tab_CSS = 'ul#editFrmTab>li:nth-child(6)>a'
Effective_Date ="""registeredTaxType[0].creg06EffectiveDate"""
VAT_Checkbox_CSS = 'table#taxtypeview>tbody>tr:nth-child(4)>td:nth-child(1)>input'
VAT_Effective_Date = """registeredTaxType[1].creg06EffectiveDate"""
VAT_Details_button = 'registeredTaxType[1].creg06TaxTypeDetail'
VAT_Estimated_Annual_Taxable_Supplies = 'supplies'
VAT_Details_Screen_Yes_button = 'button.btn.btn-primary.save.ax-save'


# Other Source of Income
Other_Source_of_Income_tab = 'liIndSecondActivity'
Other_Source_of_Income_NewButton = 'btnActivityAdd'
IN_Activity_Sector = 'taxableActivities[0].creg29ActivityCategory'
IN_Source_of_Income = 'taxableActivities[0].creg29ActivityCode'
Active_Inactive = 'taxableActivities[0].creg29ActivityStatus'

# Representatives
Representatives_NewButton = 'btnRepresentativeAdd'
Representative_Type = 'representatives[0].creg31RepresentativeType'
Representative_TIN = 'representatives[0].creg31Tin'

# attachment
registration_request_search_capture_attachments = 'table#attachmentview>tbody td>input[type="checkbox"]'

# tax type 日期
income_tax_effective_date = '01-03-2018'
vat_tax_effective_date = '01-03-2017'

# submit
capture_submit_button = 'btnSubmit'
capture_yes_button_CSS = 'button.btn.btn-primary.ax-yes'

