import streamlit as st
import pandas as pd
from datetime import date, timedelta
import os
import os
import re
import pandas as pd
from colorama import Fore
import time
from numba import njit
from navec import Navec
from slovnet import NER
from ipymarkup import show_span_ascii_markup as show_markup

s = os.path.abspath(__file__)
c = s.replace(os.path.basename(os.path.abspath(__file__)), '')

uploaded_file = st.file_uploader("Choose a file", type = 'xlsx')
sheet = st.text_input("Enter your name", "")

if uploaded_file is not None:
    df1 = pd.read_excel(uploaded_file, sheet_name=sheet, decimal =',')
    print(df1.head())
    
def main():
    @st.cache(suppress_st_warning=True)
    
    def get_fvalue(val):
        feature_dict = {"No":1,"Yes":2}
        for key,value in feature_dict.items():
            if val == key:
                return value



if __name__ == '__main__':
    main()
    
    # def DeleteCasinoPass():
    #     response = requests.delete('http://stage01.casinist.com:8509/casino_pass/clear')
    #     response
    #     st.success("CasinoPass Delete Success")

    # def DeleteEventPass():
    #     response = requests.delete('http://stage01.casinist.com:8509/pass_event/events/clear')
    #     response
    #     st.success("EventPass Delete Success")





    # Pages
    # if app_mode=='StageEvents':
        
    #     st.title('StageEvents :')
        
    #     event = st.selectbox('For what',['none','CasinoPass','EventPass'])
        
    #     if event == "none":
    #         st.markdown('')
            
    #     elif event == "CasinoPass":
            
    #         # st.subheader("Get")
    #         # st.button("GetCasinoPass", on_click=GetCasinoPass)
            
    #         st.subheader("Delete")
    #         st.button("Delete CasinoPass", on_click=DeleteCasinoPass)
            
    #         st.subheader("Post")
    #         configCP = st.number_input("configId",step=1, help="Конфиг, который нужно завести (последний - 39)")
    #         giftsCP = st.number_input("giftsId",step=1, help="Активные группы на стэйдже с препиской 'season'")
    #         st.button("Post CasinoPass", on_click=PostCasinoPass)
            
    #     elif event == "EventPass":
            
    #         # st.subheader("Get")
    #         # st.button("GetEventPass", on_click=GetEventPass)
            
    #         st.subheader("Delete")
    #         st.button("Delete EventPass", on_click=DeleteEventPass)
            
    #         st.subheader("Post")
    #         configEP = st.number_input("configId",step=1, help="Конфиг, который нужно завести (последний - 27)")
    #         st.button("Post EventPass", on_click=PostEventPass)
    
    # elif app_mode == "Skins":
        
    #     st.title('StageEvents :')
        
    #     event = st.selectbox('For what',['none','EventPass'])
        
    #     if event == "none":
    #         st.markdown('')
            
    #     elif event == "EventPass":
            
    #         st.subheader("LocSkin")
            
            
    #         st.subheader("ColorSkin")
            
    

# st.image('loan_image.jpg')
# st.markdown('Dataset :')
# data=pd.read_csv('loan_dataset.csv')
# st.write(data.head())
# st.markdown('Applicant Income VS Loan Amount ')
# st.bar_chart(data[['ApplicantIncome','LoanAmount']].head(20))

# name = st.text_input("Enter your name", "")
# st.write(f"Hello {name}!")

# st.number_input("Config id", 1, 1000)
# st.button("Delete")
# st.sidebar.button("Delete")


# x = st.slider("Select an integer x", 0, 10, 1)
# y = st.slider("Select an integer y", 0, 10, 1)
# df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
# st.write(df)

# backgroundColor="#0F0F0"