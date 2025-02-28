import json
import sys

# 处理客户端请求
def handle_request(request):
    method = request.get("method")
    params = request.get("params", {})
    request_id = request.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "result": {"version": "1.0", "capabilities": ["resources", "tools"]},
            "id": request_id
        }
    elif method == "read_resource":
        uri = params.get("uri")
        with open(uri.replace("file:///", ""), "r") as f:
            content = f.read()
        return {"jsonrpc": "2.0", "result": content, "id": request_id}
    elif method == "call_tool":
        tool_name = params.get("name")
        if tool_name == "echo":
            return {"jsonrpc": "2.0", "result": params.get("message"), "id": request_id}
    else:
        return {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": request_id}

# 主循环：通过 Stdio 通信
def main():
    while True:
        # 从 stdin 读取请求
        raw_input = sys.stdin.readline().strip()
        if not raw_input:
            break
        request = json.loads(raw_input)
        
        # 处理请求并返回响应
        response = handle_request(request)
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()