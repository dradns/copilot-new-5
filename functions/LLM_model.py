import os
import streamlit as st
import langchain
import transformers
import huggingface_hub
from huggingface_hub import InferenceClient
from functions.collect_instructions import *
from functions.collect_message_history import *

def model_improve_us():
    #1. собрать взять нужную инструкцию в зависимости от языка
    #2. собрать историю сообщений
    system_template = """Ты в роли бизнес аналитика. Предложи один вариант улучшения Пользовательской истории, которую ввел пользователь.
    Не отвечай от лица 'Пользователь' и не притворяйся 'Пользователь'. Ты будешь отвечать только как 'Ассистент'.
    Пользовательская история это короткое простое описание фунционала, описанное от лица ПЕРСОНЫ, которая желает получить новые возможности системы.
    Как пользователь <тип ПОЛЬЗОВАТЕЛЯ>, Я хочу <такую-то ЦЕЛЬ> для того чтобы <определенная ПРИЧИНА/ПОТРЕБНОСТЬ >.
    Отвечай ТОЛЬКО на РУССКОМ языке.
    Ты должен ответить не больше чем одним параграфом.
    """
    string_instructions_append_role = "Система: " + system_template + " "
    current_user_story_append_role = "Пользователь: " + st.session_state.get("tx-user-story-key")   #st.session_state["improved_us"]
    total_string = string_instructions_append_role + current_user_story_append_role
    print('--------------')
    print('--------------')
    print('total_string')
    print(total_string)
    print('--------------')
    print('--------------')
    return modell_call(total_string)

def model_generate_uc():
    #1. собрать взять нужную инструкцию в зависимости от языка
    #2. собрать историю сообщений
    system_template = """Ты в роли бизнес аналитика. На основе Пользовательской истории от пользователя напиши сценарии использования.
    Не отвечай от лица 'Пользователь' и не притворяйся 'Пользователь'. Ты будешь отвечать только как 'Ассистент'.
    Пользовательский сценарий описывает функциональные требования системы с точки зрения конечного пользователя, создавая последовательность событий, ориентированную на конкретную цель, последовательность легко осуществить для пользователя",
    Пример пользовательского сценария для ситуации, когда домработница стирает белье:
                                Участники — Жители, домработница и т.д.
                                Основной участник — Домработница
                                Цели — Постирать белье, сложить все предметы, при необходимости погладить одежду
                                Предусловия — Сегодня пятница, и в прачечной есть белье
                        
                                Основной флоу для этого пользовательского сценария:
                                Домработница приходит в прачечную в пятницу.Она приводит прачечную в порядок. 
                                После этого она стирает и сушит белье в каждой загрузки стиральной машины.
                                Она складывает вещи, которые нужно сложить, затем гладит и вешает мятые предметы.
                        
                                Альтернативные флоу:
                                Домработница гладит любые помятые вещи перед тем, как повесить их на вешалку.
                                Домработница перестирывает все вещи, которые посчитает грязными.
    Отвечай ТОЛЬКО на РУССКОМ языке.
    Ты должен ответить не больше чем одним параграфом.
    """

    string_instructions_append_role = "Система: " + system_template + " "
    current_user_story_append_role = "Пользователь: " + st.session_state.get("tx-user-story-key")   #st.session_state["improved_us"]
    total_string = string_instructions_append_role + current_user_story_append_role
    print('--------------')
    print('--------------')
    print('total_string')
    print(total_string)
    print('--------------')
    print('--------------')
    return modell_call(total_string)
def model_button_response(user_prompt, page_name):
    #1. собрать взять нужную инструкцию в зависимости от языка
    #2. собрать историю сообщений
    string_instructions_append_role = "Система: " + collect_instructions(page_name) + " "
    user_request_append_role = "Пользователь: " + user_prompt
    total_string = string_instructions_append_role + user_request_append_role
    print('--------------')
    print('--------------')
    print('total_string')
    print(total_string)
    print('--------------')
    print('--------------')
    return modell_call(total_string)

def model_response(user_prompt, page_name):
    #1. собрать взять нужную инструкцию в зависимости от языка
    #2. собрать историю сообщений

    # Collect instructions for page_name
    string_instructions = collect_instructions(page_name)
    #Сollect whole message history
    string_dialogue = collect_message_history(user_prompt, page_name)
    total_string = string_instructions + string_dialogue
    print(total_string)
    print('--------------')
    return modell_call(total_string)

endpoint_url = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-70b-chat-hf"
hf_token = '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'

client = InferenceClient(endpoint_url, token=hf_token)

gen_kwargs = dict(
    max_new_tokens=1000,
    top_k=30,
    top_p=0.5,
    temperature=0.1,
    repetition_penalty=1.02,
    stream = False,
    details=False,
    #stop_sequences=["\nUser:", "<|endoftext|>", "</s>"],
)

#model call
def modell_call(total_string):
    return client.text_generation(total_string, **gen_kwargs)