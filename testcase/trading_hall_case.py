# @Time         : 2024/02/21 上午 10:26
# @Author       : ljx
# @File         : trading_hall_case.py
# @Software     : PyCharm
from utils import util
from utils.log import Log
from utils.readelement import Element

log = Log()
getToken = Element('Token')

# 引入测试用例 excel地址
cases = util.read_data('../testdata/test_case_trading_hall.xlsx', 'interface')
for case in cases:
    time = util.timestamp()
    case_id = case.get('case_id')
    url = case.get('url')
    url = url + '?timestamp=' + str(time)
    method = case.get('method')
    case_port = case.get('case_port')
    case_interface = case.get('case_interface')
    case_title = case.get('case_title')
    data = eval(case.get('data'))
    header = eval(case.get('header'))
    expect = eval(case.get('expect'))
    expect_msg = expect.get('message')
    r = util.request_method(method, data, header, url)

    # 以text格式打印出参
    response = r.json()
    real_msg = response.get('message')
    log.info(
        "用例ID:{}\n请求方式:{}\n请求标题:{}\n请求端口:{}\n请求url:{}\n请求结果:{}\n预期结果:{}\n实际结果:{} ".format(
            case_id, method,
            case_title,
            case_port,
            r.url,
            r.text,
            expect_msg,
            real_msg))
    if real_msg == expect_msg:
        log.info('第{}条用例测试通过'.format(case_id))
        final_re = "passed"
    else:
        log.error('第{}条用例测试不通过'.format(case_id))
        final_re = "failed"
    log.info('-------------------------------------')
    util.write_result("../testdata/test_case_trading_hall.xlsx", "interface", case_id + 1, 10, final_re)
