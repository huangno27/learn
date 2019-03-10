import xlrd
# 打卡Excel
wb = xlrd.open_workbook("test_user_data.xlsx")

# 按工作薄名定位工作表
sh = wb.sheet_by_name("TestUserLogin")

# 有效数据行数
print(sh.nrows)
# 有效数据列数
print(sh.ncols)

# 输出第一行的所有值 'case_name'
print(sh.cell(0,0).value)

# 将数据和标题组装成字典，使数据更清晰
print(dict(zip(sh.row_values(0),sh.row_values(1))))

# 遍历Excel 打印所有的数据
for i in range(sh.nrows):
    print(sh.row_values(1))



