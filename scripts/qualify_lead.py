#!/usr/bin/env python3
"""
Qualify incoming leads using standardized questions.

Usage:
    python3 qualify_lead.py --lead-data <data.json>
    python3 qualify_lead.py --name "Acme Corp" --industry "HVAC" --need "Scheduling automation"
"""

import json
import sys
from typing import Dict, Any

def calculate_score(lead_data: Dict[str, Any]) -> Dict[str, Any]:
    """Calculate qualification score based on lead data."""

    score = 0
    max_score = 100
    reasons = []

    # Urgency (0-30 points)
    urgency = lead_data.get("urgency", "").lower()
    if urgency in ["immediate", "urgent", "asap"]:
        score += 30
        reasons.append("High urgency")
    elif urgency in ["this week", "soon", "next few weeks"]:
        score += 20
        reasons.append("Medium urgency")
    elif urgency in ["exploring", "researching", "just looking"]:
        score += 5
        reasons.append("Low urgency - educational")

    # Budget (0-25 points)
    budget = lead_data.get("budget", "").lower()
    if "budget" in budget and any(x in budget for x in ["ready", "approved", "allocated"]):
        score += 25
        reasons.append("Budget confirmed")
    elif any(x in budget for x in ["$", "k", "month"]):
        score += 15
        reasons.append("Budget range provided")

    # Volume (0-20 points)
    volume = lead_data.get("volume", 0)
    try:
        volume = int(volume)
        if volume >= 50:
            score += 20
            reasons.append("High volume (50+/week)")
        elif volume >= 20:
            score += 15
            reasons.append("Medium volume (20-49/week)")
        elif volume >= 5:
            score += 10
            reasons.append("Low volume (5-19/week)")
    except (ValueError, TypeError):
        score += 5
        reasons.append("Volume unknown")

    # Decision maker (0-15 points)
    if "decision" in lead_data.get("role", "").lower():
        score += 15
        reasons.append("Decision maker")
    elif lead_data.get("can_decide", False):
        score += 10
        reasons.append("Can make decision")

    # Pain point clarity (0-10 points)
    need = lead_data.get("need", "")
    if len(need) > 20:
        score += 10
        reasons.append("Clear pain point")
    elif len(need) > 10:
        score += 5
        reasons.append("Some pain point clarity")

    return {
        "score": score,
        "max_score": max_score,
        "percentage": int((score / max_score) * 100),
        "reasons": reasons,
        "qualified": score >= 50
    }

def recommend_route(qualification: Dict[str, Any]) -> str:
    """Recommend routing based on qualification score."""

    score = qualification["percentage"]

    if score >= 70:
        return "booking"
    elif score >= 50:
        return "primary_ai_number"
    elif score >= 30:
        return "youtube"
    else:
        return "website"

if __name__ == "__main__":
    # Simple implementation for demonstration
    # In production, would parse command-line args or JSON input

    example_lead = {
        "name": "Acme HVAC",
        "industry": "HVAC",
        "need": "Scheduling automation",
        "urgency": "immediate",
        "budget": "approved",
        "volume": 75,
        "role": "owner"
    }

    qualification = calculate_score(example_lead)
    route = recommend_route(qualification)

    print(json.dumps({
        "lead": example_lead,
        "qualification": qualification,
        "recommended_route": route
    }, indent=2))
