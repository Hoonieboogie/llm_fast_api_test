# 1️⃣ Python 3.12 버전 베이스 이미지 사용
FROM python:3.12

# 2️⃣ 환경 설정 (bytecode / 버퍼)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3️⃣ 작업 디렉토리 지정
WORKDIR /app

# 4️⃣ requirements.txt 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ 나머지 코드 전체 복사
COPY . .

# 6️⃣ 포트 명시 (FastAPI가 8000에서 실행됨)
EXPOSE 8000

# 7️⃣ 실행 명령 (Runpod이 컨테이너 시작 시 실행할 것)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
