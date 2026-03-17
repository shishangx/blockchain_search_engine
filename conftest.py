# conftest.py
import pytest
import json
import os

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 获取测试结果
    outcome = yield
    report = outcome.get_result()
    
    # 只关心实际执行阶段（call）的失败，忽略 setup/teardown 的失败
    if report.when == 'call' and report.failed:
        # 尝试从异常信息中提取 HTTP 状态码 (假设你用了 requests)
        error_message = str(report.longreprtext)
        status_code = "N/A"
        
        # 简单的提取逻辑：如果错误信息里包含 "status code"，就尝试抓一下
        # 实际项目中可以根据你的断言库（如 requests）做更精细的解析
        if "status_code" in item.funcargs: # 如果 fixture 里有 status_code
             pass 
        
        # 构建失败记录
        failure_data = {
            "name": item.nodeid,  # 测试用例名称
            "error": error_message[-300:].replace('\n', ' '), # 截取最后300字符，避免消息过长
        }
        
        # 将失败信息追加写入文件 (一行一个 JSON)
        with open("failure_report.json", "a") as f:
            f.write(json.dumps(failure_data) + "\n")
