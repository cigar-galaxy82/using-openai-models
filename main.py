# Example 1 

import openai 

# Replace 'your_api_key' with your actual OpenAI API key  

openai.api_key = 'your_api_key'  

response = openai.completions.create( 

model= "gpt-3.5-turbo-0125", 

prompt="Translate the following English text to French: 'Hello, how are you?'", 

max_tokens=60 

) 

print(response.choices[0].text.strip()) 

# Example 2

import openai 

# Replace 'your_api_key' with your actual OpenAI API key  

openai.api_key = 'your_api_key' 

response = openai.Completion.create( 

engine = "gpt-3.5-turbo-0125", 

prompt="Summarize the following article: 'OpenAI has announced ...'", 

max_tokens=150 

) 

print(response.choices[0].text.strip()) 


# Fine tuning a model

import openai 

# Replace 'your_api_key' with your OpenAI API key 

openai.api_key = 'your_api_key' 

response = openai.FineTune.create( 

training_file='path/to/your/training_dataset.json', 

model= " gpt-3.5-turbo-0125" 

) 

print("Fine tune job initiated:", response) 