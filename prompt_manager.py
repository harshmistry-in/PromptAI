import os
from dotenv import load_dotenv

from logger import logger

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq


load_dotenv()


class PromptManager:
    def __init__(self):
        self.chat_groq = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0.7,
            model="openai/gpt-oss-120b",
        )
        logger.info("PromptManager initialized with ChatGroq model.")

    def generate_response(self, prompt_params: dict) -> str:
        try:
            prompt_template = PromptTemplate(
                template="""
                    You are an expert prompt engineer. Your task is to generate a response based on the following parameters: the objective of the request is {objective}, intended for {target_audience}, and should consider the following context: {context}. Use the provided input data, {input_data}, to produce a response that matches the required tone and style of {tone}, while strictly following these constraints or rules: {constraints}. The output should be formatted as {output_format} and provide a {detail_level} level of detail.
                    
                    Your response should only be bounded to prompt engineering and should not include any information or content that is not directly related to the prompt parameters provided. Focus on delivering a clear, concise, and relevant response that effectively addresses the user's needs based on the given parameters.
    
            """,
                input_variables=[
                    "objective",
                    "target_audience",
                    "context",
                    "input_data",
                    "tone",
                    "constraints",
                    "output_format",
                    "detail_level",
                ],
            )
            logger.debug(
                f"Prompt template created with input variables: {prompt_template.input_variables}"
            )

            chain = prompt_template | self.chat_groq
            logger.info("Prompt chain created successfully.")

            response = chain.invoke(
                {
                    "objective": prompt_params.get("objective", ""),
                    "target_audience": prompt_params.get("target_audience", ""),
                    "context": prompt_params.get("context", ""),
                    "input_data": prompt_params.get("input_data", ""),
                    "tone": prompt_params.get("tone", ""),
                    "constraints": prompt_params.get("constraints", ""),
                    "output_format": prompt_params.get("output_format", ""),
                    "detail_level": prompt_params.get("detail_level", ""),
                }
            )

            logger.info("Response generated successfully.")
            return response.content

        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return "An error occurred while generating the response."
