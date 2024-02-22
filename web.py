import streamlit as st
import functions

st.set_page_config(layout="wide")

# Clear Button
clear_button = st.button("Clear List", key='button')

#  Design
st.markdown("<h1 style='text-align: center;'>Task Manager</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Keep Track of Your Tasks!</h2>", unsafe_allow_html=True)
col1, col2,col3 = st.columns(3)

# Function which adds input to the list also using functions.py
def add_todo():
    todo = st.session_state['new task'] + '\n'
    list.append(todo)
    functions.write_to_file(list)
    st.session_state['new task'] = ""

# Layout
buff, col, buff2 = st.columns([1,3,1])
col.text_input(label="Type in a task to do", placeholder='Add a new Task',
              on_change=add_todo, key='new task')

# Display Tasks
list = functions.read_list()

# Clear button functionality
if clear_button:
    # Create a copy of the list to iterate over
    for todo in list:
        list = functions.read_list()
        list.remove(todo)
        functions.write_to_file(list)
        del st.session_state[todo]

# Deleting tasks singularly
for index, todo in enumerate(list):
    checkbox = col2.checkbox(todo, key=todo)
    if checkbox:
        list.pop(index)
        functions.write_to_file(list)
        del st.session_state[todo]
        st.experimental_rerun()




