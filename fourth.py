
from langchain.schema import AIMessage, HumanMessage, SystemMessage



def Fourth(inside):

  import os
  os.environ['OPENAI_API_KEY'] = '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'

#   inside=input("enter the question")

  from langchain.document_loaders import TextLoader


  file_path = './pto/py.txt' 
  loader = TextLoader(file_path, encoding='utf-8')



  from langchain.text_splitter import RecursiveCharacterTextSplitter
  text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
  splits = text_splitter.split_documents(loader.load())


  from langchain.vectorstores import Chroma
  from langchain.embeddings import OpenAIEmbeddings
  vectorstore = Chroma.from_documents(documents=splits,embedding=OpenAIEmbeddings())
  retriever = vectorstore.as_retriever()


  from langchain import hub
  rag_prompt = hub.pull("rlm/rag-prompt")


  from langchain.chat_models import ChatOpenAI
  llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)



  from langchain.schema.runnable import RunnablePassthrough
  rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()} 
    | rag_prompt 
    | llm 
)
 
 
  done=rag_chain.invoke(inside)
  if isinstance(done, AIMessage):
        done = done.content
    
  return done

  