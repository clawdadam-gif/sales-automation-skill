# Sales Automation Skill

Automated sales workflow for lead qualification, routing, and follow-up management.

## What It Does

This skill automates the complete sales process for service businesses:
- **Lead Qualification:** Ask the right questions to identify high-intent prospects
- **Intelligent Routing:** Send leads to booking, phone, YouTube, or website based on intent
- **Follow-up Automation:** Schedule Day 1 and Day 3 follow-ups automatically
- **Data Logging:** Track all leads in JSON format

## Who It's For

- **Trades:** HVAC, plumbing, electrical, roofing
- **Home Services:** Landscaping, cleaning, contractors
- **Service Businesses:** Agencies, consulting, professional services

## How It Works

1. **Check incoming leads** (manual paste or automated)
2. **Qualify using 2-4 questions** (customizable by industry)
3. **Route based on intent:**
   - Warm/High-intent → Booking link
   - Immediate questions → Phone/text
   - Early-stage → Educational content (YouTube)
   - General info → Website
4. **Schedule follow-ups** (Day 1 & 3)
5. **Log to data file** (leads.json)
6. **Hand off high-intent leads** to business owner

## Installation

### Install via ClawHub (when available)
```
clawhub install sales-automation
```

### Manual Installation
```bash
mkdir -p ~/.clawdbot/skills/sales-automation
cp -r . ~/.clawdbot/skills/sales-automation/
```

## Usage

### Qualify a Lead
```bash
clawdbot agent "Qualify this lead: Acme HVAC, needs scheduling automation, 75 calls/week"
```

### Route a Lead
```bash
clawdbot agent "Route Acme HVAC to booking - urgent, budget approved"
```

### Check Follow-ups
```bash
clawdbot agent "What follow-ups are due today?"
```

## Pricing

Based on market research (February 2026):
- Basic setup: $100-300
- Full automation: $500-1,500
- Ongoing management: $200-500/month

## Features

- ✅ Industry-specific qualification questions
- ✅ Tailored framing (no false promises)
- ✅ Multi-channel routing
- ✅ Automated follow-up scheduling
- ✅ Lead data persistence (JSON)
- ✅ Handoff workflows
- ✅ Email templates included

## Configuration

Edit `lead-routing.json` to customize routing:
```json
{
  "booking": "your-booking-link",
  "primary_ai_number": "+1-your-number",
  "youtube": "your-youtube-channel",
  "website": "your-website"
}
```

## Based On

Real workflows deployed for:
- William F. Lynch Mechanical Contractors (HVAC)
- OTR Roofing (Roofing)
- Landry Mechanical (HVAC/Plumbing/Electrical)
- G&L Plumbing and Drain

## Author

Jon Dipilato <dipilatoautomations@gmail.com>
Dipilato Automations

## License

MIT

## Version

1.0.0
