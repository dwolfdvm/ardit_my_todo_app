import functions
import streamlit as st

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"  # st.session is a dictionary, 'new_todo': ""
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My ToDo App")
st.subheader("This is my ToDo app")
st.write("This app increases productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a ToDo:", placeholder="Add a new ToDo here",
              on_change=add_todo, key="new_todo")


# use terminal to view streamlit, enter: streamlit run web1.py
