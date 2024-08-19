from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from vectordb import url_to_retriever
from langchain_openai import OpenAI
llm=OpenAI(temperature=0.5, model='gpt-3.5-turbo-instruct')
prompt=ChatPromptTemplate.from_template("""Responda a pergunta com base apenas no contexto:
{context}
Pergunta: {input}                                                                                
                                        """)

document_chain = create_stuff_documents_chain(llm, prompt)
retriever = url_to_retriever('https://en.wikipedia.org/wiki/Oppenheimer_(film)')
retriever_chain=create_retrieval_chain(retriever, document_chain)
response = retriever_chain.invoke({"input":"Quantos Oscars o filme Oppenheimer ganhou em 2024?"})
print(response['answer'])