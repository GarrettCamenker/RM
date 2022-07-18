import time
from ctypes import alignment
import streamlit as st
import numpy as np
import pandas as pd
from resources import examples

from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES
st. set_page_config(layout="wide")

LANGS = [ 'python','sql','scala']
DEFAULT_LANG = 1

def loadl():
    return DEFAULT_LANG

class Container1(object):

    def __init__(self) -> None:
        pass


def change_lang(new:int):

    DEFAULT_LANG = new

def main():
    c1, c2 = st.columns([3, 1.3])
 
    with c1:
        c1_container = st.container()
    with c2:
        c2_container = st.container()
    
    with c2:
        c2.subheader("Risk Mgmt Subscription Service")
        _lang = c2.selectbox("Language", options=LANGS, index=DEFAULT_LANG, on_change=change_lang(0))
        
    with c2_container:
        desc = c2.markdown('**\*The following column aliases are required in each row of your dataframe:**')
        descr = c2.code(examples.CODE_EXAMPLES[LANGS[DEFAULT_LANG]],
                            language=LANGS[DEFAULT_LANG])
        c2.markdown('''**\*Use any additional columns to define custom report
        parameters and filters**''')
        report = c2.selectbox('Select Workspace',options=['Garrett\'s Workspace','Garrett\'s 2nd Workspace'],index=0)
        report = c2.selectbox('Select Your Report',options=['Garrett\'s Report','Garrett\'s 2nd Report'],index=0)

    with c1_container:
        content = st_ace(
            placeholder='Enter your query.',
            language=_lang,
            theme='twilight',
            keybinding='vscode',
            font_size=14,
            tab_size=4,
            show_gutter=True,
            show_print_margin=False,
            wrap=False,
            auto_update=False,
            readonly=False,
            height=400,
#            min_lines=22,
            key="ace",
        )
 
        if content:
            with st.spinner('Loading Query...'):
                time.sleep(1)
                df = pd.DataFrame(np.random.randn(50, 22),columns=('col %d' % i for i in range(22)))
                st.text('Query Results:')
                table = st.dataframe(df,height=200)  # Same as st.write(df)
                table.use_container_width = True
    

    
 
if __name__ == "__main__":
    main()
 
