# test_texts_endpoint.py
import requests

def test_texts_endpoint():
    url = "http://127.0.0.1:8101/embedder"  # FastAPI 应用的 URL 和端点
    data = [
    "Deep learning has revolutionized the field of artificial intelligence by enabling computers to learn complex patterns in large datasets.",  # Reference sentence
    "Advanced neural networks in computational learning",  # Directly related to deep learning and AI
    "Big data analytics driving AI insights",  # Related through AI and data analysis
    "The convergence of deep learning and IoT technology",  # Relates to applications of deep learning in technology
    "Real-time language translation using AI",  # AI application, potentially involving deep learning
    "Predictive maintenance in industrial systems through AI",  # AI application, possibly using deep learning for predictions
    "Marine biology and ocean ecosystems",  # Unrelated, but shares the word 'deep' in a different context
    "The history of Renaissance art",  # Unrelated to AI but deals with history and analysis
    "Strategies for effective urban planning",  # Unrelated, deals with human environments
    "Culinary techniques in French cuisine",  # Unrelated, deals with culinary arts
    "Classical music composition in the 18th century"  # Unrelated, deals with music history
    ]
    response = requests.post(url, json=data)  # 发送 POST 请求
    print(response.status_code)  # 打印响应状态码
    print(response.json())  # 打印响应内容

if __name__ == "__main__":
    test_texts_endpoint()



