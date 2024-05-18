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

start_time = time.time()
counternames = 0
countersurnames = 0
navec = Navec.load(c+'Lib/navec_news_v1_1B_250K_300d_100q.tar')
ner = NER.load(c+'Lib/slovnet_ner_news_v1.tar')

uploaded_file = st.file_uploader("Choose a file", type = 'xlsx')
sheet = st.text_input("Enter your name", "")


def date(row):
    i = re.findall(r'\d\d/\d\d/\d\d', str(row["Операции по счету: Назначение платежа"])) or re.findall(r'\d\d,\d\d,\d\d', str(row["Операции по счету: Назначение платежа"])) or re.findall(r'\d\d/\d\d/\d\d\d\d', str(row["Операции по счету: Назначение платежа"])) or re.findall(r'\d\d.\d\d.\d\d\d\d', str(row["Операции по счету: Назначение платежа"]))
    if i != []:
        return i
    else:
        return ""

def learn(row):
    a = re.findall("обучения", str(row["Операции по счету: Назначение платежа"]), flags=re.IGNORECASE) or re.findall("обучение", str(row["Операции по счету: Назначение платежа"]), flags=re.IGNORECASE) or re.findall("образовательных", str(row["Операции по счету: Назначение платежа"]), flags=re.IGNORECASE)
    if a != []:
        return "Оплата обучения"
    
def name(row):
    global counternames
    en = []
    with open(c+"first.txt","r", encoding="utf-8") as names:
        lines = names.readlines()
        for nameq in lines:
            namez = nameq.replace("\n", "")
            v = re.sub(r'_', ' ', str(row["Операции по счету: Назначение платежа"]))
            v1 = re.sub(r';', ' ', v)
            v2 = re.sub(r'\b', ' ', v1)
            v3 = re.findall(r'\w+', v2, flags=re.IGNORECASE)

            for i in v3:
                if i.lower() == namez.lower():
                    en.append(i)

    #         print(Fore.YELLOW + f'\r[+] Проверка имен: {round(counternames*100/len(df), 2)}/{100}', end='')

    # counternames += 1
    if en != []:
        return en
    
                
def sur(row):
    global countersurnames
    en = []
    with open(c+"sec.txt","r", encoding="utf-8") as surname:
        lines = surname.readlines()
        for surnameq in lines:
            surz = surnameq.replace("\n", "")
            v = re.sub(r'_', ' ', str(row["Операции по счету: Назначение платежа"]))
            v1 = re.sub(r';', ' ', v)
            v2 = re.sub(r'\b', ' ', v1)
            v3 = re.findall(r'\w+', v2, flags=re.IGNORECASE)
            for i in v3:
                if i.lower() == surz.lower():
                    en.append(i)

    #         print(Fore.YELLOW + f'\r[+] Проверка фамилий: {round(countersurnames*100/len(df), 2)}/{100}', end='')
    # countersurnames += 1
    if en != []:
        return en

def mid(row):
    en = []
    with open(c+"mid.txt","r", encoding="utf-8") as mid:
        lines = mid.readlines()
        for mids in lines:
            midz = mids.replace("\n", "")
            v = re.sub(r'_', ' ', str(row["Операции по счету: Назначение платежа"]))
            v1 = re.sub(r';', ' ', v)
            v2 = re.sub(r'\b', ' ', v1)
            v3 = re.findall(r'\w+', v2, flags=re.IGNORECASE)
            for i in v3:
                if i.lower() == midz.lower():
                    en.append(i)

    if en != []:
        return en

def fio(row):
    global counters
    en = []
    text = str(row["Операции по счету: Назначение платежа"])
    ner.navec(navec)
    markup = ner(text)
    if markup.spans != []:
        for i in markup.spans:
            if i.type == "PER":
                # print(i)
                f = row["Операции по счету: Назначение платежа"][i.start:i.stop]
                # print(f)
                return f

def end():
    df.to_excel(c+'new.xlsx')
    
    st.download_button(label='📥 Download Current Result', file_name= 'new.xlsx')

    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\n"+'Elapsed time: ', elapsed_time)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name=sheet)
    
    df['Дата'] = df.apply(date, axis=1)
    df['Обучение'] = df.apply(learn, axis=1)
    # df['Имя'] = df.apply(name, axis=1)
    # df['Фамилия'] = df.apply(sur, axis=1)
    # df['Отчество'] = df.apply(mid, axis=1)
    df['ФИО'] = df.apply(fio, axis=1)
    end()

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