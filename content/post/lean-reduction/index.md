---
title: "Lean Reduction for AI-native Operation"
subtitle: ""
summary: ""
draft: true
math: true
date: "2026-08-12"
cover:
  image: "featured.jpg"
---

## Selling Operating Models

![](./selling.png)

Let us begin with a familiar process: selling. A street vendor sells items individually from a fixed cart. By working longer hours, the vendor can sell more. However, time imposes a strict ceiling. No one can work 30 hours in a day. Revenue therefore hits a scalability limit. The vendor decides to own a store and become its manager. The store employes people in specialized roles: a cashier handles purchases, salesperson assists customers, and stock clerk manages the inventory. The store owner's role shifts from doing the whole process on his own to designing a mechanism of specialized roles and monitoring it. That allows him to serve more customers. However, One person cannot manage two different stores in two different places simultaneously. Revenue therefore hits a scalability limit. The owner delegates daily operations to managers across ten distinct store locations, and conducts periodic site visits to supervise them. Such management or supervision raises a new cost of transportation but the payoff from store expansion exceeds it. Beyond a certain point of stores count, the coordination cost may diminish more profit margins. The owner decides to build a website where customers browses items, purchases, and receive deliveries at home. The owner scales his business far beyond what 100 stores may serve. The website monitoring cost is very cheap compared to client volume served.

## Returns to Scale

![](./returns-to-scale.png)

The aforementioned sale mechanisms illustrate the notion of "returns to scale" in microeconomics. It explains how an increase in the output is associated with an increase in the input. When the owner decided to launch multiple stores, the revenue increases. However, the revenue in proportion to the added cost of coordination and monitoring is less. The total revenue increased but the average revenue per unit of output decreased.

Microeconomics conventionally represents the production function $F(K,L)$. For our purposes, we use $C(N) = cN + H(N)$ where $C$ is cost function, $N$ is output units, $c$ is the cost per unit, and $H(N)$ is human coordination cost. Scalability improves when $H(N)$ grows slowly relative to $N$. Owning many stores corresponds to a high $H(N)$ due to management hierarchy and a moderate $c$ due to store rent. The website corresponds to low $H(N)$ due to specialized IT administrators and low $c$ due to server cost. The average cost per unit of output is less in the website. The returns to scale is increasing. The website enabled the business to scale its value delivery.

## eBay and Mechanism Design

![](./eBay.png)

Consider the case that the store sells used items by manually bidding where the bid is raised step-by-step. If the owner sticks to the same process of manually bidding but with a larger volume through the internet, she may raise selling volume. However, the website won't scale, compared to a website selling fixed-price items. The bidding process raises the cost of $H(N)$ while ordering a fixed-price item has a low cost of $H(N)$. The process is the same in fixed-price items but the bid price stepping depends on human interaction.

eBay innovated a new mechanism for its auctions. The bidder enters the maximum amount she is willing to pay, and an algorithm bids on behalf of bidders following a deterministic procedure, to keep them in the lead based on fixed bid increments. That mechanism requires less human interaction. It enabled eBay to scale its business like fixed-price websites.

The lesson here is that a healthy business aims to increase its returns to scale by designing operation workflows. Taking the operational workflow for granted, then using technology to speed up a process or accommodate more volume, is not optimal in many cases.

## Inconsistent Enforced AI Workflow

![](./enforced-ai.png)

An engineer may take a subset of data, train a predictive model on it, to optimize a single KPI like task volume. The engineer implicitly compressed the rich complexities of the operation teams into a singular metric. That single metric may project a ROI on paper, but the AI system may fail to satisfy the operational constraints that govern decisions, which have been heavily hardened by real-life experiences.

Let's consider an example. A B2B marketplace adopted an AI system for default prediction. A correct prediction may be overridden to preserve a high-value retailer; a second override because the sales representative visited the retailer in person; a third override because a new supplier joined and was requested by that retailer; a fourth override because a subscription is approaching an expiration date and the firm aims for retention; a fifth override because customer service escalation granted a promotional code.

An 80% accuracy model may be overridden 80% of the time. The operation then loses trust in the model and find it an unnecessary complication. The adhoc inconsistent exceptions may be too many, so that no AI fits their workflow. The operation will defend their stance that they are reacting to a fast-paced world around them, and that data is not enough to base their decisions on.

## Refining the Operation by Incremental Modeling

**Operation Ad hoc**

A B2B marketplace has a growth team and a credit risk team. They make calls, push offers, and decide credit lines based on judgment call, i.e what feels right, following random inconsistent justifications. Examples include: (1) This grocer has been with us for a year, so increase its credit limit; (2) This area is usually problematic, deny all new retailers from there; (3) We have a GMV target this quarter, approve more, and postpone dealing with risk later.

**Process and Policy**

Each department sets a simple decision table for clarifying the process it follows.

The growth sets (1) If the retailer's average monthly order volume over the last 3 months is below some segment baseline and the retailer has been active for at least 2 billing cycles, then the growth team decides. (2) If the retailer's average monthly order volume is at least the segment baseline and the retailer showed a positive response of an increased order volume within the last 2 cycles, then the growth team offers the retailer a promotion.

The credit risk team sets (1) For each retailer segment, like small grocery, the team assigns a base credit limit according to a predefined table. (2) If the retailer has 100% on-time repayment history over the last 3 billing cycles, the team increases the credit limit. (3) If the retailer's average monthly order volume over the last 3 months is greater than the segment's baseline monthly volume, the team increases the credit limit by an additional determined amount. (4) If the retailer has any late payment in the last 2 billing cycles, the team either keeps the current limit unchanged or decreases it.

**Modeling Business Knowledge by Applied Math**

Growth

- nodes / variables
  - Order Volume Trend: Recent trajectory of the retailer's order volume (e.g., declining, stable, growing).
  - Offer Response History: How the retailer responded to past promotional offers (e.g., no response, partial uptake, strong uptake).
  - Offer Decision: The action taken by the team (e.g., send targeted offer, hold/no offer, escalate to human).

- edges / causality
  - Retailers who enjoy a growing volume trend are more likely to respond well again.
  - Retailers who showed strong uptake on past offers are more likely to respond well again.

Credit Risk

- nodes / variables
  - On-Time Repayment History: The fraction or band of on-time payments over the last 3 billing cycles.
  - Recent Late Payments: Whether there were any late payments in the last 2 billing cycles.
  - Average Monthly Order Volume: The average order amount in the last 3 months compared to a baseline for that segment.
  - Credit Limit Decision: increase by a defined percentage; keep unchanged; or decrease according to the predefined tables.

- edges / causality
  - _On-Time Repayment History_ influences _Underlying Credit Risk_.  
  - _Recent Late Payments_ influences _Underlying Credit Risk_.  
  - Higher sustained _Average Monthly Order Volume_ suggests higher growth potential.
  - _Base Credit Limit_ can influence _Average Monthly Order Volume_.  

**Integrating Automation and Monitoring**

After a while, the operation manager noticed 60–70% of cases were agreeing with the model's suggested decision. They decide to use the model to compute the probability of the suggested action. If that probability is high enough, execute the action automatically. Otherwise, the case is escalated to a human. They designed dashboards for (1) percentage of decisions taken automatically; (2) failure rate of auto-approved and manually approved cases; (3) decision type and policy version of manually escalated decisions. They designed feedback loops to recalibrate the model. The operation transitioned from deciding everything to (1) model critics and calibrators, (2) designers of the override rules, and (3) exception handlers. The operation workflow became more structured.

**Restructuring the team using the same applied math lens**

We can set a layer above the two models, considering the estimated "default risk" and "growth potential", to decide whether to increase the credit limit.

| Risk \ Growth | Growth < Threshold | Growth ≥ Threshold |
|---|---|---|
| Risk ≥ Threshold | Auto reject | Escalate to human |
| Risk < Threshold | Escalate to human | Auto approve |

Region 1 and region 2 are autonomous. The team develops new dashboards to analyze each region across other variables. Feedback loops and recalibration aim to reduce human escalation.

**A New AI Workflow**

Only then does building a predictive AI becomes fitting. The Applied Math module defined a stable, transparent structure of variables and causal assumptions. The automated decision engine specified clearly where predictions would be used. The unified process had clear, agreed-upon objective functions.

## Dimensions

![](./dimensions.png)

**World Complexity.** As operations scale to handle more of the world's complexities, workflow complexity naturally increases. Let's consider an example on a B2B marketplace. The marketplace may source from a single supplier with fixed catalogs and stable prices. Then a clerk checks a paper or spreadsheet catalog, confirms stock over the phone, and writes up a purchase order. If multiple suppliers list overlapping products, each with buyer-specific pricing, then a category manager must cross-reference several supplier price sheets. The number of sheets and their cross-relations, and the process the manager follows after the clerk, grow as the marketplace handles more complex operations.

**AI / System Simplicity.** A marketplace may have an inventory house. A simple max-min threshold automation embedded in a spreadsheet may suffice: when a quantity drops below the minimum, a triggered formula or macro flags the item and auto-generates a replenishment request up to the max level. As the marketplace grows, buyer behaviour becomes more volatile. Alternatively, A predictive AI for demand forecasting may determine reorder points. The mechanism grows from a conditional formula to a learning model. The formula is easy to understand and audit. The learning model requires the operation to maintain more complexities as predictions may not always be accurate. Those include data distribution shift, model recalibration, and feedback loops.

**Human Supervision.** In customer support for example, a human may not intervene with cases at all; or handle a proportion of cases. A human may write an answer from scratch, review a given one, or monitor an aggregation of many cases.

As the operation aims to handle more of the world's complexities, it is natural to require more human supervision, and more complicated operation procedure. A good AI engineer designs the operation workflow and utilizes AI toolkit, so that a high complexity of the world is reduced to a simple AI or system mechanism with a minimal human supervision.

## Lean Reduction

Eric Ries initiated the "Lean Startup" methodology to avoid long business planning and to avoid engineering an expensive product, which may receive negative customer feedback, requiring redoing much work from scratch. The idea is to build a minimum product to discover and validate what the client needs, then progressively iterate on the product alongside the client's feedback. So building and feedback go hand-in-hand.

Our situation here is analogous. We may build a time-consuming AI which enforces a workflow, then discover it is inconsistent with the operation adhocs. We may build an expensive AI, then later discover it presumes the decision-making maturity required, missing from the operation member. In analogy to "Lean Startup", we need another kind of "Lean", where AI and operation adaptation go hand-in-hand.

The goal is not to immediately design the best workflow or best AI. The goal is to iteratively reduce adhocs and chaos into order alongside training the operation members to think with structured toolkit. AI and automation will follow naturally, and they will unlock new opportunities for operation restructure, to scale value delivery. AI comes as a natural consequence to fulfill subroutines the operation members had mastered but find boring.

That process is not trivial. If a member is used to manually checking all performance metrics to inform the executive, then taking the step to manually check less information alongside an aggregating view by AI, is not easy. Let's take an example. A hospital pharmacist reviews medication orders. He manually checks the prescribed drug against the patient's full medication list. If the hospital introduces a prescriptive AI which outputs "Approve" or "Review", he loses control and the stakes of following a wrong approved recommendation is high. However, If the hospital introduces descriptive data like the risk of ordered drug, the pharmacist may rely more on AI's recommendations for safe drugs, and devote more review time for unsafe drugs. That judgment skill, deciding when to follow and when to review, requires training and experience. The process of pushing the pharmacist to higher-level cognitive work should progress with AI solution design and building.

## Methodology

![](./methodology.png)

further. where to start? where to focus efforts?
