# Personal Assistant
Source code for [this blog post](https://zainj.dev/posts?post=building-your-own-personal-assistant) about building a simple personal assistant using agents.

## Setup
Start by cloning this repository:

```
git clone https://github.com/zainmfjavaid/PersonalAssistant
```

Then, install the package requirements by running:

```
pip install -r requirements.txt
```

Before you can use the web app, you'll also need to configure your OpenAI API key. You can do this by going to the **agent.py** file and 
replacing the placeholder text on line 11:

```
os.environ['OPENAI_API_KEY'] = 'YOUR_OPENAI_API_KEY'
```

If you don't have an OpenAI API key yet, you can get one [here](https://platform.openai.com/account/api-keys)

## Running/Accessing the Web App
You can start the web server by running the **app.py** file.

Once you start the server, you can access the app at http://localhost:5000

## Notes
Although the rates are relatively low, keep in mind OpenAI charges for API use. The agent uses gpt-3.5-turbo by default, which you can find more pricing information about [here](https://openai.com/api/pricing/). You can also monitor your costs [here](https://platform.openai.com/usage). 
