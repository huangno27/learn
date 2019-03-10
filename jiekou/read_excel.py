import xlrd

# excel文件名 data_file
# 工作簿名 sheet
# 用例名 case_name
# 不用每次都遍历excel
# 定义方法第一个获取所有数据
# 第二个查找该条用例的数据

def excel_to_list(data_file,sheet):
    # 新建空列表 乘取所有数据
    data_list = []
    wb = xlrd.open_workbook(data_file)                   # 打开excel
    sh = wb.sheet_by_name(sheet)                         # 获取工作簿
    header = sh.row_values(0)                            # 获取行标题数据
    for i in range(1,sh.nrows):                          # 跳过行标题 从第二行开始取数据
        d = dict(zip(header,sh.row_values(i)))           # 将标题和每行数据组装成字典
        data_list.append(d)
    return data_list                                     # 列表嵌套数据格式 每个元素是一个字典

def get_test_data(data_list,case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:          # 如果字典数据中case_name 与参数一致
            return case_data                             # 如果查询不到返回none
        #print("!")

if __name__ == '__main__':
    data_list = excel_to_list("test_user_data.xlsx","TestUserLogin")  # 读取工作簿
    case_data = get_test_data(data_list,'test_user_login_normal')     # 查找用例的数据
    print(case_data)



