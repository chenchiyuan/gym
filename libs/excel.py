# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function


class ExcelHelper(object):
    @classmethod
    def write(cls, path, data, encoding="utf-8"):
        import xlwt
        workbook = xlwt.Workbook(encoding)
        worksheet = workbook.add_sheet('sheet1')

        for i, line in enumerate(data):
            for j, text in enumerate(line):
                worksheet.write(i, j, label=text)
        workbook.save(path)

    @classmethod
    def read(cls, path, from_row=1, from_col=0):
        import xlrd
        workbook = xlrd.open_workbook(path)
        sheet = workbook.sheets()[0]
        lines = []
        for row in range(from_row, sheet.nrows):
            line = []
            for col in range(from_col, sheet.ncols):
                line.append(sheet.cell(row, col).value)
            lines.append(line)
        return lines