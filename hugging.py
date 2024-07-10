from transformers import pipeline, set_seed

# 텍스트 생성 파이프라인 초기화
text_generator = pipeline("text-generation", model="beomi/gemma-ko-2b")
set_seed(42)

# 예시 프롬프트에 기반하여 텍스트 생성
result = text_generator(
    "나는 오늘 어떤 하루를 보냈나면", max_length=80, num_return_sequences=1
)
