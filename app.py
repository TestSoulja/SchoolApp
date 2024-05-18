import streamlit as st
import pandas as pd
import requests
import datetime
from datetime import date, timedelta
import os
import time
import json
import streamlit_analytics

s = os.path.abspath(__file__)
c = s.replace(os.path.basename(os.path.abspath(__file__)), '')

with st.form("Просим пройти небольшой опрос"):
    
    st.write("Просим пройти небольшой опрос")
    
    st.write(" ")
    st.write(" ")
#     st.write("Как тебя зовут?)")
    
    name = st.text_input("Как тебя зовут? (имя, фамилия)")
    
    st.write(" ")
    st.write(" ")
#    st.write("Фамилия/или просто славное дополнение, а то у нас многовато тёсок")
   
    # name1 = st.text_input("Фамилия/или просто славное дополнение, а то у нас многовато тёсок")
    
    # st.write(" ")
    
    st.write("Что по напиткам?")
    
    checkbox_val = st.checkbox('Пиво')
    checkbox_val1 = st.checkbox("Шампанское")
    checkbox_val2 = st.checkbox("Вино")
    checkbox_val3 = st.checkbox("Сидр")
    checkbox_val4 = st.checkbox("Водка")
    checkbox_val5 = st.checkbox("Мартини")
    checkbox_val6 = st.checkbox("Виски")
    
    drink = st.text_input("Свой вариант напитков")
    
    st.write(" ")
    st.write(" ")
    st.write("Что по еде?")
    
    checkbox_val7 = st.checkbox("Пицца")
    checkbox_val8 = st.checkbox("Роллы")
    checkbox_val9 = st.checkbox("Бургеры")
    checkbox_val10 = st.checkbox("Тарталетки")
    checkbox_val11 = st.checkbox("Шашлык")
    
    food = st.text_input("Свой вариант еды")
    
    # Every form must have a submit button.
    # def s():
    #     st.success("okokok")
    
    
    # submitted = st.form_submit_button("Отправить пожелания")
    
    sub = st.form_submit_button("Отправить пожелания (нажми на меня 1 раз, я работаю, хотя это и не заметно)")
    # st.write("Нажать на кнопку можно 1 раз и всё отправится, ну максимум 2 раза, в любом случае мы всё получим")

   
    data = {
        "Имя": name,
        # "Фамилия": name1,
        "Food":{
        'Пиво': checkbox_val,
        "Шампанское": checkbox_val1,
        "Вино": checkbox_val2,
        "Сидр": checkbox_val3,
        "Водка": checkbox_val4,
        "Мартини": checkbox_val5,
        "Виски": checkbox_val6,
        "Пицца": checkbox_val7,
        "Роллы": checkbox_val8,
        "Бургеры": checkbox_val9,
        "Тарталетки": checkbox_val10,
        "Шашлык": checkbox_val11,
        "drink": drink,
        "food": food}
    }
   
    with open(c+"form.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    file.close()
    
    cou = 0
    tr = False
    while tr == False:
        try:
            y.upload(c+"form.json","/_Test/Second/form"+str(cou)+".json")
            # print("ok")
            tr = True
        except:
            cou += 1
            # print(cou)
    tr = False


delta = datetime.datetime(2023, 9, 16) - datetime.datetime.now()

def main():
    @st.cache(suppress_st_warning=True)
    
    def get_fvalue(val):
        feature_dict = {"No":1,"Yes":2}
        for key,value in feature_dict.items():
            if val == key:
                return value
    def get_value(val,my_dict):
        for key,value in my_dict.items():
            if val == key:
                return value
    
    ph = st.empty()
    N = 5*60
    for secs in range(N,0,-1):
        ph.metric("Дней до свадьбы:", "💀"+str(delta.days)+"💀")
        time.sleep(1)




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

    # def PostCasinoPass():
    #     if configCP != 0:
    #         cp = {
    #             "id": 0,
    #             "name": "Test",
    #             "enabled": bool(True),
    #             "vipStore": bool(True),
    #             "timeStart": str(date.today()-timedelta(days=10)) + "T08:00:00",
    #             "timeEnd": str(date.today()+timedelta(days=11)) + "T03:00:00",
    #             "previousSeasonStart": str(date.today()-timedelta(days=31)) + "T08:00:00",
    #             "previousSeasonEnd": str(date.today()-timedelta(days=10)) + "T03:00:00",
    #             "freeExpResetTime": "08:00",
    #             "predicates": "anybody",
    #             "skinId": 163,
    #             "giftGroupId": int(giftsCP),
    #             "optionConfigId": int(configCP)
    #             }
            
    #         response = requests.post('http://stage01.casinist.com:8509/casino_pass/create', json = cp)
    #         response
    #         requests.get('http://stage01.casinist.com:8509/casino_pass/reload', json = cp)
    #         st.success("CasinoPass Post Success")
    #     else:
    #         st.error("incorrect configId")
        
    # def PostEventPass():
    #     if configEP != 0 and giftsCP != 0:
    #         ep = {
    #         "name": "string",
    #         "enabled": bool(True),
    #         "skinId": 167,
    #         "timeStart": str(date.today()-timedelta(days=4)) + "T07:26:48.064Z",
    #         "timeEnd": str(date.today()+timedelta(days=3)) + "T07:26:48.064Z",
    #         "timeClose": str(date.today()+timedelta(days=4)) + "T07:26:48.064Z",
    #         "predicates": "anybody",
    #         "vipStore": bool(True),
    #         "actionsConfigId": 3,
    #         "optionsConfigId": int(configEP)
    #     }
            
    #         response = requests.post('http://stage01.casinist.com:8509/pass_event/events/create', json = ep)
    #         response
    #         requests.get('http://stage01.casinist.com:8509/pass_event/reload', json = ep)
    #         st.success("EventPass Post Success")
    #     else:
    #         st.error("incorrect configId")



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