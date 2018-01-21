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

# capture journal
TAC_Journal_Capture_TIN = 'creg01Tin_source'
# TAC_Journal_Capture_Journal_Category = 'entity_ctac01JournalCategory'
TAC_Journal_Capture_Journal_Type = 'entity_ctac01JournalType'
# TAC_Journal_Capture_Journal_Reason_Type = 'entity_ctac01JournalReasonType'
TAC_Journal_Capture_Submission_Source = 'entity_ctac01ReceivingChannel'
TAC_Journal_Capture_Request_by = 'entity_ctac01JournalSource'
TAC_Journal_Capture_Requestor = 'entity_ctac01CompletedBy'
TAC_Journal_Capture_Journal_Description = 'entity_ctac01JournalDescription'
