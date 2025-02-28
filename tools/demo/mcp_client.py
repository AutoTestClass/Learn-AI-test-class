import subprocess
import json

# 启动 MCP Server 并与之交互
def run_mcp_client():
    # 启动服务器进程
    server_process = subprocess.Popen(
        ["python", "mcp_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    # 发送请求的辅助函数
    def send_request(request):
        server_process.stdin.write(json.dumps(request) + "\n")
        server_process.stdin.flush()
        return server_process.stdout.readline().strip()

    # 测试 initialize
    init_request = {"jsonrpc": "2.0", "method": "initialize", "id": 1}
    print("Initialize Response:", send_request(init_request))

    # 测试 read_resource
    resource_request = {
        "jsonrpc": "2.0",
        "method": "read_resource",
        "params": {"uri": "file:///file:///D:/github/AutoTestClass/Learn-AI-test-class/tools/demo/test.txt"},
        "id": 2
    }
    print("Read Resource Response:", send_request(resource_request))

    # 测试 call_tool
    tool_request = {
        "jsonrpc": "2.0",
        "method": "call_tool",
        "params": {"name": "echo", "message": "Hello from client!"},
        "id": 3
    }
    print("Tool Call Response:", send_request(tool_request))

    # 关闭服务器
    server_process.stdin.close()
    server_process.wait()

if __name__ == "__main__":
    run_mcp_client()