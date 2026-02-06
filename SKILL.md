---
name: sales-automation
description: Automated sales workflow for lead qualification, routing, and follow-up management. Use when managing inbound leads, qualifying prospects, routing to booking/phone/website, and scheduling follow-ups (Day 1 & 3). Ideal for trades, home services, and small businesses with manual sales processes.
---

# Sales Automation

Complete sales workflow automation for service businesses. This skill handles lead qualification, intelligent routing, and automated follow-ups based on proven sales methodologies.

## Target Industries

- **Trades:** HVAC, plumbing, electrical, roofing
- **Home Services:** Landscaping, cleaning, contractors
- **Service Businesses:** Agencies, consulting, professional services

## Core Workflow

### 1. Lead Qualification (2-4 Questions)

Ask these qualifying questions based on SALES_SOP.md:

```
1. What process are you trying to improve right now?
2. How are you handling it today?
3. Roughly how many leads/tasks per week?
4. What happens if this stays the same for the next 30 days?
5. Who decides on this?
6. What budget range are you comfortable with?
```

**Purpose:** Identify urgency, budget, and decision-maker.

### 2. Lead Routing

Route qualified leads based on intent and urgency:

| Lead Type | Route | When to Use |
|-----------|-------|-------------|
| **Warm/High-intent** | Booking link | Confirmed budget or clear urgency |
| **Immediate questions** | Primary AI number | Same-day response needed |
| **Early-stage/educational** | YouTube | Want proof or education first |
| **General info** | Website | Comparison shopping |

**Always offer choice:** "Want the booking link or a quick call/text?"

### 3. Follow-up Schedule

- **Day 1:** First follow-up (24 hours after initial contact)
- **Day 3:** Second follow-up (if no response)
- **Handoff:** High-intent leads to business owner

## Scripts

### `qualify_lead.py`

Qualify incoming leads using standardized questions:

```bash
python3 scripts/qualify_lead.py --lead-data <data.json>
```

**Output:** Lead qualification score + recommended route

### `route_lead.py`

Route qualified leads to appropriate channel:

```bash
python3 scripts/route_lead.py --qualified-lead <data.json> --config <lead-routing.json>
```

**Output:** Routing recommendation + message template

## Configuration

Lead routing is configured in `/home/jonny/clawd/config/lead-routing.json`:

```json
{
  "website": "https://dipilatoautomations.com",
  "booking": "https://cal.com/jon-dipilato/30min",
  "primary_ai_number": "+1-508-290-7939",
  "youtube": "https://www.youtube.com/@JonDipilato"
}
```

## Data Storage

All leads logged to `/home/jonny/clawd/data/leads.json` with:

- Name, company, role, need
- Current process, volume, urgency
- Budget, source, route
- Next step, timestamp

## Tailored Framing Formula

**Use the prospect's numbers — never claim fixed results.**

Example:
- Prospect says: 30 leads/week, 8 mins each, 2 touches
- You calculate: That's ~8 hours/week today
- You say: "That's ~8 hours/week today. If we cut that in half, that's ~4 hours/week back."

**Never say:** "10-20 hours" unless the math supports it.

## Handoff to Owner

Hand off leads when:
- Budget is confirmed and they want to proceed
- They ask for pricing or a proposal
- Strong objection needs owner-level response

## Pricing Guidance

Based on market research (February 2026):

- **Basic setup:** $100-300 (configuration only)
- **Full automation:** $500-1,500 (custom workflows)
- **Ongoing management:** $200-500/month

## Quick Start

1. Check incoming leads
2. Run qualification questions
3. Route based on intent
4. Schedule follow-ups
5. Log to leads.json
6. Hand off high-intent leads

## References

- **SALES_SOP.md:** Complete sales methodology
- **qualification_questions.md:** Detailed question bank
- **email_templates.md:** Pre-written outreach templates

---

**Version:** 1.0.0
**Author:** Jon Dipilato <dipilatoautomations@gmail.com>
**License:** MIT
**Based on:** Real workflows deployed for trades and home services businesses
