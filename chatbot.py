from chatterbot import ChatBot
chatbot = ChatBot("gareeb")

from chatterbot.trainers import ListTrainer
from tkinter import *
from PIL import ImageTk, Image

convo = [
    "Hello Modi Jii",
    "Hi Gareeb, This is FAKEER AADMI",
    "I am so lucky to have you on my machine.",
    "LOL.LOL. ROFL.",
    "How is life modi jii",
    "Having fun with DO-LUND Trump. What about you?",
    "Not great, like you.",
    "HO BHI NAHI PAAYEGA, MERE JAISA GREAT",
    "Happy to hear that",
    "In which city you live?",
    "I live in binary state!",
    "In which language you talk?",
    "I talk in your language",
    "Thank you.",
    "You're welcome.",
    "okay, bye",
    "see you then"

]

trainer = ListTrainer(chatbot)
trainer.train(convo)


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



main.geometry("600x750")
main.title("gareeb CODER")
canvas = Canvas(main, width=200, height=200)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("bot.jpg"))
canvas.create_image(20,20, anchor=NW, image=img)
##photoL = Label(main,image=img)
##photoL.pack(pady=5)

def ask_from_bot():
    query = textF.get()
    answer_from_bot = chatbot.get_response(query)
    msgs.insert(END,"you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END,"Fakeer:  "+ str(answer_from_bot))
    textF.delete(0,END)

frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame,width=80,height=20)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

textF = Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)

btn = Button(main,text="Ask from Fakeer AADMI", font=("Verdana",20), command=ask_from_bot)
btn.pack()
main.mainloop()

