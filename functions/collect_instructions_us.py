import os
import streamlit as st
import langchain
import transformers
import huggingface_hub
from huggingface_hub import InferenceClient
from locals.prompt import *
from locals.content import *

lc = Content()
pt = Prompt()

#collecting context
def collect_instructions_us():
    user_story_role = pt.gp("user-story-role")
    do_not_pretend = pt.gp("do-not-pretend")
    user_story_description = pt.gp("user-story-description")
    user_story_example = pt.gp("user-story-example")
    language_instruction = pt.gp("language-instruction")
    length_instruction = pt.gp("length-instruction")
    string_instructions = user_story_role + do_not_pretend + user_story_description + user_story_example + language_instruction + length_instruction

    return string_instructions

