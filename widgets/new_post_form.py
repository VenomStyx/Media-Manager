import os
from datetime import datetime

import streamlit as st

from resources.utility import convert_strings_to_datetime
from resources.config import settings_core
from resources.posts import post

settings = settings_core()


def app():

       ##### NEW POSTS FORM
    with st.form("new_post_form"):
        st.markdown("#### Create a new post")


        ##### DATE / TIME
        datetime_col_date, datetime_col_time = st.columns(2)
        
        with datetime_col_date:
            date_input = st.date_input("DATE")
        with datetime_col_time:
            time_input = st.time_input("TIME")

        datetime_input = convert_strings_to_datetime(date_input, time_input)

        ##### TITLE / DESCRIPTION
        chosen_title = st.text_input("Title")
        chosen_description = st.text_area("Description")


        ##### POST LOCATION
        st.write("Where would you like to post?")

        
        ##### ACCOUNT SELECTION
        def format_post_option(option=[]):
            return option['display_name']

        
        media_accounts_checkboxes = st.multiselect("Select media accounts", settings.media_accounts, format_func=format_post_option)

        #print(media_accounts_checkboxes)




        

        ##### FILE UPLOAD
        uploaded_file_list = []

        uploaded_files = st.file_uploader("Upload attachments", accept_multiple_files=True)

        st.info("Files that are uploaded first get put first in order when published.")
        
        if len(uploaded_files) > 0:
        
            ##### FOR UPLOADED FILES
            for your_file in uploaded_files:

                ##### CREATE A FILE NAME

                ## append datetime to file name to make it unique
                chosen_file_name = datetime.now().strftime("%Y-%m-%M-%S") + "-" + your_file.name

                ## create a path to the file


                #chosen_file_name = str(hash(your_file.getvalue())) + "." + your_file.name.split(".")[-1]
                new_file_path = os.path.join(settings.uploaded_media_dir, chosen_file_name)

                if not os.path.exists(new_file_path):
                    ##### SAVE THE FILE
                    with open(new_file_path, "wb") as f:
                        f.write(your_file.getbuffer())
                        print(f"Saved file {chosen_file_name} to disk")
                        uploaded_file_list.append(chosen_file_name)
            
                else:  
                    print(f"File {chosen_file_name} already exists. File has been referenced rather than saved.")
                    uploaded_file_list.append(chosen_file_name)


        ##### SUBMIT BUTTON
        submitted = st.form_submit_button("Submit")

        ##### IF SUBMITTED
        if submitted:

            ##### CREATE POST
            st.spinner("Creating post...")

            ##### IF POST IN FUTURE
            if datetime_input > datetime.now():

                ##### CHECK FOR MEDIAS SELECTED
                desired_medias = []

                if len(media_accounts_checkboxes) > 0:
                    for media_account in media_accounts_checkboxes:
                        desired_medias.append(media_account['name'])
                
                ##### CREATE POST OBJECT
                desired_post = post(chosen_title, chosen_description, "n/a", date_input, time_input, desired_medias, uploaded_file_list)
                
                ##### SAVE POST OBJECT
                desired_post.save_as_scheduled()

                ##### SUCCESS FEEDBACK
                st.success(f""""{chosen_title}" has been Scheduled!""")

            ##### IF POST IN PAST
            else:    
                ##### ERROR FEEDBACK
                st.warning(settings.post_not_scheduled_for_reason_time_in_past)