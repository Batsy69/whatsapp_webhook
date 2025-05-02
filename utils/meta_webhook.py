import frappe

@frappe.whitelist(allow_guest=True)
def webhook():
    if frappe.request.method == "GET":
        verify_token = "your_verify_token"
        mode = frappe.form_dict.get("hub.mode")
        token = frappe.form_dict.get("hub.verify_token")
        challenge = frappe.form_dict.get("hub.challenge")

        if mode == "subscribe" and token == verify_token:
            return challenge
        else:
            frappe.throw("Verification failed.")

    elif frappe.request.method == "POST":
        data = frappe.request.get_json()
        frappe.log_error("Meta Webhook Received", str(data))
        return {"status": "received"}
