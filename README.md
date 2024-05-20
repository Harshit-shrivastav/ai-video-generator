# 📽️ AI Video Generator 🤖

Welcome to the AI Video Generator! This app helps create educational videos easily. Just give it a title, and it does the rest!

## 🚀 Features

- 🎥 Create educational videos from a title
- 🖼️ Create visually stunning slides with background images and engaging text content tailored to the topic
- 🔊 Convert text to natural-sounding speech using Microsoft Edge TTS, bringing the content to life with a variety of voice options available
- 📧 Get an email with the video download link (optional)
- ⏱️ Automatic deletion of the video file after 24 hours for efficient storage management
- 🌐 User-friendly web interface with a clean and modern design

## 🔧 Prerequisites

Before starting, make sure you have:

- Python 3.11 🐍
- Required Python packages (see `requirements.txt`)
- A Gmail account for email notifications 📨

## 🚀 Installation

Here's how to get started:

1. Clone the repository: 🔥

```bash
git clone https://github.com/Harshit-shrivastav/AI-Video-Generator
```

2. Go to the project directory: 📂

```bash
cd AI-Video-Generator
```

3. Install required packages: 📦

```bash
pip install -r requirements.txt
```

4. Update environment variables in `.env` file. 📧

## 🔧 Variables

Here are the variables you need to define before using the AI Video Generator:

- `EMAIL_ADDRESS`: Your Email address for SMTP
- `EMAIL_PASSWORD`: You Password For SMTP
- `GOOGLE_API_KEY`: Gemini API Key
- `GROQ_API_KEY`: Groq API Key(Optional if Gemini is working in your region)
## 🚀 Usage

To generate a video:

1. Start the Web App: 🏃‍♂️

```bash
python3 -m main
```

2. Open your web browser and go to `http://localhost:8000`. 🌐

3. Enter the video title, choose a speaker voice, and optionally provide an email for the download link. 📝

4. Click "Generate Video" to start. 🎬

5. Wait for the video to be created. You'll get a success message with the video path (and an email if you provided one). 📨

6. Click "Download Video" to get your video.


## 📝 To Do List

Here are some features that i will implement in future (You can also contribute):

- [ ] Adding support for Images in slides
- [ ] Adding Title on Video slide
- [ ] Adding more formatting on Video Slides
- [ ] Fix bugs in slide generation(if any)


## 🤝 Contributing

We welcome contributions! If you find issues or have suggestions, please let us know. Your help makes this project better! 💪

## 📄 License

This project is licensed under the permissive [MIT License](LICENSE). Feel free to use, modify, and distribute the code. 🔑


Get ready to create and enjoy educational content in a whole new way! 🌟 Happy video making! 🎉
