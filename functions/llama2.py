import os

#import replicate
import streamlit as st
import langchain
import transformers
import huggingface_hub
from huggingface_hub import InferenceClient

#collecting context
def model_response(prompt_input):
    #string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."

    role_rus = "Ты в роли опытного бизнес аналитика. Ты должен помочь пользователю написать USER STORY. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    description_rus = "USER STORY это короткое простое описание фунционала, описанное от лица ПЕРСОНЫ, которая желает получить новые возможности системы. "
    format_rus = "Как пользователь < тип ПОЛЬЗОВАТЕЛЯ >, Я хочу < такую-то ЦЕЛЬ > для того чтобы < определенная ПРИЧИНА/ПОТРЕБНОСТЬ >."
    prompt_rus = "Помоги написать юзер стори для фичи в моем приложении. Фича похожа на сторисы в инстаграм."
    language_rus = "Ты должен отвечать только на РУССКОМ языке."

    string_dialogue = "%s %s Формат должен быть такой: %s User promt: %s %s " % (role_rus, description_rus, format_rus, prompt_input, language_rus)

    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    print(string_dialogue)
    print('--------------')
    return response2(string_dialogue, prompt_input)

endpoint_url = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-70b-chat-hf"
hf_token = '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'

client = InferenceClient(endpoint_url, token=hf_token)

gen_kwargs = dict(
    max_new_tokens=500,
    top_k=30,
    top_p=0.9,
    temperature=0.2,
    repetition_penalty=1.02,
    stream = False,
    details=False,
    #stop_sequences=["\nUser:", "<|endoftext|>", "</s>"],
)

#model call
def response2(string_dialogue, prompt_input):
    # output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
    #                        input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
    #                               "temperature": 0.01, "top_p": 0.1, "max_length": 120,
    #                               "repetition_penalty": 1})
    #return output
    #print(hf_token)
    prompt = f"{string_dialogue} {prompt_input} Assistant: "
    return client.text_generation(prompt, **gen_kwargs)