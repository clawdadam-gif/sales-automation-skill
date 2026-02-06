#!/usr/bin/env python3
"""
Route qualified leads to appropriate channels.

Usage:
    python3 route_lead.py --qualified-lead <data.json> --config <lead-routing.json>
"""

import json
import sys
from typing import Dict, Any

# Default routing configuration
DEFAULT_ROUTING = {
    "booking": "https://cal.com/jon-dipilato/30min",
    "primary_ai_number": "+1-508-290-7939",
    "youtube": "https://www.youtube.com/@JonDipilato",
    "website": "https://dipilatoautomations.com"
}

def route_lead(lead: Dict[str, Any], config: Dict[str, str] = None) -> Dict[str, Any]:
    """Route lead to appropriate channel."""

    if config is None:
        config = DEFAULT_ROUTING

    # Determine route based on lead data
    urgency = lead.get("urgency", "").lower()
    budget_confirmed = "budget" in lead.get("budget", "").lower() and any(
        x in lead.get("budget", "") for x in ["ready", "approved", "allocated"]
    )

    # Routing logic
    if urgency in ["immediate", "urgent", "asap"] and budget_confirmed:
        route = "booking"
        message = f"High-intent lead ready to book. Route to: {config['booking']}"
    elif urgency in ["immediate", "urgent", "asap"]:
        route = "primary_ai_number"
        message = f"Urgent lead needs immediate response. Call/text: {config['primary_ai_number']}"
    elif urgency in ["exploring", "researching", "just looking"]:
        route = "youtube"
        message = f"Educational lead. Share proof: {config['youtube']}"
    else:
        route = "website"
        message = f"General inquiry. Send to: {config['website']}"

    return {
        "lead": lead.get("name", "Unknown"),
        "route": route,
        "url": config.get(route, ""),
        "message": message,
        "next_action": get_next_action(route)
    }

def get_next_action(route: str) -> str:
    """Get recommended next action for route."""

    actions = {
        "booking": "Send booking link with 'Want to book now or talk first?'",
        "primary_ai_number": "Call or text within 1 hour",
        "youtube": "Send 2-3 relevant video links + CTA",
        "website": "Send website URL + 'What questions can I answer?'"
    }

    return actions.get(route, "Follow up in 24 hours")

if __name__ == "__main__":
    # Example usage
    example_lead = {
        "name": "Acme HVAC",
        "urgency": "immediate",
        "budget": "approved for $2k"
    }

    result = route_lead(example_lead)
    print(json.dumps(result, indent=2))
