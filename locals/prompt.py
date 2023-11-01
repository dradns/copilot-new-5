import streamlit as st
class Prompt:
    prompt_eng = {
        'test': 'ENG-con',


    }

    prompt_rus = {
        'test': 'RUS-con',
        'ss': 'bb'
    }

    def gp(self, key):
        if st.session_state.get("LANGUAGE") == 'RUS':
            return self.prompt_rus[key]
        # elif st.session_state.get("LANGUAGE") == 'ENG':
        #     return self.prompt_eng[key]
        else:
            return self.prompt_eng[key]