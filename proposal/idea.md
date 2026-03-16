# Project Blue nanoGPT: Local Real Estate Intelligence for Pima County, AZ 

# Team Members
## Emeka Ekwenibe
## Elizabeth Maziarka
## Ricardo Gonzalez
## Leonardo Montoya

## Problem Statement
Who is the user?

The primary users are first-time home buyers interested in purchasing property in or near the Project Blue area in Pima County, Arizona. These buyers often do not have deep local knowledge about zoning, infrastructure plans, or long-term development projects that may affect the neighborhoods they are considering.

What problem or pain point do they experience today?

Today, people who want to understand how an area may develop in the future must search through many long government planning documents, zoning reports, infrastructure proposals, and scattered public records. This information is difficult to interpret and often spread across multiple websites. As a result, many buyers rely mostly on real estate websites, agents, or local news, which may not clearly explain how future development could affect property values, traffic, schools, or neighborhood growth.

## Why Now?
Why does this problem matter in the next 3–5 years?

The Project Blue region is expected to experience significant development and infrastructure changes over the coming years. As new housing, transportation projects, and commercial developments are planned, the surrounding neighborhoods may change rapidly. First-time buyers who purchase homes in the area without understanding these future developments may face unexpected changes in property values, traffic patterns, or community structure. Helping buyers understand these changes early can lead to better-informed housing decisions.

What changed that makes this possible now?

Recent advances in large language models and smaller fine-tuned AI models make it possible to build assistants that can read long documents and summarize them for users. In addition, many government planning records and development documents are now publicly available online, making it possible to collect and train a model on region-specific information. With lightweight models such as nanoGPT, it is now feasible to build a focused AI system trained on local data rather than relying on large general-purpose models.

## Proposed AI-Powered Solution
What does your product do for the user?

The proposed system is a local AI knowledge assistant trained on public planning and development documents related to the Project Blue area. A user can ask questions about housing development, infrastructure projects, zoning changes, schools, transportation, or neighborhood growth. The system will analyze the relevant public documents and provide clear summaries explaining what those developments may mean for someone considering purchasing a home in the area.

Where does AI/ML add unique value vs simple rules or heuristics?

AI provides value by allowing the system to read, interpret, and summarize large amounts of unstructured text from planning documents and public reports. Instead of manually searching through hundreds of pages of documents, users can ask natural language questions and receive a concise explanation. Traditional rule-based systems would struggle to interpret complex planning language, while a trained AI model can extract relevant information and generate understandable summaries for users.

## Initial Technical Concept
What data would you need (or already have)?

The system would rely on publicly available documents related to the Project Blue region, such as:

Pima County zoning and planning documents

Infrastructure and transportation project plans

Housing development proposals

School district information

Public safety or crime statistics reports

Local government meeting summaries and planning reports

These documents will form the training or reference dataset used by the AI assistant.

What model(s) might you use?

The project will explore using a small GPT-style language model (nanoGPT) trained or fine-tuned on text from the collected documents. The model will be designed to generate summaries and responses to user questions related to development and planning information in the area.

How could your nanoGPT work feed into this?

The nanoGPT model can act as the core generative component of the system. It can be trained on the curated dataset of local planning documents so that it learns terminology and context specific to the Project Blue region. The model can then generate summaries and answers to user questions based on the information contained in those documents.

## Scope for MVP
What can you realistically build in ~6 weeks?

Within six weeks, the team could build a basic prototype of the assistant that can process a limited set of planning documents and generate summaries or answers to simple user questions about development in the Project Blue area.

Concrete v1 feature

A user can enter a question about development near the Project Blue area, and the system returns a short explanation summarizing relevant information from local planning documents along with references to the source documents.

## Risks and Open Questions

Data availability and completeness – Some planning information may be incomplete, outdated, or difficult to obtain in machine-readable form.

Model accuracy and interpretation – The AI may misinterpret complex planning language or generate incorrect summaries if the data is unclear.

User trust and adoption – Home buyers may still rely heavily on traditional sources such as real estate agents, so the system must clearly reference original documents to build trust.

## Planned Data Sources

Potential sources for the dataset include:

Pima County planning and zoning department websites

Public infrastructure project reports

Local government planning documents and meeting records

School district information and public reports

Public crime or safety statistics

Other publicly available datasets related to housing and development in Pima County
