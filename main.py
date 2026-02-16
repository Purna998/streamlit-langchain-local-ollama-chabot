import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

# Page configuration
st.set_page_config(
    page_title="Ollama Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .main {
        background-color: #0e1117;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Fixed configuration
model_name = "llama3.2"
temperature = 0.7
max_tokens = 2048

# Main chat interface
st.title("Ollama Chatbot")


# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.chat_history.append(HumanMessage(content=prompt))
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Initialize the LLM
            llm = ChatOllama(
                model=model_name,
                temperature=temperature,
                num_predict=max_tokens
            )
            
            # Stream the response
            with st.spinner("Thinking..."):
                for chunk in llm.stream(st.session_state.chat_history):
                    full_response += chunk.content
                    message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            st.session_state.chat_history.append(AIMessage(content=full_response))
            
        except Exception as e:
            error_message = f"❌ **Error:** {str(e)}\n\n"
            error_message += "**Possible solutions:**\n"
            error_message += "- Make sure Ollama is running (`ollama serve`)\n"
            error_message += f"- Verify the model is installed (`ollama pull {model_name}`)\n"
            error_message += "- Check if Ollama is accessible at http://localhost:11434"
            
            message_placeholder.error(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})

# Display welcome message if no messages
if len(st.session_state.messages) == 0:
    st.info("Welcome! Start chatting by typing a message below.")
    
    # Example prompts
    st.markdown("### Try these examples:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Write a poem about AI", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Write a short poem about artificial intelligence"})
            st.rerun()
    
    with col2:
        if st.button("Explain Python decorators", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Explain Python decorators with a simple example"})
            st.rerun()
    
    with col3:
        if st.button("Fun fact about space", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Tell me an interesting fact about space"})
            st.rerun()
