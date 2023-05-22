# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LynxHistorical(models.Model):
    op_finalweight = models.FloatField(blank=True, null=True)
    op_stagename = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    op_id = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_isdeleted = models.BooleanField(blank=True, null=True)
    op_accountid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_recordtypeid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_name = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_amount = models.FloatField(blank=True, null=True)
    op_probability = models.FloatField(blank=True, null=True)
    op_expectedrevenue = models.FloatField(blank=True, null=True)
    op_weightedvalue = models.FloatField(blank=True, null=True)
    op_totalopportunityquantity = models.FloatField(blank=True, null=True)
    op_closedate = models.DateField(blank=True, null=True)
    op_type = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_nextstep = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_leadsource = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_isclosed = models.BooleanField(blank=True, null=True)
    op_iswon = models.BooleanField(blank=True, null=True)
    op_forecastcategory = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_forecastcategoryname = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_hasopportunitylineitem = models.BooleanField(blank=True, null=True)
    op_pricebook2id = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_ownerid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_createddate = models.TextField(blank=True, null=True)  # This field type is a guess.
    op_createdbyid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_lastmodifieddate = models.TextField(blank=True, null=True)  # This field type is a guess.
    op_lastmodifiedbyid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_systemmodstamp = models.TextField(blank=True, null=True)  # This field type is a guess.
    op_lastactivitydate = models.DateField(blank=True, null=True)
    op_pushcount = models.BigIntegerField(blank=True, null=True)
    op_laststagechangedate = models.TextField(blank=True, null=True)  # This field type is a guess.
    op_fiscalquarter = models.BigIntegerField(blank=True, null=True)
    op_fiscalyear = models.BigIntegerField(blank=True, null=True)
    op_fiscal = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_contactid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_lastvieweddate = models.TextField(blank=True, null=True)  # This field type is a guess.
    op_lastreferenceddate = models.TextField(blank=True, null=True)  # This field type is a guess.
    op_hasopenactivity = models.BooleanField(blank=True, null=True)
    op_hasoverduetask = models.BooleanField(blank=True, null=True)
    op_lastamountchangedhistoryid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_lastclosedatechangedhistoryid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_distributor_field = models.CharField(db_column='op_distributor_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_opportunity_description_field = models.CharField(db_column='op_opportunity_description_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_project_field = models.CharField(db_column='op_project_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_push_out_date_field = models.DateField(db_column='op_push_out_date_', blank=True, null=True)  # Field renamed because it ended with '_'.
    opontains_ode_product_field = models.BooleanField(db_column='opontains_ode_product_', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_mgr_commit_field = models.BooleanField(db_column='op_mgr_commit_', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_licenseonfiguration_approved_field = models.BooleanField(db_column='op_licenseonfiguration_approved_', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_does_oppty_include_licensed_product_field = models.CharField(db_column='op_does_oppty_include_licensed_product_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_po_number_field = models.CharField(db_column='op_po_number_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_serial_number_field = models.CharField(db_column='op_serial_number_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_so_number_field = models.CharField(db_column='op_so_number_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_invoice_number_field = models.CharField(db_column='op_invoice_number_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_sales_tax_field = models.CharField(db_column='op_sales_tax_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_freight_term_field = models.CharField(db_column='op_freight_term_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_method_of_shipment_field = models.CharField(db_column='op_method_of_shipment_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_freight_charge_field = models.CharField(db_column='op_freight_charge_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_reason_on_hold_or_lost_field = models.CharField(db_column='op_reason_on_hold_or_lost_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_product_gap_detail_field = models.CharField(db_column='op_product_gap_detail_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_oppo_ship_to_field = models.CharField(db_column='op_oppo_ship_to_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_upgrade_contact_name_field = models.CharField(db_column='op_upgrade_contact_name_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_upgrade_contact_email_address_field = models.CharField(db_column='op_upgrade_contact_email_address_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_support_renewal_field = models.BooleanField(db_column='op_support_renewal_', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_product_gap_yes_field = models.BooleanField(db_column='op_product_gap_yes_', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_follow_up_date_field = models.DateField(db_column='op_follow_up_date_', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_award_date_field = models.DateField(db_column='op_award_date_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_id = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    pr_ownerid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    pr_isdeleted = models.BooleanField(blank=True, null=True)
    pr_name = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    pr_recordtypeid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    pr_createddate = models.TextField(blank=True, null=True)  # This field type is a guess.
    pr_createdbyid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    pr_lastmodifieddate = models.TextField(blank=True, null=True)  # This field type is a guess.
    pr_lastmodifiedbyid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    pr_systemmodstamp = models.TextField(blank=True, null=True)  # This field type is a guess.
    pr_lastactivitydate = models.DateField(blank=True, null=True)
    pr_lastvieweddate = models.TextField(blank=True, null=True)  # This field type is a guess.
    pr_lastreferenceddate = models.TextField(blank=True, null=True)  # This field type is a guess.
    pr_follow_up_date_field = models.DateField(db_column='pr_follow_up_date_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_campaign_field = models.CharField(db_column='pr_campaign_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_lynuxworks_strengths_field = models.CharField(db_column='pr_lynuxworks_strengths_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_lynuxworks_weaknesses_field = models.CharField(db_column='pr_lynuxworks_weaknesses_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_design_win_type_field = models.CharField(db_column='pr_design_win_type_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_exec_advocate_field = models.CharField(db_column='pr_exec_advocate_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_submit_license_info_for_approval_field = models.BooleanField(db_column='pr_submit_license_info_for_approval_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_does_project_include_licensed_product_field = models.CharField(db_column='pr_does_project_include_licensed_product_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_license_configuration_approved_field = models.BooleanField(db_column='pr_license_configuration_approved_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_lead_source_field = models.CharField(db_column='pr_lead_source_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_compelling_event_s_field = models.CharField(db_column='pr_compelling_event_s_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_application_type_field = models.CharField(db_column='pr_application_type_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_decision_criteria_field = models.CharField(db_column='pr_decision_criteria_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_design_win_field = models.BooleanField(db_column='pr_design_win_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_design_win_date_field = models.DateField(db_column='pr_design_win_date_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_development_host_field = models.CharField(db_column='pr_development_host_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_distributor_field = models.CharField(db_column='pr_distributor_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_government_agency_field = models.CharField(db_column='pr_government_agency_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_government_program_name_field = models.CharField(db_column='pr_government_program_name_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_if_this_is_sub_who_is_prime_field = models.CharField(db_column='pr_if_this_is_sub_who_is_prime_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_include_in_top_projects_report_field = models.BooleanField(db_column='pr_include_in_top_projects_report_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_last_updated_on_field = models.DateField(db_column='pr_last_updated_on_', blank=True, null=True)  # Field renamed because it ended with '_'.
    prontains_ode_product_field = models.BooleanField(db_column='prontains_ode_product_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_lifetime_total_forecast_conservative_field = models.FloatField(db_column='pr_lifetime_total_forecast_conservative_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_lifetime_total_forecast_optimistic_field = models.FloatField(db_column='pr_lifetime_total_forecast_optimistic_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_reason_lost_field = models.CharField(db_column='pr_reason_lost_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_meets_design_win_criteria_field = models.BooleanField(db_column='pr_meets_design_win_criteria_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_dev_tool_host_license_field = models.CharField(db_column='pr_dev_tool_host_license_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_development_tool_license_model_field = models.CharField(db_column='pr_development_tool_license_model_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_war_room_priority_field = models.CharField(db_column='pr_war_room_priority_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_processor_s_under_consideration_field = models.CharField(db_column='pr_processor_s_under_consideration_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_project_stage_field = models.CharField(db_column='pr_project_stage_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_project_type_field = models.CharField(db_column='pr_project_type_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_run_time_status_field = models.CharField(db_column='pr_run_time_status_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_specific_processor_type_field = models.CharField(db_column='pr_specific_processor_type_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_support_status_field = models.CharField(db_column='pr_support_status_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_target_boards_under_consideration_field = models.CharField(db_column='pr_target_boards_under_consideration_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_os_of_interest_field = models.CharField(db_column='pr_os_of_interest_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_tools_requirements_field = models.CharField(db_column='pr_tools_requirements_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_account_field = models.CharField(db_column='pr_account_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_dev_tool_rtos_processor_architecture_field = models.CharField(db_column='pr_dev_tool_rtos_processor_architecture_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_development_tool_user_license_type_field = models.CharField(db_column='pr_development_tool_user_license_type_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_rtos_dev_deploy_lic_project_description_field = models.CharField(db_column='pr_rtos_dev_deploy_lic_project_description_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_rtos_dev_deploy_license_site_description_field = models.CharField(db_column='pr_rtos_dev_deploy_license_site_description_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_market_segment_field = models.CharField(db_column='pr_market_segment_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_rtos_deployment_license_type_field = models.CharField(db_column='pr_rtos_deployment_license_type_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_meets_oderiteria_field = models.BooleanField(db_column='pr_meets_oderiteria_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_program_field = models.CharField(db_column='pr_program_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_graphic_hardware_field = models.CharField(db_column='pr_graphic_hardware_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_graphics_software_requirements_field = models.CharField(db_column='pr_graphics_software_requirements_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_graphics_software_details_field = models.CharField(db_column='pr_graphics_software_details_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_other_tools_requirements_field = models.CharField(db_column='pr_other_tools_requirements_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_project_license_size_field = models.CharField(db_column='pr_project_license_size_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_lost_on_hold_reason_field = models.CharField(db_column='pr_lost_on_hold_reason_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_competitor_field = models.CharField(db_column='pr_competitor_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_development_tool_site_restriction_field = models.CharField(db_column='pr_development_tool_site_restriction_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_product_licensing_field = models.CharField(db_column='pr_product_licensing_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_x3rd_party_tools_requirements_field = models.CharField(db_column='pr_x3rd_party_tools_requirements_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    pr_special_license_terms_attach_license_field = models.BooleanField(db_column='pr_special_license_terms_attach_license_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_id = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_isdeleted = models.BooleanField(blank=True, null=True)
    ac_masterrecordid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_name = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_type = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_recordtypeid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_parentid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_billingstreet = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_billingcity = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_billingstate = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_billingpostalcode = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_billingcountry = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_billinglatitude = models.FloatField(blank=True, null=True)
    ac_billinglongitude = models.FloatField(blank=True, null=True)
    ac_billinggeocodeaccuracy = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shippingstreet = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shippingcity = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shippingstate = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shippingpostalcode = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shippingcountry = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shippinglatitude = models.FloatField(blank=True, null=True)
    ac_shippinglongitude = models.FloatField(blank=True, null=True)
    ac_shippinggeocodeaccuracy = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_phone = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_fax = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_accountnumber = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_website = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_photourl = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_sic = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_industry = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_annualrevenue = models.FloatField(blank=True, null=True)
    ac_numberofemployees = models.BigIntegerField(blank=True, null=True)
    ac_ownership = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_tickersymbol = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_rating = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_site = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_ownerid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_createddate = models.TextField(blank=True, null=True)  # This field type is a guess.
    ac_createdbyid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_lastmodifieddate = models.TextField(blank=True, null=True)  # This field type is a guess.
    ac_lastmodifiedbyid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_systemmodstamp = models.TextField(blank=True, null=True)  # This field type is a guess.
    ac_lastactivitydate = models.DateField(blank=True, null=True)
    ac_lastvieweddate = models.TextField(blank=True, null=True)  # This field type is a guess.
    ac_lastreferenceddate = models.TextField(blank=True, null=True)  # This field type is a guess.
    ac_jigsaw = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_jigsawcompanyid = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_accountsource = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_sicdesc = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_shipping_phone_field = models.CharField(db_column='ac_shipping_phone_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_shipping_fax_field = models.CharField(db_column='ac_shipping_fax_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_sales_team_field = models.CharField(db_column='ac_sales_team_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_duns_field = models.CharField(db_column='ac_duns_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_focus_or_general_field = models.CharField(db_column='ac_focus_or_general_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_project_lynxos_field = models.BooleanField(db_column='ac_project_lynxos_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_strategic_strengths_field = models.CharField(db_column='ac_strategic_strengths_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_critical_vulnerability_field = models.CharField(db_column='ac_critical_vulnerability_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_goals_field = models.CharField(db_column='ac_goals_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_account_field = models.CharField(db_column='ac_account_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_bonus_eligible_field = models.BooleanField(db_column='ac_bonus_eligible_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_account_type_field = models.CharField(db_column='ac_account_type_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_project_lynxsecure_field = models.BooleanField(db_column='ac_project_lynxsecure_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_project_lynxos_178_field = models.BooleanField(db_column='ac_project_lynxos_178_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_project_lynxos_se_field = models.BooleanField(db_column='ac_project_lynxos_se_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_safety_attack_plan_field = models.BooleanField(db_column='ac_safety_attack_plan_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_project_bluecat_field = models.BooleanField(db_column='ac_project_bluecat_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_follow_up_date_field = models.DateField(db_column='ac_follow_up_date_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_region_field = models.CharField(db_column='ac_region_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_validedge_field = models.BooleanField(db_column='ac_validedge_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_past_owner_field = models.CharField(db_column='ac_past_owner_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_business_unit_field = models.CharField(db_column='ac_business_unit_', max_length=8192, db_collation='binary', blank=True, null=True)  # Field renamed because it ended with '_'.
    op_opportunity_owner = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    ac_account_owner = models.CharField(max_length=8192, db_collation='binary', blank=True, null=True)
    op_pgopwin = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LYNX_HISTORICAL'
