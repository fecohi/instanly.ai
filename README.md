# Instantly API v2: From CSV to Campaign-Ready Leads in Minutes

Welcome to the **Instantly API v2** guide! In this tutorial, we’ll show you how to automate lead management workflows with ease. Whether you’re a developer looking to streamline CSV uploads or a growth marketer aiming to scale campaigns, this guide is for you.

---

## 🚀 Why Choose Instantly API v2?

Manually uploading CSV files and verifying emails is a thing of the past. With Instantly’s API v2, you can:

- **Automate** repetitive tasks like CSV uploads.
- **Verify** email addresses before ingestion.
- **Control** access with scoped API keys.
- **Test safely** using the **mock server** (no real data, no risk).

Instantly’s API is designed to save you time and reduce errors, so you can focus on what matters: growing your business.

---

## 🛠️ What We’ll Build

In this guide, we’ll create a Python script that:

1. Creates a **Lead List**.
2. Reads a local **CSV** file (`name,email`).
3. **Verifies** each email address.
4. **Creates** leads linked to the list.
5. Prints a summary of the process.

> **Note:** We’ll use the official **mock API** for a zero-risk demo. Switch one environment variable to hit production later.

---

## 📋 Prerequisites

Before you begin, ensure you have the following:

- **Python 3.10+**
- An **Instantly API key** (with minimal scopes for this demo)
- The `requests` library installed

### Setup Instructions

1. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use source venv/Scripts/activate
    pip install -r requirements.txt
    ```

2. Set the required environment variables:

    ```bash
    export INSTANTLY_API_KEY="your_api_key"
    export MOCK=1 or true   # Use mock server: https://developer.instantly.ai/_mock/api/v2
    ```

3. Run the script:

    ```bash
    python main.py
    ```

---

## 📡 Instantly API Endpoints Used

Here’s a quick overview of the API calls we’ll use:

- **`POST /lead-lists`**: Create a target lead list.
- **`POST /email-verification`**: Validate each email address before upload.
- **`POST /leads`**: Attach verified leads to the list.

---

## 🖥️ Example Output

When you run the script, you’ll see output like this:

```plaintext
✅ Lead list created: 019a0e4f-2924-7fb9-9775-0942f3d3219d
🔍 example@example.com -> valid
✅ 10 leads uploaded successfully
```

---

## 🌟 Why Developers Love Instantly

- **Comprehensive Documentation**: Get started quickly with clear examples.
- **Mock Server**: Test your integration without touching production data.
- **Scalable API**: Designed to handle high-volume campaigns effortlessly.

For more details, visit our [official documentation](https://developer.instantly.ai).

---

## 🤝 Join the Community

Have questions or need support? Join our developer community:

- [Instantly Developer Discord](https://discord.instantly.ai)
- [Contact Support](mailto:support@instantly.ai)

Let’s build something amazing together!
