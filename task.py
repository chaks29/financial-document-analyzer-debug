## Importing libraries and files
from crewai import Task
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import search_tool, read_financial_document, analyze_investment, assess_risk

## Creating a task to help solve user's query
analyze_financial_document = Task(
    description="Analyze the provided financial document to address the user's specific query: {query}. "
                "Extract relevant data points, identify key trends, and provide a detailed analysis based on the document's content.",
    expected_output="A comprehensive financial analysis report addressing the user query with data-backed insights and clear summaries.",
    agent=financial_analyst,
    tools=[read_financial_document],
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description="Based on the financial analysis, provide strategic investment recommendations. "
                "Consider the user's query: {query} and identify opportunities or concerns reflected in the data.",
    expected_output="A list of strategic investment recommendations, including potential buy/sell/hold actions and supporting rationale.",
    agent=investment_advisor,
    tools=[analyze_investment, search_tool],
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description="Identify and assess potential financial risks associated with the document and current market conditions. "
                "Highlight any areas of concern for an investor focused on: {query}.",
    expected_output="A detailed risk assessment report quantifying potential downsides and suggesting mitigation strategies.",
    agent=risk_assessor,
    tools=[assess_risk],
    async_execution=False,
)

verification = Task(
    description="Verify the relevance and accuracy of the financial data extracted from the document. "
                "Ensure that the analysis is based on factual information from the provided source.",
    expected_output="A verification report confirming the data integrity and relevance of the source document used in the analysis.",
    agent=verifier,
    tools=[read_financial_document],
    async_execution=False
)