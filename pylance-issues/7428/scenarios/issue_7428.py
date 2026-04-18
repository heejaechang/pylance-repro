# SCENARIO: `langchain-openai` accepts field aliases through Pydantic, but Pylance reports false `No parameter named ...` call diagnostics.
# TARGET: the `AzureChatOpenAI` and `AzureOpenAIEmbeddings` constructor calls below.
# TRIGGER: wait for diagnostics to settle and inspect Problems.
# EXPECT: these keyword arguments should be accepted for this package surface; if Pylance reports `No parameter named "openai_api_key"` or `No parameter named "openai_api_version"`, treat that as a reproduction.
# VERIFY: the false `reportCallIssue` diagnostics remain visible on the constructor call sites.
# RECOVER: no recovery needed.

from httpx import Client
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings

CERTIFICATE_PATH = True
DEPLOYMENT_NAME = "test-deployment"
EMBEDDINGS_DEPLOYMENT_NAME = "test-embeddings"
OPENAI_API_VERSION = "2024-10-21"
OPENAI_BASE_URL = "https://example.openai.azure.com/openai/deployments"


llm = AzureChatOpenAI(
    model=DEPLOYMENT_NAME,
    openai_api_version=OPENAI_API_VERSION,
    openai_api_key="test-key",
    base_url=f"{OPENAI_BASE_URL}/{DEPLOYMENT_NAME}",
    verbose=True,
    http_client=Client(verify=CERTIFICATE_PATH),
)

embeddings = AzureOpenAIEmbeddings(
    model=EMBEDDINGS_DEPLOYMENT_NAME,
    openai_api_version=OPENAI_API_VERSION,
    openai_api_key="test-key",
    base_url=f"{OPENAI_BASE_URL}/{EMBEDDINGS_DEPLOYMENT_NAME}",
    http_client=Client(verify=CERTIFICATE_PATH),
)