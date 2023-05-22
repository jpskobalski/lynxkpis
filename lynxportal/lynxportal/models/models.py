# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LynxHistorical(models.Model):
    op_finalweight = models.FloatField(db_column='OP_FinalWeight', blank=True, null=True)
    op_stagename = models.CharField(db_column='OP_StageName', max_length=8192, db_collation='binary', blank=True, null=True)
    timestamp = models.DateField(db_column='TimeStamp', blank=True, null=True)
    op_id = models.CharField(db_column='OP_Id', max_length=8192, db_collation='binary', blank=True, null=True)
    op_isdeleted = models.BooleanField(db_column='OP_IsDeleted', blank=True, null=True)
    op_accountid = models.CharField(db_column='OP_AccountId', max_length=8192, db_collation='binary', blank=True, null=True)
    op_recordtypeid = models.CharField(db_column='OP_RecordTypeId', max_length=8192, db_collation='binary', blank=True, null=True)
    op_name = models.CharField(db_column='OP_Name', max_length=8192, db_collation='binary', blank=True, null=True)
    op_amount = models.FloatField(db_column='OP_Amount', blank=True, null=True)
    op_probability = models.FloatField(db_column='OP_Probability', blank=True, null=True)
    op_expectedrevenue = models.FloatField(db_column='OP_ExpectedRevenue', blank=True, null=True)
    op_weightedvalue = models.FloatField(db_column='OP_WeightedValue', blank=True, null=True)
    op_totalopportunityquantity = models.FloatField(db_column='OP_TotalOpportunityQuantity', blank=True, null=True)
    op_closedate = models.DateField(db_column='OP_CloseDate', blank=True, null=True)
    op_type = models.CharField(db_column='OP_Type', max_length=8192, db_collation='binary', blank=True, null=True)
    op_nextstep = models.CharField(db_column='OP_NextStep', max_length=8192, db_collation='binary', blank=True, null=True)
    op_leadsource = models.CharField(db_column='OP_LeadSource', max_length=8192, db_collation='binary', blank=True, null=True)
    op_isclosed = models.BooleanField(db_column='OP_IsClosed', blank=True, null=True)
    op_iswon = models.BooleanField(db_column='OP_IsWon', blank=True, null=True)
    op_forecastcategory = models.CharField(db_column='OP_ForecastCategory', max_length=8192, db_collation='binary', blank=True, null=True)
    op_forecastcategoryname = models.CharField(db_column='OP_ForecastCategoryName', max_length=8192, db_collation='binary', blank=True, null=True)
    op_hasopportunitylineitem = models.BooleanField(db_column='OP_HasOpportunityLineItem', blank=True, null=True)
    op_pricebook2id = models.CharField(db_column='OP_Pricebook2Id', max_length=8192, db_collation='binary', blank=True, null=True)
    op_ownerid = models.CharField(db_column='OP_OwnerId', max_length=8192, db_collation='binary', blank=True, null=True)
    op_createddate = models.TextField(db_column='OP_CreatedDate', blank=True, null=True)  # This field type is a guess.
    op_createdbyid = models.CharField(db_column='OP_CreatedById', max_length=8192, db_collation='binary', blank=True, null=True)
    op_lastmodifieddate = models.TextField(db_column='OP_LastModifiedDate', blank=True, null=True)  # This field type is a guess.
    op_lastmodifiedbyid = models.CharField(db_column='OP_LastModifiedById', max_length=8192, db_collation='binary', blank=True, null=True)
    op_systemmodstamp = models.TextField(db_column='OP_SystemModstamp', blank=True, null=True)  # This field type is a guess.
    op_lastactivitydate = models.DateField(db_column='OP_LastActivityDate', blank=True, null=True)
    op_pushcount = models.BigIntegerField(db_column='OP_PushCount', blank=True, null=True)
    op_laststagechangedate = models.TextField(db_column='OP_LastStageChangeDate', blank=True, null=True)  # This field type is a guess.
    op_fiscalquarter = models.BigIntegerField(db_column='OP_FiscalQuarter', blank=True, null=True)
    op_fiscalyear = models.BigIntegerField(db_column='OP_FiscalYear', blank=True, null=True)
    op_fiscal = models.CharField(db_column='OP_Fiscal', max_length=8192, db_collation='binary', blank=True, null=True)
    op_contactid = models.CharField(db_column='OP_ContactId', max_length=8192, db_collation='binary', blank=True, null=True)
    op_lastvieweddate = models.TextField(db_column='OP_LastViewedDate', blank=True, null=True)  # This field type is a guess.
    op_lastreferenceddate = models.TextField(db_column='OP_LastReferencedDate', blank=True, null=True)  # This field type is a guess.
    op_hasopenactivity = models.BooleanField(db_column='OP_HasOpenActivity', blank=True, null=True)
    op_hasoverduetask = models.BooleanField(db_column='OP_HasOverdueTask', blank=True, null=True)
    op_lastamountchangedhistoryid = models.CharField(db_column='OP_LastAmountChangedHistoryId', max_length=8192, db_collation='binary', blank=True, null=True)
    op_lastclosedatechangedhistoryid = models.CharField(db_column='OP_LastCloseDateChangedHistoryId', max_length=8192, db_collation='binary', blank=True, null=True)
    op_distributor_field = models.CharField(db_column='OP_Distributor_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_opportunity_description_field = models.CharField(db_column='OP_Opportunity_Description_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_project_field = models.CharField(db_column='OP_Project_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_push_out_date_field = models.DateField(db_column='OP_Push_out_date_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    opontains_ode_product_field = models.BooleanField(db_column='OPontains_ODE_product_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    op_mgr_commit_field = models.BooleanField(db_column='OP_MGR_Commit_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    op_licenseonfiguration_approved_field = models.BooleanField(db_column='OP_Licenseonfiguration_approved_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    op_does_oppty_include_licensed_product_field = models.CharField(db_column='OP_Does_Oppty_include_licensed_product_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_po_number_field = models.CharField(db_column='OP_PO_Number_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_serial_number_field = models.CharField(db_column='OP_Serial_Number_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_so_number_field = models.CharField(db_column='OP_SO_Number_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_invoice_number_field = models.CharField(db_column='OP_Invoice_Number_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_sales_tax_field = models.CharField(db_column='OP_Sales_Tax_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_freight_term_field = models.CharField(db_column='OP_Freight_Term_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_method_of_shipment_field = models.CharField(db_column='OP_Method_of_Shipment_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_freight_charge_field = models.CharField(db_column='OP_Freight_Charge_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_reason_on_hold_or_lost_field = models.CharField(db_column='OP_Reason_on_hold_or_lost_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_product_gap_detail_field = models.CharField(db_column='OP_Product_Gap_Detail_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_oppo_ship_to_field = models.CharField(db_column='OP_Oppo_Ship_to_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_upgrade_contact_name_field = models.CharField(db_column='OP_Upgrade_Contact_Name_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_upgrade_contact_email_address_field = models.CharField(db_column='OP_Upgrade_Contact_email_address_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_support_renewal_field = models.BooleanField(db_column='OP_Support_Renewal_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    op_product_gap_yes_field = models.BooleanField(db_column='OP_Product_Gap_Yes_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    op_follow_up_date_field = models.DateField(db_column='OP_Follow_up_Date_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    op_award_date_field = models.DateField(db_column='OP_Award_Date_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_id = models.CharField(db_column='PR_Id', max_length=8192, db_collation='binary', blank=True, null=True)
    pr_ownerid = models.CharField(db_column='PR_OwnerId', max_length=8192, db_collation='binary', blank=True, null=True)
    pr_isdeleted = models.BooleanField(db_column='PR_IsDeleted', blank=True, null=True)
    pr_name = models.CharField(db_column='PR_Name', max_length=8192, db_collation='binary', blank=True, null=True)
    pr_recordtypeid = models.CharField(db_column='PR_RecordTypeId', max_length=8192, db_collation='binary', blank=True, null=True)
    pr_createddate = models.TextField(db_column='PR_CreatedDate', blank=True, null=True)  # This field type is a guess.
    pr_createdbyid = models.CharField(db_column='PR_CreatedById', max_length=8192, db_collation='binary', blank=True, null=True)
    pr_lastmodifieddate = models.TextField(db_column='PR_LastModifiedDate', blank=True, null=True)  # This field type is a guess.
    pr_lastmodifiedbyid = models.CharField(db_column='PR_LastModifiedById', max_length=8192, db_collation='binary', blank=True, null=True)
    pr_systemmodstamp = models.TextField(db_column='PR_SystemModstamp', blank=True, null=True)  # This field type is a guess.
    pr_lastactivitydate = models.DateField(db_column='PR_LastActivityDate', blank=True, null=True)
    pr_lastvieweddate = models.TextField(db_column='PR_LastViewedDate', blank=True, null=True)  # This field type is a guess.
    pr_lastreferenceddate = models.TextField(db_column='PR_LastReferencedDate', blank=True, null=True)  # This field type is a guess.
    pr_follow_up_date_field = models.DateField(db_column='PR_Follow_up_Date_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_campaign_field = models.CharField(db_column='PR_Campaign_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_lynuxworks_strengths_field = models.CharField(db_column='PR_LynuxWorks_Strengths_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_lynuxworks_weaknesses_field = models.CharField(db_column='PR_LynuxWorks_Weaknesses_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_design_win_type_field = models.CharField(db_column='PR_Design_Win_Type_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_exec_advocate_field = models.CharField(db_column='PR_Exec_Advocate_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_submit_license_info_for_approval_field = models.BooleanField(db_column='PR_Submit_License_Info_for_Approval_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_does_project_include_licensed_product_field = models.CharField(db_column='PR_Does_Project_Include_Licensed_Product_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_license_configuration_approved_field = models.BooleanField(db_column='PR_License_Configuration_Approved_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_lead_source_field = models.CharField(db_column='PR_Lead_Source_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_compelling_event_s_field = models.CharField(db_column='PR_Compelling_Event_s_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_application_type_field = models.CharField(db_column='PR_Application_Type_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_decision_criteria_field = models.CharField(db_column='PR_Decision_Criteria_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_design_win_field = models.BooleanField(db_column='PR_Design_Win_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_design_win_date_field = models.DateField(db_column='PR_Design_Win_Date_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_development_host_field = models.CharField(db_column='PR_Development_Host_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_distributor_field = models.CharField(db_column='PR_Distributor_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_government_agency_field = models.CharField(db_column='PR_Government_Agency_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_government_program_name_field = models.CharField(db_column='PR_Government_Program_Name_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_if_this_is_sub_who_is_prime_field = models.CharField(db_column='PR_If_This_Is_Sub_Who_Is_Prime_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_include_in_top_projects_report_field = models.BooleanField(db_column='PR_Include_In_Top_Projects_Report_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_last_updated_on_field = models.DateField(db_column='PR_Last_Updated_On_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    prontains_ode_product_field = models.BooleanField(db_column='PRontains_ODE_Product_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_lifetime_total_forecast_conservative_field = models.FloatField(db_column='PR_Lifetime_Total_Forecast_Conservative_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_lifetime_total_forecast_optimistic_field = models.FloatField(db_column='PR_Lifetime_Total_Forecast_Optimistic_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_reason_lost_field = models.CharField(db_column='PR_Reason_Lost_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_meets_design_win_criteria_field = models.BooleanField(db_column='PR_Meets_Design_Win_Criteria_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_dev_tool_host_license_field = models.CharField(db_column='PR_Dev_Tool_Host_License_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_development_tool_license_model_field = models.CharField(db_column='PR_Development_Tool_License_Model_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_war_room_priority_field = models.CharField(db_column='PR_War_Room_Priority_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_processor_s_under_consideration_field = models.CharField(db_column='PR_Processor_s_Under_Consideration_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_project_stage_field = models.CharField(db_column='PR_Project_Stage_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_project_type_field = models.CharField(db_column='PR_Project_Type_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_run_time_status_field = models.CharField(db_column='PR_Run_Time_Status_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_specific_processor_type_field = models.CharField(db_column='PR_Specific_Processor_Type_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_support_status_field = models.CharField(db_column='PR_Support_Status_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_target_boards_under_consideration_field = models.CharField(db_column='PR_Target_Boards_Under_Consideration_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_os_of_interest_field = models.CharField(db_column='PR_OS_of_Interest_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_tools_requirements_field = models.CharField(db_column='PR_Tools_Requirements_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_account_field = models.CharField(db_column='PR_Account_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_dev_tool_rtos_processor_architecture_field = models.CharField(db_column='PR_Dev_Tool_RTOS_Processor_Architecture_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_development_tool_user_license_type_field = models.CharField(db_column='PR_Development_Tool_User_License_Type_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_rtos_dev_deploy_lic_project_description_field = models.CharField(db_column='PR_RTOS_Dev_Deploy_Lic_Project_Description_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_rtos_dev_deploy_license_site_description_field = models.CharField(db_column='PR_RTOS_Dev_Deploy_License_Site_Description_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_market_segment_field = models.CharField(db_column='PR_Market_segment_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_rtos_deployment_license_type_field = models.CharField(db_column='PR_RTOS_Deployment_License_Type_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_meets_oderiteria_field = models.BooleanField(db_column='PR_meets_oderiteria_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_program_field = models.CharField(db_column='PR_Program_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_graphic_hardware_field = models.CharField(db_column='PR_Graphic_Hardware_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_graphics_software_requirements_field = models.CharField(db_column='PR_Graphics_Software_Requirements_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_graphics_software_details_field = models.CharField(db_column='PR_Graphics_Software_Details_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_other_tools_requirements_field = models.CharField(db_column='PR_Other_Tools_Requirements_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_project_license_size_field = models.CharField(db_column='PR_Project_License_Size_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_lost_on_hold_reason_field = models.CharField(db_column='PR_Lost_On_Hold_Reason_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_competitor_field = models.CharField(db_column='PR_Competitor_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_development_tool_site_restriction_field = models.CharField(db_column='PR_Development_Tool_Site_Restriction_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_product_licensing_field = models.CharField(db_column='PR_Product_Licensing_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_x3rd_party_tools_requirements_field = models.CharField(db_column='PR_X3rd_Party_Tools_Requirements_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_special_license_terms_attach_license_field = models.BooleanField(db_column='PR_Special_License_Terms_attach_license_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_id = models.CharField(db_column='AC_Id', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_isdeleted = models.BooleanField(db_column='AC_IsDeleted', blank=True, null=True)
    ac_masterrecordid = models.CharField(db_column='AC_MasterRecordId', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_name = models.CharField(db_column='AC_Name', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_type = models.CharField(db_column='AC_Type', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_recordtypeid = models.CharField(db_column='AC_RecordTypeId', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_parentid = models.CharField(db_column='AC_ParentId', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_billingstreet = models.CharField(db_column='AC_BillingStreet', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_billingcity = models.CharField(db_column='AC_BillingCity', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_billingstate = models.CharField(db_column='AC_BillingState', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_billingpostalcode = models.CharField(db_column='AC_BillingPostalCode', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_billingcountry = models.CharField(db_column='AC_BillingCountry', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_billinglatitude = models.FloatField(db_column='AC_BillingLatitude', blank=True, null=True)
    ac_billinglongitude = models.FloatField(db_column='AC_BillingLongitude', blank=True, null=True)
    ac_billinggeocodeaccuracy = models.CharField(db_column='AC_BillingGeocodeAccuracy', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shippingstreet = models.CharField(db_column='AC_ShippingStreet', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shippingcity = models.CharField(db_column='AC_ShippingCity', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shippingstate = models.CharField(db_column='AC_ShippingState', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shippingpostalcode = models.CharField(db_column='AC_ShippingPostalCode', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shippingcountry = models.CharField(db_column='AC_ShippingCountry', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shippinglatitude = models.FloatField(db_column='AC_ShippingLatitude', blank=True, null=True)
    ac_shippinglongitude = models.FloatField(db_column='AC_ShippingLongitude', blank=True, null=True)
    ac_shippinggeocodeaccuracy = models.CharField(db_column='AC_ShippingGeocodeAccuracy', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_phone = models.CharField(db_column='AC_Phone', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_fax = models.CharField(db_column='AC_Fax', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_accountnumber = models.CharField(db_column='AC_AccountNumber', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_website = models.CharField(db_column='AC_Website', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_photourl = models.CharField(db_column='AC_PhotoUrl', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_sic = models.CharField(db_column='AC_Sic', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_industry = models.CharField(db_column='AC_Industry', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_annualrevenue = models.FloatField(db_column='AC_AnnualRevenue', blank=True, null=True)
    ac_numberofemployees = models.BigIntegerField(db_column='AC_NumberOfEmployees', blank=True, null=True)
    ac_ownership = models.CharField(db_column='AC_Ownership', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_tickersymbol = models.CharField(db_column='AC_TickerSymbol', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_rating = models.CharField(db_column='AC_Rating', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_site = models.CharField(db_column='AC_Site', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_ownerid = models.CharField(db_column='AC_OwnerId', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_createddate = models.TextField(db_column='AC_CreatedDate', blank=True, null=True)  # This field type is a guess.
    ac_createdbyid = models.CharField(db_column='AC_CreatedById', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_lastmodifieddate = models.TextField(db_column='AC_LastModifiedDate', blank=True, null=True)  # This field type is a guess.
    ac_lastmodifiedbyid = models.CharField(db_column='AC_LastModifiedById', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_systemmodstamp = models.TextField(db_column='AC_SystemModstamp', blank=True, null=True)  # This field type is a guess.
    ac_lastactivitydate = models.DateField(db_column='AC_LastActivityDate', blank=True, null=True)
    ac_lastvieweddate = models.TextField(db_column='AC_LastViewedDate', blank=True, null=True)  # This field type is a guess.
    ac_lastreferenceddate = models.TextField(db_column='AC_LastReferencedDate', blank=True, null=True)  # This field type is a guess.
    ac_jigsaw = models.CharField(db_column='AC_Jigsaw', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_jigsawcompanyid = models.CharField(db_column='AC_JigsawCompanyId', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_accountsource = models.CharField(db_column='AC_AccountSource', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_sicdesc = models.CharField(db_column='AC_SicDesc', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shipping_phone_field = models.CharField(db_column='AC_Shipping_Phone_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_shipping_fax_field = models.CharField(db_column='AC_Shipping_Fax_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_sales_team_field = models.CharField(db_column='AC_Sales_Team_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_duns_field = models.CharField(db_column='AC_DUNS_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_focus_or_general_field = models.CharField(db_column='AC_Focus_or_General_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_project_lynxos_field = models.BooleanField(db_column='AC_Project_LynxOS_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_strategic_strengths_field = models.CharField(db_column='AC_Strategic_Strengths_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_critical_vulnerability_field = models.CharField(db_column='AC_Critical_Vulnerability_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_goals_field = models.CharField(db_column='AC_Goals_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_account_field = models.CharField(db_column='AC_Account_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_bonus_eligible_field = models.BooleanField(db_column='AC_Bonus_Eligible_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_account_type_field = models.CharField(db_column='AC_Account_Type_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_project_lynxsecure_field = models.BooleanField(db_column='AC_Project_LynxSecure_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_project_lynxos_178_field = models.BooleanField(db_column='AC_Project_LynxOS_178_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_project_lynxos_se_field = models.BooleanField(db_column='AC_Project_LynxOS_SE_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_safety_attack_plan_field = models.BooleanField(db_column='AC_Safety_Attack_Plan_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_project_bluecat_field = models.BooleanField(db_column='AC_Project_BlueCat_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_follow_up_date_field = models.DateField(db_column='AC_Follow_up_Date_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_region_field = models.CharField(db_column='AC_Region_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_validedge_field = models.BooleanField(db_column='AC_ValidEdge_',  blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_past_owner_field = models.CharField(db_column='AC_Past_Owner_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_business_unit_field = models.CharField(db_column='AC_Business_Unit_',  max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_opportunity_owner = models.CharField(db_column='OP_Opportunity_Owner', max_length=8192, db_collation='binary', blank=True, null=True)
    ac_account_owner = models.CharField(db_column='AC_Account_Owner', max_length=8192, db_collation='binary', blank=True, null=True)
    op_pgopwin = models.FloatField(db_column='OP_PGoPWin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LYNX_HISTORICAL'
