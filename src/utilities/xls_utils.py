# -*- coding: utf-8 -*-
import xlsxwriter


class XlsUtils:

    def export(member,filename):
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()

        row = 1
        col = 0

        worksheet.write(0, 0, "ת.ז")
        worksheet.write(0, 1, "שם פרטי")
        worksheet.write(0, 2, "שם משפחה")
        worksheet.write(0, 3, "ת.לידה")
        worksheet.write(0, 4, "סוג מוצר פנסיוני")
        worksheet.write(0, 5, "שם התוכנית")
        worksheet.write(0, 6, "שם מסלול השקעה")
        worksheet.write(0, 7, "שם מעסיק")

        # Iterate over the data and write it out row by row.
        for mutzar in (member.get_mutzarim()):
            for maasik in (mutzar.get_maasikim()):
                worksheet.write(row, 0, member.member_personal_data.identity_number)
                worksheet.write(row, 1, member.member_personal_data.first_name)
                worksheet.write(row, 2, member.member_personal_data.last_name)
                worksheet.write(row, 3, member.member_personal_data.birth_date)
                worksheet.write(row, 4, mutzar.sug_mutzar)
                worksheet.write(row, 5, mutzar.shem_tochnit)
                worksheet.write(row, 6, mutzar.shem_maslul_hashkaa)
                worksheet.write(row, 7, maasik.name)
                row += 1


        workbook.close()

