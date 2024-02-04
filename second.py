import openai
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage  

# def Second(inside):
#     os.environ['OPENAI_API_KEY'] = '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'
#     llm = ChatOpenAI(openai_api_key='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')
#     # text=input("enter the sentence")
#     response = str(llm([HumanMessage(content=inside)]))
#     print("Langchain Response:", response)
#     split_string = response.split('=')
    
#     if len(split_string) >= 2:
#         data_string = split_string[1].split('"')
#         print("Data String:", data_string)  
        
#         if len(data_string) >= 2:
#             content = data_string[1].strip('" ')
#             return content
#         else:
#             print("Data string does not have enough elements.")
#     else:
#         print("Response does not have enough elements.")

#     return None


# def Second(inside):
#     os.environ['OPENAI_API_KEY'] = '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'
#     llm = ChatOpenAI(openai_api_key='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')
#     response = str(llm([HumanMessage(content=inside)]))
#     print("Langchain Response:", response)
    
#     # Parse the content value correctly
#     content_start = response.find("content=")
#     if content_start != -1:
#         content_start += len("content=")
#         content_end = response.find("'", content_start)
#         if content_end != -1:
#             content = response[content_start:content_end]
#             return content
#         else:
#             print("Content end not found.")
#     else:
#         print("Content start not found.")
    
#     # Return None if no valid content was extracted
#     return None


def Second(inside):
    os.environ['OPENAI_API_KEY'] = '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'
    llm = ChatOpenAI(openai_api_key='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')
    response = str(llm([HumanMessage(content=inside)]))
    print("Langchain Response:", response)
    
    # Extract content value
    content_start = response.find("content='")
    content_end = response.find("'", content_start + len("content='"))
    
    if content_start != -1 and content_end != -1:
        content = response[content_start + len("content='"):content_end]
        return content
    else:
        print("Content not found in Langchain response.")
        return None
