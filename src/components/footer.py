# import streamlit as st

# def footer_home():

#     logo_url="https://i.ibb.co/4r5X1FY/apnacollege.png"

#     st.markdown(f"""
#         <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
#             <p style="font-weight:bold; color:white;"> Created with Love by </p>
#             <img src='{logo_url}' style='max-height:25px' />
#         </div>
#                 """,unsafe_allow_html=True)

    


# def footer_dashboard():

#     logo_url="https://i.ibb.co/4r5X1FY/apnacollege.png"

#     st.markdown(f"""
#         <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
#             <p style="font-weight:bold; color:black;"> Created with Love by </p>
#             <img src='{logo_url}' style='max-height:25px' />
#         </div>
#                 """,unsafe_allow_html=True)



import streamlit as st


def footer_home():

    st.markdown("""
        <div style="
            margin-top: 2rem;
            display: flex;
            gap: 6px;
            justify-content: center;
            align-items: center;
        ">
            <p style="font-weight: bold; color: white; margin: 0;">
                Built with ❤️ by
            </p>

            <a href="#" style="font-weight: bold; color: white; text-decoration: none;">Manish Kumar</a>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():

    st.markdown("""
        <div style="
            margin-top: 2rem;
            display: flex;
            gap: 6px;
            justify-content: center;
            align-items: center;
        ">
            <p style="font-weight: bold; color: black; margin: 0;">
                Built with ❤️ by
            </p>

            <a href="#" style="font-weight: bold; color: black; text-decoration: none;">Manish Kumar</a>
        </div>
    """, unsafe_allow_html=True)