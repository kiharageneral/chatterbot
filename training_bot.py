# from chatterbot.trainers import ListTrainer
# from chatterbot import ChatBot

# chatbot = ChatBot('MyBot')
# trainer = ListTrainer(chatbot)

# # Read training data from file
# with open('training_data.txt') as f:
#     conversations = f.readlines()

# # Train the chatbot with the conversations
# trainer.train(conversations)
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('MyBot')

# Train the chatbot
trainer = ListTrainer(chatbot)


# Remove the trained data
chatbot.storage.drop()

# Train the chatbot again from scratch
# # Read training data from file
with open('training_data.txt') as f:
    conversations = f.readlines()
    
trainer.train(conversations)

# Get a response from the chatbot
response = chatbot.get_response('What is a compiler?')
print(response)
