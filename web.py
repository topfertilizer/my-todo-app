import streamlit as st
from modules import functions as f

todos = []
f.load_todos(todos)


def add_todo():
    _todo = st.session_state['new_todo']
    todos.append(_todo)
    note = f'{todos[-1]} is now added to the list.'
    print(note)
    f.save_todos(todos)


st.title('Super Todo App')
st.subheader('Welcome to super Todo app')
st.write('Let\'s use it anyway you want!')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.save_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Enter a todo:', placeholder='todo...',
              on_change=add_todo, key='new_todo')
