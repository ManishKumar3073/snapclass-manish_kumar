import streamlit as st

def header_home():

    # logo_url="https://i.ibb.co/YTYGn5qV/logo.png"
    logo_url="https://chatgpt.com/backend-api/estuary/content?id=file_0000000027ac8211901b2cd3fa55b385&ts=497051&p=fs&cid=1&sig=6fa13c765b2657bce509fe99bfabcaa71a26e492d08c59213e4d1ebdb40b2f2a&v=0"

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF'>Class<br/>Lens</h1> 
        </div>

                """,unsafe_allow_html=True)


def header_dashboard():

    logo_url="https://chatgpt.com/backend-api/estuary/content?id=file_0000000027ac8211901b2cd3fa55b385&ts=497051&p=fs&cid=1&sig=6fa13c765b2657bce509fe99bfabcaa71a26e492d08c59213e4d1ebdb40b2f2a&v=0"

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>Class<br/>Lens</h2> 
        </div>

                """,unsafe_allow_html=True)
