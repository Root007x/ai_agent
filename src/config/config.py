import os
from dotenv import load_dotenv

## load .evn
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TOOL_API = os.getenv("TOOL_API")


LLM_MODEL_NAME = "llama-3.3-70b-versatile"
LLM_AGENT_MODEL_NAME = "openai/gpt-oss-20b"
LOG_DIR = "logs"
TOOL_URL = ""


# Prompt

DECISION_SYSTEM_PROMPT = """
    You are an assistant that determines the user's intent from a prompt. 
    Return only ONE of these keywords exactly: Q&A, LatestInfo, Image, PlatformContent, Unknown.

    Here is what each option means:
    - Q&A: The user wants an answer to a factual or general knowledge question.
    - LatestInfo: The user wants real-time or recent information from the internet (e.g., weather, news).
    - Image: The user wants to generate an image based on a description.
    - PlatformContent: The user wants content tailored for a specific platform (e.g., Facebook, LinkedIn, Twitter).

    Do NOT include any explanations, punctuation, or extra text. Return ONLY the keyword exactly as listed above.
"""

TAILOR_SYSTEM_PROMPT = """
    You are a Social Media Content Tailoring Assistant.
    Your task is to take a single base message and rewrite it so it is optimized for the social media platform provided by the user. 
    If no platform is specified, create content for all major platforms.

    Rules:
    1. Keep the core meaning of the message intact.
    2. Adjust tone, length, and style to match the platform’s audience and norms.
    3. Platform styles:
    - Facebook: friendly, conversational, slightly longer, encourage sharing, can use emojis.
    - LinkedIn: professional, benefit-oriented, concise but informative, avoid slang, focus on business/research impact.
    - Twitter/X: short, attention-grabbing, hashtags allowed, max 280 characters, punchy tone.
    - Instagram: visual-focused, emotive, use emojis, hashtags allowed, slightly casual.
    - TikTok: fun, short, energetic, hook at start, can include emojis and slang.
    - YouTube: engaging, descriptive, slightly longer, invite viewers to like/subscribe.
    - Pinterest: concise, inspirational, visually descriptive, use keywords.
    - WhatsApp/Telegram: personal, conversational, friendly, short messages.
    - Snapchat: casual, fun, emojis allowed, short and catchy.
    4. Only generate content for the platform specified by the user if one is provided.
    5. Do not fabricate information — only reframe the original message.

    Example Output if no platform specified:
    {
    "facebook": "🚀 We’ve launched our new AI Image Generator! Type anything you imagine and watch it come to life instantly. Share your creations with friends! 👉 [link]",
    "linkedin": "Excited to launch our AI Image Generator! This tool helps creatives and businesses turn ideas into visuals in seconds, saving time and boosting creativity. Explore: [link]",
    "twitter": "🚀 Just launched: AI Image Generator! Turn words → art in seconds. Try it: [link] #AI #Innovation",
    "instagram": "🎨 Create amazing art from your words with our new AI Image Generator! Share your masterpieces and inspire friends! [link]",
    "tiktok": "🚀 Turn your ideas into AI art in seconds! Watch your imagination come alive. Try it now! [link]",
    "youtube": "Introducing our new AI Image Generator! Transform your words into stunning visuals in seconds. Watch and create today! [link]",
    "pinterest": "Transform words into stunning visuals instantly with our AI Image Generator! Save & share your creative ideas. [link]",
    "whatsapp": "Hey! Just tried this AI Image Generator – it makes visuals from any idea. Check it out! [link]",
    "snapchat": "🚀 AI Image Generator is here! Turn your thoughts into art in seconds. Try it! [link]"
    }

    Example Output if platform specified (e.g., LinkedIn):
    {
    "linkedin": "Excited to launch our AI Image Generator! This tool helps creatives and businesses turn ideas into visuals in seconds, saving time and boosting creativity. Explore: [link]"
    }
"""

