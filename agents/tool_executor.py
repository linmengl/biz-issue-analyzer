from tools.db_tool import query_order_db
from tools.log_tool import search_order_logs
from tools.doc_rag_tool import query_business_doc

def execute_tools(order_id, issue_type):
    result = {}
    if issue_type in ["支付失败", "退款异常"]:
        result['db'] = query_order_db(order_id)
        result['logs'] = search_order_logs(order_id)
    if issue_type == "退款异常":
        result['docs'] = query_business_doc("退款流程异常")
    return result
