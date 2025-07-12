import gradio as gr

def create_whatsapp_link(phone, message):
    phone = phone.strip().replace("+", "")
    message = message.strip()
    
    if not phone or not message:
        return "Please enter both phone number and message."
    
    url = f"https://wa.me/{phone}?text={message.replace(' ', '%20')}"
    clickable_link = f"[Click to open WhatsApp chat]({url})"
    return clickable_link

with gr.Blocks(title="WhatsApp Message Sender") as demo:
    gr.Markdown("## 📲 Send WhatsApp Message")

    phone = gr.Textbox(label="Phone Number (with country code)", placeholder="e.g. 918107355673")
    message = gr.Textbox(label="Message", placeholder="Type your message here...", lines=3)

    output = gr.Markdown()

    send_button = gr.Button("Send via WhatsApp")
    send_button.click(create_whatsapp_link, inputs=[phone, message], outputs=output)

demo.launch()
