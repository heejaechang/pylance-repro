from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from httpx import Client

llm = AzureChatOpenAI(
    model=DEPLOYMENT_NAME,
    openai_api_version=OPENAI_API_VERSION,
    openai_api_key=config['OPENAI']['OPENAI_API_KEY'],
    base_url=f'{OPENAI_BASE_URL}/{DEPLOYMENT_NAME}',
    verbose=True,
    http_client=Client(verify=CERTIFICATE_PATH)
)

print(llm.invoke('Hello world.').content)

EMBEDDINGS_DEPLOYMENT_NAME='text-embedding-petrobras'
embeddings = AzureOpenAIEmbeddings(
    model=EMBEDDINGS_DEPLOYMENT_NAME,
    openai_api_version=OPENAI_API_VERSION,
    openai_api_key=config['OPENAI']['OPENAI_API_KEY'],
    base_url=f'{OPENAI_BASE_URL}/{EMBEDDINGS_DEPLOYMENT_NAME}',
    http_client=Client(verify=CERTIFICATE_PATH)
)

print(embeddings.embed_query('this is a test document'))
