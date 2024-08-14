from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def generate_dog_name(animal_type, color):
    llm= OpenAI(temperature=0.5)
    prompt_animal_name= PromptTemplate(
        input_variables=['animal_type', 'color'],
        template= "Você tem um {animal_type} filhote novo da cor {color} e gostaria de dar um nome legal para ele, de 5 sugestões de possíveis nomes"
    )
    animal_name_chain= prompt_animal_name | llm | StrOutputParser()
    response = animal_name_chain.invoke({'animal_type':animal_type, 'color':color})
    
    return response

if __name__=="__main__":
    print(generate_dog_name("dragão", "preto"))