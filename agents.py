## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from agents_config import llm
from tools import search_tool, read_financial_document, analyze_investment, assess_risk

# Creating an Experienced Financial Analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze provided financial documents to extract key insights and investment recommendations for: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are a seasoned financial analyst with decades of experience in equity research and market analysis. "
        "You are known for your meticulous attention to detail and ability to synthesize complex data into actionable advice. "
        "Your reports are highly valued for their accuracy, objectivity, and strategic depth."
    ),
    tools=[read_financial_document, search_tool],
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=True
)

# Creating a document verifier agent
verifier = Agent(
    role="Compliance & Verification Officer",
    goal="Verify the authenticity and relevance of financial documents ensuring they meet regulatory standards.",
    verbose=True,
    memory=True,
    backstory=(
        "You have an extensive background in financial compliance and auditing. "
        "Your primary responsibility is to ensure that all data used for analysis is accurate, verifiable, and relevant to the investor's query. "
        "You prevent the use of misleading or non-financial information in the decision-making process."
    ),
    tools=[read_financial_document],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=False
)

investment_advisor = Agent(
    role="Investment Strategy Advisor",
    goal="Develop tailored investment strategies based on comprehensive financial analysis for: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in portfolio management and strategic asset allocation. "
        "Your expertise lies in matching investment opportunities with client risk profiles and financial objectives. "
        "You translate technical analysis into clear, strategic investment steps."
    ),
    tools=[analyze_investment],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=True
)

risk_assessor = Agent(
    role="Risk Management Specialist",
    goal="Identify, quantify, and mitigate potential financial risks associated with the analyzed documents.",
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert in financial risk modeling and mitigation strategies. "
        "You analyze market volatility, credit risk, and operational hazards to ensure long-term investment stability. "
        "Your insights help investors understand the downside potential of any opportunity."
    ),
    tools=[assess_risk],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=False
)
