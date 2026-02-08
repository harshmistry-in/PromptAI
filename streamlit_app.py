import streamlit as st
from prompt_manager import PromptManager

def main():
    st.set_page_config(
        page_title="Prompt Engineer",
        page_icon="🧠"
        )
    
    st.title("Prompt Engineer 😀")
    
    st.subheader("Enter Prompt Parameters")
    objective = st.selectbox("Objective", ["RAG", "Summarization", "Code Generation", "Creative Writing", "Data Analysis", "AI Agent"   ])
    target_audience = st.selectbox("Target Audience", ["General Public", "Technical Experts", "Students", "Business Professionals", "Researchers"])
    context = st.text_area("Context", placeholder="Provide any relevant background information or context for the prompt.")
    input_data = st.selectbox("Input Data", ["None", "User Query", "Document", "Code Snippet", "Dataset", ])
    tone = st.selectbox("Tone", ["Technical", "Friendly", "Persuasive", "Neutral"])
    constraints = st.multiselect("Constraints", ["No slang", "Use simple language", "Include examples", "Be concise", "Use bullet points", "Avoid technical jargon", "Provide step-by-step instructions", "Focus on practical solutions", "Use a formal tone", "Include relevant statistics or data"])
    output_format = st.selectbox("Output Format", ["Text", "JSON", "Markdown"])
    detail_level = st.selectbox("Detail Level", ["Low", "Medium", "High"])
    
    if st.button("Generate Response"):
    
        # Validation
        if not objective.strip():
            st.warning("Objective is required!")
            st.stop()

        if not context.strip():
            st.warning("Context is required!")
            st.stop()

        if not input_data.strip():
            st.warning("Input Data is required!")
            st.stop()

        if not constraints:
            st.warning("Please select at least one constraint!")
            st.stop()

        with st.spinner("Generating response..."):
            prompt_params = {
                "objective": objective,
                "target_audience": target_audience,
                "context": context,
                "input_data": input_data,
                "tone": tone,
                "constraints": ", ".join(constraints),
                "output_format": output_format,
                "detail_level": detail_level,
            }

            prompt_manager = PromptManager()
            response = prompt_manager.generate_response(prompt_params)

            st.success("Generated Response!")
            st.write(response)

                
        
        st.markdown("---")
        st.markdown("Created with love ❤️ by **Harsh Mistry** - Prompt Engineer")


if __name__ == "__main__":
    main()