from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def oscar(filme, ano, llm):
    prompt_animal_name= PromptTemplate(
        input_variables=['filme', 'ano'],
        template= "Quantos oscars o filme {filme} ganhou em {ano}"
    )
    animal_name_chain= prompt_animal_name | llm | StrOutputParser()
    response = animal_name_chain.invoke({'filme':filme, 'ano':ano})
    
    return response

llm= OpenAI(temperature=0.5, model='gpt-3.5-turbo-instruct')

if __name__=="__main__":
    response=oscar("Oppenheimer", "2024", llm)
    print(response)