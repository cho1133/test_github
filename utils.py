# 앱의 재사용성을 위해

# -------------------------------------------------------------------------
# 참고: 이 코드의 일부는 다음 GitHub 리포지토리에서 참고하였습니다:
# https://github.com/lim-hyo-jeong/Wanted-Pre-Onboarding-AI-2407
# 해당 리포지토리의 라이센스에 따라 사용되었습니다.
# -------------------------------------------------------------------------

import os
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import (
    LLMChain,
)  # 파이프라인과 다른점 - 순서가 중요할 떄 파이프라인을 활용
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv


# env로 key 불로오기

load_dotenv()

# 주어진 모델 이름으로 ChatGPT API 모델 불러오는 함수


# 키를 불러주고
def load_model(model_name: str) -> ChatOpenAI:

    # 닷스트링을 사용하는 이유 -> 다른 사람도 이해할 수있도록 작성합니다.
    """
    주어진 모델 이름을 기반으로 ChatOpenAI 모델을 로드합니다.

    Args:
        model_name (str): 사용할 모델의 이름.

    Returns:
        ChatOpenAI: 로드된 ChatOpenAI 모델.
    """

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model_name=model_name)
    return llm


# 사전에 저장해둔 prompt file을 읽어와 str로 반환하는 함수


def load_prompt(character_name: str):
    """캐릭터의 이름을 받아 그에 해당하는 프롬프트를 문자열로 반환

    Args:
        character_name (str): 불러올 캐릭터 이름을 입력받음 (바이든,트럼프)

    Returns:
        string(prompt): 불러온 프롬프트 내용을 반환
    """
    with open(f"prompts/{character_name}.prompt", "r", encoding="utf-8") as file:
        prompt = file.read().strip()  # 공백제거 strip
    return prompt


# 대화를 메모리하는 함수


def set_memory() -> ConversationBufferMemory:
    """
    대화 히스토리를 저장하기 위한 메모리를 설정합니다.

    Returns:
        ConversationBufferMemory: 초기화된 대화 메모리.
    """
    return ConversationBufferMemory(memory_key="chat_history", return_messages=True)


# langchain의 chain을 만들어주는 함수


def initialize_chain(
    llm: ChatOpenAI, character_name: str, memory: ConversationBufferMemory
) -> LLMChain:
    """
    주어진 LLM과 캐릭터 이름, 메모리를 기반으로 체인을 초기화합니다.

    Args:
        llm (ChatOpenAI): 사용할 언어 모델.
        character_name (str): 캐릭터의 이름.
        memory (ConversationBufferMemory): 대화 메모리.

    Returns:
        LLMChain: 초기화된 LLM 체인.
    """
    system_prompt = load_prompt(character_name)
    custom_prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{input}"),
        ]
    )
    chain = LLMChain(
        llm=llm, prompt=custom_prompt, verbose=True, memory=memory
    )  # verbose - chain에 들어온 것들을 출력합니다. 진행상황을 확인할 때 사용
    return chain


# LLM의 답변을 생성하는 함수(invoke) 0717 solar llm pipeline이 쓰이는 경우를 비교해볼것


def generate_message(chain: LLMChain, user_input: str) -> str:
    """
    사용자 입력을 기반으로 메시지를 생성합니다.

    Args:
        chain (LLMChain): 사용할 체인.
        user_input (str): 사용자의 입력.

    Returns:
        str: 생성된 응답 메시지.
    """
    result = chain({"input": user_input})
    response_content = result["text"]
    return response_content
