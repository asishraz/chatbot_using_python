from chatterbot import ChatBot
chatbot = ChatBot("gareeb")

from chatterbot.trainers import ListTrainer
from tkinter import *
from PIL import ImageTk, Image

##convo = [
##    "Hello",
##    "Hi there!",
##    "what is your name?",
##    "I am bot, I don't have any name."
##    "How are you doing?",
##    "I'm doing great.",
##    "That is good to hear",
##    "In which city you live?",
##    "I live in binary state!",
##    "In which language you talk?",
##    "I talk in your language",
##    "Thank you.",
##    "You're welcome.",
##    "okay, bye",
##    "see you then"
##
##]

##trainer = ListTrainer(chatbot)
##trainer.train(convo)


##response = chatbot.get_response("what is your name?")
##print(response)

##print("TALK TO BOT")
##while True:
##    query = input()
##    if query == 'exit':
##        break
##    answer = chatbot.get_response(query)
##    print("Bot: ",answer)


main = Tk()
main.geometry("500x650")
main.title("gareeb CODER")
canvas = Canvas(main, width=300, height=300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("bot.jpg"))
canvas.create_image(20,20, anchor=NW, image=img)
##photoL = Label(main,image=img)
##photoL.pack(pady=5)
main.mainloop()

