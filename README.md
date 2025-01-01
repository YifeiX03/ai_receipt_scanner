# AI empowered receipt scanner

## AI technologies:

- MultiModal Large Language Model
- Tool/Function calling
- Few-Shots
- Multiple AI Agents framework
- Programmable chain of thought

## Workflow

```mermaid
graph TD
    real_user([Real User])
    expense_claim_system[Expense Claim System]

    subgraph AI_Scanner_System["AI Scanner System"]
        direction TB
        bookkeeper[AI Bookkeeper]
        merchant_finder[AI Merchant Finder]
    end

    subgraph LLM_System["LLM System"]
        direction LR
        mmllm[MultiModal LLM]
        llm[LLM]
    end

    real_user -->|1.Upload receipt image| bookkeeper
    bookkeeper -->|2.Forward receipt image| mmllm
    mmllm -->|3.Extract receipt details| bookkeeper
    bookkeeper -->|4.Request merchant identification| merchant_finder
    merchant_finder -->|5.Query merchant information| llm
    llm -->|6.Provide merchant details| merchant_finder
    merchant_finder -->|7.Return merchant profile| bookkeeper
    bookkeeper -->|8.Request policy compliance check| llm
    llm -->|9.Assess receipt against policy| bookkeeper
    bookkeeper -->|10.Process expense claim| expense_claim_system
    expense_claim_system -->|11.Confirm claim submission| bookkeeper
    bookkeeper -->|12.Notify claim status| real_user

    classDef user fill:#f9d5e5,stroke:#333,stroke-width:2px
    classDef system fill:#d0e1f9,stroke:#333,stroke-width:2px
    classDef ai fill:#d5f5e3,stroke:#333,stroke-width:2px
    classDef llm fill:#ffcccb,stroke:#333,stroke-width:2px

    class real_user,expense_claim_system user
    class AI_Scanner_System system
    class bookkeeper,merchant_finder ai
    class LLM_System,mmllm,llm llm

    linkStyle default stroke:#333,stroke-width:2px
    style AI_Scanner_System fill:#f0f8ff,stroke:#333,stroke-width:2px
    style LLM_System fill:#fff0f5,stroke:#333,stroke-width:2px
```

## Programmable Chain of Thought

```mermaid
sequenceDiagram
    box AI_Scanner_System
    participant bookkeeper as AI Bookkeeper
    participant merchant_finder as AI Merchant Finder
    end
    box LLM_System
    participant mmllm as MultiModal LLM
    participant llm as LLM
    end

    bookkeeper->>mmllm: Send receipt image
    mmllm->>bookkeeper: Extract receipt details (merchant, time, amount)

    bookkeeper->>merchant_finder: Request merchant identification
    merchant_finder->>llm: Query merchant information
    llm->>merchant_finder: Provide merchant details (category, location)
    merchant_finder->>bookkeeper: Return merchant profile (category, location)
    bookkeeper->>llm: Query expense policy compliance (expense policy, merchant category, location, time, amount)
    llm->>bookkeeper: Return compliance assessment
```

## User cases

```mermaid
sequenceDiagram
    participant real_user as Real User
    participant ai_scanner_system as AI Scanner System
    participant expense_claim_system as Expense Claim System

    real_user->>ai_scanner_system: Send receipt image
    alt Processed
        ai_scanner_system->>expense_claim_system: Process expense claim
        expense_claim_system->>ai_scanner_system: Confirm claim submission
        ai_scanner_system->>real_user: Notify claim approval
    else Rejected
        ai_scanner_system->>real_user: Communicate rejection rationale
    else Additional Information Required
        ai_scanner_system->>real_user: Request supplementary receipt details
        real_user->>ai_scanner_system: Provide additional receipt information
        ai_scanner_system->>expense_claim_system: Process expense claim
        expense_claim_system->>ai_scanner_system: Confirm claim submission
        ai_scanner_system->>real_user: Notify claim approval
    end
```

## Prompts

- AI bookkeeper

```
Role: Bookkeeper

Task: Review expense receipts and determine approval status based on company expense policy and special case exceptions.

Input:

Expense Receipt informations:  merchant, time, amount
Merchant informations: category, location

Output:

Approval Status: One of the following:
APPROVE: The expense is compliant with the policy.
Additional Information Required: The expense is not fully compliant but may be approved with additional documentation.
REJECT: The expense is not compliant with the policy and special case exceptions.

Expense Policy:

[Insert specific expense policy details here, e.g., allowable expense categories, maximum spending limits, required documentation, etc.]

Special Case Exceptions:

[Insert specific exceptions to the expense policy, e.g., emergency expenses, client entertainment, etc.]

Example:

Input:
- Expense Receipt informations:  ABC, $500, 10pm
- Merchant informations: ABC is a restaurant, located in Vancouver

Output:

If the expense policy allows for client entertainment up to $250: Additional Information Required (requires documentation of the business purpose and attendees)
If the expense policy does not allow for client entertainment: REJECT
Note: To provide accurate and consistent approvals, the AI should be trained on a large dataset of expense receipts and policy decisions. It's also essential to regularly update the expense policy and special case exceptions to ensure accurate decision-making.
```

## Competitor

[fyle](https://www.fylehq.com/product/conversational-ai-for-expenses)
