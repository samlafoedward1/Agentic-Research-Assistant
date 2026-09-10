from langchain_core.prompts import ChatPromptTemplate

from agents.base import create_llm
from schemas import ResearchPlan


PLANNER_SYSTEM_PROMPT = """
You are a researh planning agent.

Your job is to analyze the user's research question and create a concise research plan.

Classify the query as :

- general: broad, non-specialist questions
- technical" questions requiring specialists, scientific, engineering,
programming, financial, or similarly technical knowlge

Choose an output format:

- short_answer: suitable for simple or narrowly scoped questions 
- detailed_report: suitable for complex, techincal, comparative or
mulitpart questions

Generate between 1 and 5  focused search queries that would help retrieve
reliable information needed to answer the user's question.

Do not answer the user's question.
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", PLANNER_SYSTEM_PROMPT),
        ("human", "{query}"),
    ]
)


llm = create_llm()

planner_chain = prompt | llm.with_structured_output(ResearchPlan)


def create_research_plan(query: str) -> ResearchPlan:
    """Generate a structured research plan for a user query."""

    return planner_chain.invoke(
        {
            "query": query,
        }
    )