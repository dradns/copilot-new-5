import streamlit as st
class Content:
    content_eng = {
        #TEST
        "test": "ENG-con",
        #TOOLS
        "thinking": "Thinking...",



        #USER STORY PAGE
        "user-story-title": "User story",
        "user-story-description": "This page will help you to write User Story. It's recommended to read page goals, stages and typical mistakes. After that go to the chat and AI will help you to write User Story for you 😎",
        "user-story-goal-page": "Page goals 🎯",
        "user-story-steps": "Page steps 📶",
        "user-story-typical-mistakes": "Typical mistakes 🚨",
        "user-story-lets-write": "Are you ready to write couple of user stories?",
        "user-story-button-forget": "Forget context",
        "user-story-ass-first-reply": "I'm best business analyst ever! Wanna help?",
    }

    content_rus = {
        # TEST
        "test": "RUS-con",
        # TOOLS
        "thinking": "Думаю...",

        # USER STORY PAGE
        "user-story-title": "Пользовательская история",
        "user-story-description": "Эта страница поможет тебе написать пользовательскую историю. Рекомендую прочитать цели, этапы и типичные ошибки ниже. Потом переходи в чат и AI поможет тебе написать пользовательскую историю для тебя 😎",
        "user-story-goal-page": "Цели страницы 🎯",
        "user-story-steps": "Этапы выполнения 📶",
        "user-story-typical-mistakes": "Типичные ошибки 🚨",
        "user-story-lets-write": "Готов написать пару пользовательских историй?",
        "user-story-button-forget": "Забыть контекст",
        "user-story-ass-first-reply": "Я лучший бизнес аналитик! Давай помогу?",
    }

    def gt(self, key):
        if st.session_state.get("LANGUAGE") == 'RUS':
            return self.content_rus[key]
        # elif st.session_state.get("LANGUAGE") == 'ENG':
        #     return self.content_eng[key]
        else:
            return self.content_eng[key]
