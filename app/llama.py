import replicate

def run_chatbot(prompt):
    model_path = "meta/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1"
    input_data = {"prompt": prompt}
    
    output = replicate.run(model_path, input=input_data)
    
    # Combine all output items into a single string
    output_line = ' '.join(output)
    
    return output_line

# Example usage:
# prompt = "Hello, I'm a chatbot. What's your name?"
# output_line = run_chatbot(prompt)

# # Print the entire output line
# print(output_line)
# export REPLICATE_API_TOKEN=r8_BfzemfuXrzof5FwwdjjMycJRmiZK6ye3IxPOO
