# 解析xml文件
import lxml.etree as xml

source_str = """
            <pssearch>
                <!-- 结算组织 -->
                <field name="sett_org_id" string="Settle Organization" required="1"/>
                <combine>
                    <!-- 往来单位 -->
                    <field name="contact_dept" string="Contact Department" required="1"/>
                    <!-- 供应商 -->
                    <field name="supplier_ids" string="Supplier" domain="[('use_org_id', '=', sett_org_id), ('state', '=', 'audit'), ('forbid_state', '=', 'normal')]" attrs="{'invisible': [('contact_dept','!=','supplier')]}"/>
                    <!-- 客户 -->
                    <field name="customer_ids" string="Customer" domain="[('use_org_id', '=', sett_org_id), ('state', '=', 'audit'), ('forbid_state', '=', 'normal')]" attrs="{'invisible': [('contact_dept','!=','customer')]}"/>
                    <!-- 部门 -->
                    <field name="department_ids" string="Department" domain="[('use_org_id', '=', sett_org_id), ('state', '=', 'audit'), ('forbid_state', '=', 'normal')]" attrs="{'invisible': [('contact_dept','!=','department')]}"/>
                    <!-- 员工 -->
                    <field name="employee_ids" string="Employee" domain="[('use_org_id', '=', sett_org_id), ('state', '=', 'audit'), ('forbid_state', '=', 'normal')]" attrs="{'invisible': [('contact_dept','!=','employee')]}"/>
                </combine>
                <!-- 币别 -->
                <field name="currency_ids" string="Currency" required="1" domain="[('number', '!=', '9999')]"/>
                <combine>
                    <!-- 开始日期 -->
                    <field name="start_date" string="Start Date" required="1"/>
                    <!-- 结束日期 -->
                    <field name="end_date" string="End Date" required="1"/>
                </combine>
                <combine>
                    <field name="is_include_unaudit_doc" string="Is Include Unaudit Doc"/>
                    <field name="is_including_temp_est_payable" string="Is Including Temp Est Payable"/>
                    <field name="is_only_temp_est_payable" string="Is Only Temp Est Payable"/>
                </combine>
            </pssearch>
"""

'''
    解析 xml.parse(文件)
         xml.XML(xml字符串)
'''
doc = xml.XML(source_str)
field_node = doc.xpath("//field")