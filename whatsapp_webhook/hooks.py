# whatsapp_webhook/hooks.py

app_name = "whatsapp_webhook"
app_title = "Whatsapp Webhook"
app_publisher = "Yusuf Paloba"
app_description = "Handle WhatsApp webhooks via Meta"
app_email = "yusufpaloba43@outlook.com"
app_license = "MIT"

# Optional but useful for APIs
has_whitelisted_api = True

# Avoid frontend asset build errors
app_include_js = []
app_include_css = []
web_include_js = []
web_include_css = []

# If you are using any fixtures (custom fields, scripts, etc.)
# fixtures = ["Custom Field", "Client Script", "Server Script"]

# Optional - example webhook route (you can adjust based on your actual route)
# override_whitelisted_methods = {
#     "your.route.path": "whatsapp_webhook.api.receive_message"
# }

# Optional - if you have scheduled tasks
# scheduler_events = {
#     "all": ["whatsapp_webhook.tasks.all"],
#     "daily": ["whatsapp_webhook.tasks.daily"],
#     "hourly": ["whatsapp_webhook.tasks.hourly"],
#     "weekly": ["whatsapp_webhook.tasks.weekly"],
#     "monthly": ["whatsapp_webhook.tasks.monthly"],
# }
