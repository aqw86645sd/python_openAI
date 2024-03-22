import openai
import os

# 定義 token 檔案名稱
file_path = "token/api_token"

# 檢查檔案是否存在
if not os.path.exists(file_path):
    # 如果檔案不存在，創建一個新檔案
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # 建立檔案
    with open(file_path, 'w') as file:
        file.write('')  # 可以在這裡寫入初始內容

    print(f"已創建新的 api_token 檔案，請填入 API taken。")
else:

    # 設置API密鑰
    api_token = open(file_path, "r").read()
    openai.api_key = api_token

    # 問題
    message = """ChatGPT 是什麼？"""

    # 調用ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    # 提取ChatGPT的回應
    print(response['choices'][0]['message']['content'])
