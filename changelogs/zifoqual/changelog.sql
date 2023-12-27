--liquibase formatted sql

--changeset vsundararajan labels:Testing 
--comment: Testing
UPDATE m_sales_status SET status_name="1 - Opportunity Discovery" WHERE status_id=21 AND application=36;
UPDATE m_sales_status SET status_name="2 - Opportunity Qualification" WHERE status_id=5 AND application=36;
UPDATE m_sales_status SET status_name="3 - Proposal" WHERE status_id=7 AND application=36;
UPDATE m_sales_status SET status_name="4 - SoW Draft" WHERE status_id=8 AND application=36;
UPDATE m_sales_status SET status_name="5 - Awaiting PO" WHERE status_id=10 AND application=36;
UPDATE m_sales_status SET status_name="6 - Closed as Won" WHERE status_id=17 AND application=36;
UPDATE m_sales_status SET status_name="7 - Closed as Lost" WHERE status_id=13 AND application=36;	 
UPDATE m_sales_status SET udrf_summary_card = JSON_SET(udrf_summary_card, '$.dataType', '1 -Opportunity Discovery'), udrf_summary_card = JSON_SET(udrf_summary_card, '$.dataTypeCode', '1 Opportunity Discovery') WHERE status_id=21 AND application=36;

--changeset vsundararajan labels:Testing 
--comment: Testing
UPDATE m_sales_status SET status_name="1 - Opportunity Discovery" WHERE status_id=21 AND application=36;
UPDATE m_sales_status SET status_name="2 - Opportunity Qualification" WHERE status_id=5 AND application=36;
UPDATE m_sales_status SET status_name="3 - Proposal" WHERE status_id=7 AND application=36;
UPDATE m_sales_status SET status_name="4 - SoW Draft" WHERE status_id=8 AND application=36;
UPDATE m_sales_status SET status_name="5 - Awaiting PO" WHERE status_id=10 AND application=36;
UPDATE m_sales_status SET status_name="6 - Closed as Won" WHERE status_id=17 AND application=36;
UPDATE m_sales_status SET status_name="7 - Closed as Lost" WHERE status_id=13 AND application=36;	 
UPDATE m_sales_status SET udrf_summary_card = JSON_SET(udrf_summary_card, '$.dataType', '1 -Opportunity Discovery'), udrf_summary_card = JSON_SET(udrf_summary_card, '$.dataTypeCode', '1 Opportunity Discovery') WHERE status_id=21 AND application=36;

--changeset vsundararajan labels:Testing 
--comment: Testing
UPDATE m_sales_status SET status_name="1 - Opportunity Discovery" WHERE status_id=21 AND application=36;
UPDATE m_sales_status SET status_name="2 - Opportunity Qualification" WHERE status_id=5 AND application=36;
UPDATE m_sales_status SET status_name="3 - Proposal" WHERE status_id=7 AND application=36;
UPDATE m_sales_status SET status_name="4 - SoW Draft" WHERE status_id=8 AND application=36;
UPDATE m_sales_status SET status_name="5 - Awaiting PO" WHERE status_id=10 AND application=36;
UPDATE m_sales_status SET status_name="6 - Closed as Won" WHERE status_id=17 AND application=36;
UPDATE m_sales_status SET status_name="7 - Closed as Lost" WHERE status_id=13 AND application=36;	 
UPDATE m_sales_status SET udrf_summary_card = JSON_SET(udrf_summary_card, '$.dataType', '1 -Opportunity Discovery'), udrf_summary_card = JSON_SET(udrf_summary_card, '$.dataTypeCode', '1 Opportunity Discovery') WHERE status_id=21 AND application=36;


--changeset arakeshraj labels:test 
--comment: test
UPDATE kaar.t_assoc_subm SET hours = 8.38 WHERE id = 1856157; 
UPDATE kaar.t_assoc_subm SET is_active = 1 WHERE id = 1852020; 
SELECT * FROM congruent.t_notification WHERE recipient_id_1 = "532c63bb-c654-4181-9a3e-867a941be474";
