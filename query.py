from langchain_groq import ChatGroq
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser


from dotenv import load_dotenv
load_dotenv()
graph=Neo4jGraph()
llm= ChatGroq(model_name="llama3-groq-8b-8192-tool-use-preview")
chain=GraphCypherQAChain.from_llm(llm=llm,graph=graph,verbose=True, allow_dangerous_requests=True )


def check_is_getquery(query_string):
    response_schemas = [
    ResponseSchema(name="is_requested", description="answer to the user's question True if a read query else False"),
]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

    format_instructions = output_parser.get_format_instructions()
    prompt = f"""
    You are an expert in databases. Given the following query, determine whether it is requesting information (a read query) or manipulating data (a write query).
    Query: {query_string}

    Your answer should be in the following format:
    format:{format_instructions}
    """
    chain2=llm|output_parser
    res=chain2.invoke(prompt)
    print(res)
    return res["is_requested"]



def query(query_string):

    if(not check_is_getquery(query_string)):
        return "This model does not support any data manupulation."
    

    try:
        res=chain.invoke({"query":query_string})
        return res["result"]
    except Exception as e:
        return f"Error executing query: {e}"
      


