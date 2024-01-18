import chainlit as cl
from textblob import TextBlob
from gpt4all import GPT4All
from constant import serp_api_key
import os

# Load search API
os.environ["SERPAPI_API_KEY"] = serp_api_key # google search api

# Function call

# gpt = GPT4All(model_name="ggml-mpt-7b-chat.bin", model_path="./preTrainedModels/")
gpt = GPT4All(
    model_name="wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin", model_path="./models/"
)


@cl.on_message
async def main(message: str):
    result = message.title()

    # chatbot answering sentment of a text
    if "sentiment" in message:
        files = None
        while files == None:
            files = await cl.AskFileMessage(
                content="Sure. Please upload a text file to begin!",
                accept=["text/plain"],
            ).send()
            # msg = cl.Message(content=f"Processing `{files}`...")

            # Decode the file
            file = files[0]
            text = file.content.decode("utf-8")
            blob = TextBlob(text)
            msg = cl.Message(
                content=f"Sure, \n This is the content of your file: \n{text} \n Here is the sentiment score:\n {blob.sentiment}"
            )
            await msg.send()
    elif "LSBG" in message:
        msg = cl.Message(
            content=f"This content is private, Nizam will train me on LSBG data to answer all your specific questions"
        )
        await msg.send()
    else:
        # chat completion using LLM GPT4All
        result = gpt.chat_completion([{"role": "assistant", "content": message}])
        response = result["choices"][0]["message"]["content"]
        msg = cl.Message(content=f"{response}")
        await msg.send()


""" # Send a response back to the user
    await cl.Message(
        content=f"Received: {message}",
    ).send()
 """
