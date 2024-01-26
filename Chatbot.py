from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os

information = """Charles Oliveira (born 17 October 1989) is a Brazilian professional mixed martial artist[6] and third degree black belt Brazilian jiu-jitsu practitioner.[a]

Oliveira started training Brazilian jiu-jitsu in his youth, achieving multiple championship titles before transitioning to MMA in 2007.[6][7] Oliveira currently competes in the Lightweight division in the Ultimate Fighting Championship (UFC), where he is the former UFC Lightweight Champion. Oliveira holds multiple UFC records, notably the most submission wins in the organization's history at 16, most finishes at 20 and most bonuses at 19

As of May 10, 2022, he is #1 in the UFC lightweight rankings[8] and as of September 12, 2023, he is #5 in the UFC men's pound-for-pound rankings.[8]"""

if __name__ == '__main__':
    print("Hello World")

    summary_template = """
    Given the Linkedin information {information} about a person from i want yout to create: 
    1. A short summary
    2. Two intresting facts about them"""

    summary_prompt_template = PromptTemplate(input_variables=['information'],template=summary_template)

    llm = ChatOpenAI(temperature=0,model_name="gpt-3.5-turbo",streaming=True)
    chain = LLMChain(llm=llm,prompt=summary_prompt_template)
    print(chain.run(information=information))