import streamlit as st
class Content:
    content_eng = {
        "test": "ENG-con",

        #USER STORY PAGE
        "user-story-title": "User story",
        "user-story-goal-page": "Page goals",
        "user-story-steps": "Page steps",
        "user-story-typical-mistakes": "Typical mistakes",
        "user-story-lets-write": "Lets write couple of user stories",
        "user-story-button-forget": "Forget context",
    }

    content_rus = {
        "test": "RUS-con",

        # USER STORY PAGE
        "user-story-title": "User story",
        "user-story-goal-page": "Цели страницы",
        "user-story-steps": "Этапы выполнения",
        "user-story-typical-mistakes": "Типичные ошибки",
        "user-story-lets-write": "Давай напишем пару user story",
        "user-story-button-forget": "Забыть контекст",
    }

    def gt(self, key):
        if st.session_state.get("LANGUAGE") == 'RUS':
            return self.content_rus[key]
        # elif st.session_state.get("LANGUAGE") == 'ENG':
        #     return self.content_eng[key]
        else:
            return self.content_eng[key]
