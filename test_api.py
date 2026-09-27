import requests

def test_get_post():
    """测试GET请求：获取一篇文章"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    # 断言1：状态码必须是200
    assert response.status_code == 200
    # 断言2：返回的JSON里必须包含 'userId' 字段
    assert "userId" in response.json()
    # 断言3：标题不能为空
    assert response.json()["title"] != ""

def test_create_post():
    """测试POST请求：创建一篇文章"""
    payload = {"title": "test", "body": "hello", "userId": 1}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    # 断言返回的数据中，标题和我们发送的一致
    assert response.json()["title"] == "test"