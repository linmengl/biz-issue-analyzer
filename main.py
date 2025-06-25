# 主入口
from agents.classifier import classify_issue
from agents.tool_executor import execute_tools
from agents.analyzer import analyze_issue

def main():
    print("=== 业务问题分析助手 ===")
    user_input = input("请输入订单问题描述：")
    order_id = input("请输入订单号：")

    print("\n[1] 正在识别问题类型...")
    issue_type = classify_issue(user_input)
    print(f"识别结果：{issue_type}")

    print("\n[2] 正在调用相关工具获取信息...")
    info_dict = execute_tools(order_id, issue_type)
    print(f"工具信息：{info_dict}")

    print("\n[3] 正在分析问题...")
    analysis_result = analyze_issue(user_input, info_dict)

    print("\n=== 分析报告输出 ===")
    print(analysis_result)

if __name__ == "__main__":
    main()