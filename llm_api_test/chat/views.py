from django.shortcuts import render
import requests, os

RUNPOD_API_LAW = os.getenv("RUNPOD_API_LAW")
RUNPOD_API_MANUAL = os.getenv("RUNPOD_API_MANUAL")

def chat(request):
    answer = ""
    user_message = ""
    selected_mode = "manual"  # 기본값

    if request.method == "POST":
        user_message = request.POST.get("message", "")
        selected_mode = request.POST.get("mode", "law")

        if selected_mode == "law":
            runpod_url = RUNPOD_API_LAW
        else:
            runpod_url = RUNPOD_API_MANUAL

        try:
            res = requests.post(runpod_url, json={"text": user_message}, timeout=60)
            if res.status_code == 200:
                answer = res.json().get("answer", "응답 없음")
            else:
                answer = f"서버 오류: {res.status_code}"
        except Exception as e:
            answer = f"에러 발생: {e}"

    return render(
        request,
        "chat.html",
        {
            "user_message": user_message,
            "answer": answer,
            "selected_mode": selected_mode,
        },
    )
