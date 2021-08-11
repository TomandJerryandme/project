# -*- coding: utf-8 -*-

import read_excel
import re_match_file

ID_STR_INDEX = 0
MODEL_STR_INDEX = 1
# xml文件基本格式
XML_COMMON_STRING = """<?xml version="1.0" encoding="utf-8"?>
<odoo>
  <data noupdate="1">
    <!-- 主要是preset_data的数据量与格式的匹配不好做公共抽象 -->
    {preset_data}
  </data>
</odoo>"""
# csv文件格式
CSV_COMMON_STRING = """"""

# 生成预置文件（分为两种格式：从其他文件中获取数据、自己生成数据：大部分情况下是从EXCEL文件中获取）
# 从其他文件中获取数据：从excel文件、从txt文件、甚至从csv文件，如果是从txt文件的话很大概率需要用正则表达式取数
# 自己生成数据：大部分情况是生成xml文件的预置数据，该预置数据不与其他数据关联

# 需要传入参数：文件后缀，文件内容格式，文件名，参数列表
# 文件后缀与参数列表用于生成对应的文件内容格式
# csv文件是以","为分隔符
# xml文件

"""
一般的xml文件预置格式

其中，param有可能是一个ref值，就需要变化
如果是多个ref值

并且，record中，多个参数的值可能是相同的

"𓆗𓆏𓆌𓆉𓆈𓅰𓅭𓅪𓅦𓅜𓄿𓃻𓃹𓃷𓃵𓃲𓃱𓃰𓃯𓃬𓆧𓆦𓆣𓆡𓆟𓆗𓆏𓆌𓆉𓆈𓅰𓅭𓅪𓅦𓆗𓆏𓆌𓆉𓆈𓅰𓅭𓅪𓅦𓅜𓄿𓃻𓃹𓃷𓃵𓃲𓃱𓃰𓃯𓃬𓆧𓆦𓆣𓆡𓆟𓆗𓆏𓆌𓆉𓆈𓅰𓅭𓅪𓅦𓆗𓆏𓆌𓆉𓆈𓅰𓅭"

<odoo>
    <data noupdate="1">
        <!-- 注释 -->
        <record id="id1" model="model">
            <field name="param1">1</field>
            <field name="param2">serial_number</field>
            <field name="param3">6</field>
            <field name="param4">1</field>
            <field name="param5">1</field>
            <field name="param6" eval="ref('ps_mdm.currency-1')"/>
            <field name="param7" eval="'_'.join([str(ref('ps_mdm.account-1')), str(ref('ps_mdm.account-2')), str(ref('ps_mdm.account-3'))])"></field>
            %s
        </record>
        
        <record id="id2" model="model">
            <field name="param1">1</field>
            <field name="param2">serial_number</field>
            <field name="param3">6</field>
            <field name="param4">1</field>
            <field name="param5">1</field>
            # 从这里有可能不同，就可以将上面的这几个参数放在公共的record里
            <field name="param6" eval="ref('ps_mdm.currency-1')"/>
            <field name="param7" eval="'_'.join([str(ref('ps_mdm.account-1')), str(ref('ps_mdm.account-2')), str(ref('ps_mdm.account-3'))])"></field>
        </record>
    </data>
</odoo>

还有一种特殊的情况：
    如果预置的记录中，记录中不同的地方如%s里，不同的有相同的如：{common1：diff1, common2:diff2, common3:diff3}
    这种的情况目前没有实现递归调用，只能实现第一层

common_str = '
        <record id="id2" model="model">
            <record id="id2" model="model">
            <field name="param1">1</field>
            <field name="param2">serial_number</field>
            <field name="param3">6</field>
            <field name="param4">1</field>
            <field name="param5">1</field>
            %s或者format方式进行动态赋值
        <record id="id2" model="model">'

"""



def generate_preset_file(file_type, params, file_name="preset_file", source_type="file", source_file_path=None):
    """
    生成对应的预置文件
    :param file_type: 文件类型(xml/csv)
    :param file_name: 文件名(用于生成文件使用)
    :param params: 参数列表
    :param source_type: 数据来源(file/manual)
    :param source_file_path: 数据来源文件路径
    :return: None
    """
    if file_type == "xml":
        generate_xml_file(params, source_data=source_file_path, file_name=file_name)
    elif file_type == "csv":
        generate_csv_file(params, source_data=source_file_path, file_name=file_name)


def generate_xml_common_format(params):
    """
    生成通用的xml文件预置格式
    :param params: 参数列表
    :param other_field_str: 用于扩展
    :return: result_str
    """
    result_str = ""
    index = 1
    for key in params.get("common_params"):
        index += 1
        param_value_str = '''      <field name="''' + key + '''">{''' + str(index) + '}</field>\n'
        result_str += param_value_str
    record_str_common = '    <record id="{' + "0" + '}" model="{' + "1" + '}">\n' + result_str + "%s" + '    </record>'

    return record_str_common

def generate_csv_format(params):
    """
    生成csv文件预置格式
    :param params:(LIST)
    :return:
    """
    global CSV_COMMON_STRING
    code_format = ""
    index = -1
    for param in params:
        index += 1
        if index != len(params) - 1:
            CSV_COMMON_STRING = CSV_COMMON_STRING + param + ','
            code_format += "{" + str(index) + "},"
        else:
            CSV_COMMON_STRING = CSV_COMMON_STRING + param + '\n'
            code_format += "{" + str(index) + "}" + '\n'
    return code_format

def generate_xml_file(params, source_data, file_name):
    """
    生成xml预置文件
    :param params: 参数字典（Dict）
    :param source_data: 数据来源
    :param file_name: 文件名
    :return: None
    """
    if params.get("sub_params", None):
        # 有参数具有附属参数，需要分为不同的记录
        xml_str_list = generate_xml_format_multi(params)
        index = 0
        model_str = params.get("model_str")
        id_str = params.get("id_str")
        for xml_str in xml_str_list:
            index += 1
            print(xml_str)
    else:
        xml_str_list = generate_xml_format_multi(params)
        print(xml_str_list[0])

def generate_xml_format_multi(params):
    """
    根据参数生成多条记录模板
    :param params:参数字典
    :param common_param_template: 公共参数的记录模板
    :return: 记录模板
    """
    index = 1
    common_param_template = generate_xml_common_format(params)
    params_templates_list = []
    sub_params = params.get("sub_params", [])
    index = 2 + len(params.get('common_params'))
    for param in sub_params:
        sub_template = common_param_template % (
                    '      <field name="' + param + '">{' + str(index) + '}</field>\n')
        params_templates_list.append(sub_template)
    if not sub_params:
        return [common_param_template % '']
    '''
    if not sub_params:
        # 最后一层子表
        for line in params.get('common_params'):
            index += 1
            sub_template = common_param_template % (
                        '      <field name="' + line + '">{' + str(index) + '}</field>\n')
            params_templates_list.append(sub_template)
        return params_templates_list

    # 下级还有子表，需要递归调用
    index += len(sub_params)
    params_templates_list.extend(generate_xml_format_multi(sub_params, index))
    elif isinstance(sub_params, list):
        for sub_param in sub_params:
            # 组织子分录
            index += 1
            sub_template = common_param_template % ('      <field name="' + sub_param + '">{' + str(index) + '}</field>\n')
            params_templates_list.append(sub_template)
    '''
    return params_templates_list

def generate_csv_file(params, source_data, file_name):
    format_str = generate_csv_format(params)
    with open('D:\\back\create_file\\' + file_name + '.csv', mode='w+') as f:
        f.write(CSV_COMMON_STRING)
        # for x in source_data:
        f.write(format_str.format('res1','source1', 'target1', 'type1'))

# generate_csv_file(['res_id', 'source_id', 'target_id', 'type'], source_data='', file_name='generate_csv_file')

# generate_xml_file({
#     'id_str': 'er_expense',
#     'model_str': 'er.expense',
#     'common_params': ['common_key1', 'common_key2'],
#     # 'sub_params': ['diff_key1', 'diff_key2', 'diff_key3'],
# })
