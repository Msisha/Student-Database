import streamlit as st
import streamlit_authenticator as stauth
from signup import sign_up, fetch_users
from streamlit_option_menu import option_menu
import dashboard
import courses
import students
import teacher
import Sessions

key_counter = 0


def Menu():
    global key_counter
    with st.sidebar:
        k = f"menu_{key_counter}"
        key_counter += 1  # Increment the counter for the next use
        app = option_menu(
            menu_title='Navigation ',
            options=['Dashboard', 'Students',
                     'Teachers', 'Courses', 'Sessions'],
            icons=['house-fill', 'person-circle',
                   'trophy-fill', 'chat-fill', 'info-circle-fill'],
            menu_icon='chat-text-fill',
            default_index=0,
            key=k,
            styles={
                "container": {"padding": "5!important", "background-color": 'black'},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                             "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )

    if app == "Dashboard":
        k = f"menu_{key_counter}"
        key_counter += 1
        dashboard.app()
    if app == "Students":
        k = f"menu_{key_counter}"
        key_counter += 1
        students.app()
    if app == "Teachers":
        k = f"menu_{key_counter}"
        key_counter += 1
        teacher.app()
    if app == "Courses":
        k = f"menu_{key_counter}"
        key_counter += 1
        courses.app()
    if app == "Sessions":
        k = f"menu_{key_counter}"
        key_counter += 1
        Sessions.app()

Menu()
# try:
#     users = fetch_users()
#     emails = []
#     usernames = []
#     passwords = []

#     for user in users:
#         emails.append(user['key'])
#         usernames.append(user['username'])
#         passwords.append(user['password'])

#     credentials = {'usernames': {}}
#     for index in range(len(emails)):
#         credentials['usernames'][usernames[index]] = {
#             'name': emails[index], 'password': passwords[index]}

#     Authenticator = stauth.Authenticate(
#         credentials, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4)

#     email, authentication_status, username = Authenticator.login(
#         ':green[Login]', 'main')

#     info, info1 = st.columns(2)

#     if not authentication_status:
#         sign_up()

#     if username:
#         if username in usernames:
#             if authentication_status:
#                 st.sidebar.subheader(f'Welcome {username}❤️')
#                 Authenticator.logout('Log Out', 'sidebar')
#                 Menu()
#                 st.sidebar.subheader("Made with ❤️ by our team")
#             elif not authentication_status:
#                 with info:
#                     st.error('Incorrect Password or username')
#             else:
#                 with info:
#                     st.warning('Please feed in your credentials')
#         else:
#             with info:
#                 st.warning('Username does not exist, Please Sign up')
# except:
#     # run()
#     st.success('Refresh Page')