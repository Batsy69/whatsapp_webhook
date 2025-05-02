import frappe
import json

@frappe.whitelist(allow_guest=True)
def webhook():
    if frappe.request.method == "GET":
        verify_token = "123456"  # <-- Your verify token
        mode = frappe.request.args.get("hub.mode")
        token = frappe.request.args.get("hub.verify_token")
        challenge = frappe.request.args.get("hub.challenge")

        if mode == "subscribe" and token == verify_token:
            return challenge
        else:
            frappe.throw("Verification failed.")

    elif frappe.request.method == "POST":
        data = frappe.request.get_json()
        frappe.log_error("Meta Webhook Received", json.dumps(data, indent=2))
        return {"status": "received"}
