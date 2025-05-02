import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get():
    verify_token = "123456"
    mode = frappe.form_dict.get("hub.mode")
    token = frappe.form_dict.get("hub.verify_token")
    challenge = frappe.form_dict.get("hub.challenge")

    if mode == "subscribe" and token == verify_token:
        return challenge
    else:
        return "Verification failed."

@frappe.whitelist(allow_guest=True)
def post():
    data = frappe.request.get_json()
    frappe.log_error("Meta Webhook Received", str(data))
    return {"status": "received"}

def get_context(context):
    if frappe.request.method == "GET":
        return get()
    elif frappe.request.method == "POST":
        return post()
    else:
        frappe.throw(_("Method not allowed"))
