from django.shortcuts import render
import requests
import os

# 환경변수 사용 (RUNPOD_API_URL)
RUNPOD_API_URL = os.getenv("RUNPOD_API_URL", "https://<runpod-ip>:8000/rag") # 이거 runpod ip로 바꿔

def chat(request):
    answer = ""
    user_message = ""

    if request.method == "POST":
        user_message = request.POST.get("message", "")
        try:
            res = requests.post(RUNPOD_API_URL, json={"text": user_message}, timeout=60)
            if res.status_code == 200:
                answer = res.json().get("answer", "응답이 없습니다.")
            else:
                answer = f"서버 오류: {res.status_code}"
        except Exception as e:
            answer = f"에러 발생: {e}"

    return render(request, "chat.html", {"user_message": user_message, "answer": answer})
