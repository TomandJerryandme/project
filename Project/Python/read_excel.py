# -*- coding: utf-8 -*-

import json

import xlrd, xlwt
from openpyxl import load_workbook
#  E
def read_excel_file():
    file = load_workbook(r"C:\Users\liuxuan02\Desktop\document_type.xlsx")
    sheet = file["Sheet1"]
    tran_list = ""
    source_list = ""
    for x in range(2, 110):
        document_type_source = sheet.cell(row=x, column=5).value
        document_type_tran = sheet.cell(row=x, column=6).value
        is_out = sheet.cell(row=x, column=8).value
        is_project = sheet.cell(row=x, column=9).value
        document_type_number = sheet.cell(row=x, column=12).value
        biz_type = sheet.cell(row=x, column=7).value
        if document_type_tran and document_type_source:
            print_source = document_type_source.split(".")[1]
            source_list = source_list + print_source + "\n"
            print_tran = ""
            if ". " in document_type_tran:
                print_tran = document_type_tran.split(". ")[1]
            else:
                print_tran = document_type_tran.split(".")[1]
            print(biz_type)

def read_excel_file_to_generate_dict():
    file = load_workbook(r"C:\Users\liuxuan02\Desktop\dict_items.xlsx")
    sheet = file["Sheet1"]
    source_list = ""
    dict = {}
    for x in range(1, 91):
        key_value = sheet.cell(row=x, column=3).value
        value_value = sheet.cell(row=x, column=2).value
        dict[key_value] = value_value
    return dict

# read_excel_file()
# import pandas as pd
# file = open(r"C:\Users\liuxuan02\Desktop\document_type.xlsx", "rb")
# pd.read_excel(r"C:\Users\liuxuan02\Desktop\document_type.xlsx", )
