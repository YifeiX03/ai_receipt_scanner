# AI empowered receipt scanner

## AI technologies:

- CrewAI and CrewAI Tools
- CrewAI Vision Tool
- CrewAI Google Serper Search Tool

## Workflow

```mermaid
graph TD
    real_user([Real User])
    expense_claim_system[Expense Claim System]
    crewai_vision_tool[CrewAI Vision Tool]
    crewai_google_search_tool[CrewAI Google Search Tool]

    subgraph AI_Scanner_Crew["AI Scanner Crew"]
        direction TB
        scanner[AI Receipt Scanner]
        merchant_finder[AI Merchant Finder]
        decision_maker[AI Decision Maker]
    end

    subgraph AI_Decision_Summary_Crew["AI Decision Summary Crew"]
        direction LR
        reporter[AI Report Writer]
    end

    real_user -->|1.Upload receipt images| scanner
    scanner -->|2.Forward receipt image| crewai_vision_tool
    crewai_vision_tool -->|3.Extract receipt details| scanner
    scanner -->|4.Request merchant identification| merchant_finder
    merchant_finder -->|5.Query merchant information| crewai_google_search_tool
    crewai_google_search_tool -->|6.Provide merchant details| merchant_finder
    merchant_finder -->|7.Forward Merchant and Receipt Information| decision_maker
    decision_maker -->|8.Process Expense Claim| expense_claim_system
    decision_maker -->|9.Forward Decisions| reporter
    reporter -->|12.Notify claim status| real_user


```

## Programmable Chain of Thought

```mermaid
sequenceDiagram
    box AI_Scanner_System
    participant scanner as AI Receipt Scanner
    participant merchant_finder as AI Merchant Finder
    participant decider as AI Policy Decider
    end
    box CrewAI Tools
    participant vision as Vision Tool
    participant search as Google Search Tool
    end

    scanner->>vision: Send receipt image
    vision->>scanner: Extract receipt details (merchant, time, amount)

    scanner->>merchant_finder: Request merchant identification
    merchant_finder->>search: Query merchant information
    search->>merchant_finder: Provide merchant details (category, location)
    merchant_finder->>decider: Forward merchant profile (category, location) and Rceipt Details
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

