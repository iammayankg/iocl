#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlwt
import base64

def write_res(filename, res):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet 1')
    format_string = u"₹"
    for idx, prod in enumerate(res['productList']):
        cell = u"{} {}".format(format_string, prod['rsp'])
        ws.write(idx, 0, cell)
    wb.save(filename)


if __name__ == "__main__":
    import requests

    out_file = 'out.xlsx'
    url = "https://immense-earth-44640.herokuapp.com/api/"

    response = requests.get(url, auth=('username', 'password'))
    if response.status_code != 200:
        print("Response failed with code ", response.status_code)
    else:
        res = response.json()
        write_res(out_file, res)
    pass
