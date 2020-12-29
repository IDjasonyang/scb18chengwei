


from CHESHI1213.ceshi02 import read_case,api_fun,write_result
def execute_fun(filename,sheetname):
    cases = read_case(filename,sheetname)    #调用函数,设置变量接收返回值
    for case in cases:
        case_id = case['case_id']   #获取用例编号
        url_case = case['url']      #获取url的值
        data = eval(case['data'])   #字符串--字典
        expect = eval(case['expect'])  #预期结果
        expect_msg = expect['msg']  #预期结果中的msg
        real_result = api_fun(url=url_case,data=data)
        real_msg = real_result['msg']  #获取实际结果中的msg
        print('期望结果为: {}'.format(expect_msg))
        print('实际结果为: {}'.format(real_msg))

        if expect_msg == real_msg:
            print('第{}条用例不通过'.format(case_id))
            final_re = 'Passed'
        else:
            print('第{}条用例不通过'.format(case_id))
            final_re = 'Failed'
        write_result(filename,sheetname,case_id+1,8,final_re)  #写入结果到测试用例
        print('**********')
#调用函数
execute_fun('C:\\Python\\scb_18\\test_data\\test_case_api.xlsx','register')
execute_fun('C:\\Python\\scb_18\\test_data\\test_case_api.xlsx','login')