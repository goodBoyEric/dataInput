# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2018/1/19

# search element
TAC_Journal_Search_TIN = 'creg01Tin'
TAC_Journal_Search_Journal_Number = 'ctac01JournalNumber'
TAC_Journal_Search_Journal_Category = 'ctac01JournalCategory'
TAC_Journal_Search_Journal_Type = 'ctac01JournalType'
TAC_Journal_Search_Journal_Status = 'ctac01JournalStatus'
TAC_Journal_Search_Submission_Source = 'ctac01ReceivingChannel'
TAC_Journal_Search_Request_by = 'ctac01JournalSource'

# search button
TAC_Journal_Search_Search_button = 'btnSearch'
TAC_Journal_Search_New_button = 'btnAddNew'
TAC_Journal_Search_Process_button = 'btnProcess'
TAC_Journal_Search_Reallocation_of_Receipt_CSS = """ul#journalCategories a[onclick="newJournal('RORJ')"]"""
TAC_Journal_Search_Miscellaneous_Adjustment_CSS = """ul#journalCategories a[onclick="newJournal('MAJ')"]"""
TAC_Journal_Search_Transfer_CSS = """ul#journalCategories a[onclick="newJournal('TJ')"]"""
TAC_Journal_Search_Write_off_CSS = """ul#journalCategories a[onclick="newJournal('WOJ')"]"""

# search data --- first line&line data
TAC_Journal_Search_Table_First_Line = 'table#gridview>tbody>tr:nth-child(1)'

# capture journal common element
TAC_Journal_Capture_TIN = 'creg01Tin_source'
# TAC_Journal_Capture_Journal_Category = 'entity_ctac01JournalCategory'
TAC_Journal_Capture_Journal_Type = 'entity_ctac01JournalType'
# TAC_Journal_Capture_Journal_Reason_Type = 'entity_ctac01JournalReasonType'
TAC_Journal_Capture_Submission_Source = 'entity_ctac01ReceivingChannel'
TAC_Journal_Capture_Request_by = 'entity_ctac01JournalSource'
TAC_Journal_Capture_Requestor = 'entity_ctac01CompletedBy'
TAC_Journal_Capture_Journal_Description = 'entity_ctac01JournalDescription'
TAC_Journal_Capture_Submit_button = 'btnSubmit'
TAC_Journal_Capture_Approve_button = 'btnApprove'
TAC_Journal_Capture_Approve_Yes_button_CSS = 'button.btn.btn-primary.save.ax-save'

TAC_Journal_Capture_Reject_button = 'btnReject'
TAC_Journal_Capture_SendBack_button = 'btnReturn'
TAC_Journal_Capture_Complete_button = 'btnComplete'


# button
TAC_Journal_Capture_Add_button = 'btnSubAdd_ttac02JournalTransaction'
TAC_Journal_Capture_AR_Search_button = 'btnSearchTACTransaction'
TAC_Journal_Capture_AR_Add_to_Journal_button = 'btnAddToJournal'


# capture adjust receipt
TAC_Journal_Capture_AR_Doc_No_Text = 'q_ctac03DocumentNum'
TAC_Journal_Capture_AR_Table_Data_CSS = 'table#TACTransactionGrid_ARDR>tbody>tr:nth-child(1)>td:nth-child(7)'
TAC_Journal_Capture_AR_Target_Issue_Date = 'entity_targetIssueDate'
TAC_Journal_Capture_attachments = """table#attachmentview>tbody td>input[type="checkbox"]"""

# capture Adjust Brought Forwardx Balance
TAC_Journal_Capture_BF_Tax_Type = 'entity_cret09TaxtypeUid'
TAC_Journal_Capture_BF_Liability_Type = 'entity_ctac02LiabilityType'
TAC_Journal_Capture_BF_Tax_Year = 'entity_ctac02TaxYear'
TAC_Journal_Capture_BF_Tax_Period = 'entity_ctac02TaxPeriod'
TAC_Journal_Capture_BF_Amount = 'entity_ctac02Amount'
# button
TAC_Journal_Capture_BF_Add_button = 'btnSubAdd_ttac02JournalTransaction'

# Capture Reverse Adhoc Transaction
TAC_Journal_Capture_RT_Doc_No_Yes = 'isChoose0'
TAC_Journal_Capture_RT_Doc_No_NO = 'isChoose1'
TAC_Journal_Capture_RT_Doc_No = 'q_ctac03DocumentNum'
TAC_Journal_Capture_RT_Search_button = 'btnSearchTACTransaction'
TAC_Journal_Capture_RT_CheckAll_CSS = """table#TACTransactionGrid input[name="ChkAll"]"""
TAC_Journal_Capture_RT_AddtoJournal_button='btnAddToJournal'

# # Capture Adjust Receipt Amount
TAC_Journal_Capture_ARA_Tax_Type = 'q_cret09TaxtypeUid'
TAC_Journal_Capture_ARA_Liability_Type = 'q_ctac03LiabilityType'
TAC_Journal_Capture_ARA_Tax_Year = 'q_ctac03TaxYear'
TAC_Journal_Capture_ARA_Table_Data_CSS = 'table#TACTransactionGrid>tbody>tr:nth-child(1)>td:nth-child('
TAC_Journal_Capture_ARA_Table_Data_Amount = 'input_reviseAmount_0'


# send back
TAC_Journal_Input_Text= 'textarea.txt'

# reject journal

# write off journal
TAC_Journal_Capture_Write_Off_Authorization_Number = 'entity_ctac01AuthorizationNumber'
TAC_Journal_Capture_Write_Off_Type = 'entity_ctac01JournalType'
TAC_Journal_Capture_Write_Off_Reason = 'entity_ctac01JournalReasonType'
