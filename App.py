from tkinter import *
from mydb import Database
from tkinter import messagebox
from myApi import API

class NLPApp:
    def __init__(self):
        
        # create db object 
        self.dbo = Database()
        self.apio = API()
        
        # loading login GUI 
        self.root = Tk()
        # Tk is the main class inside tkinter and root is the variable which contain Tk class's object(Tk())
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/nlp.ico')
        # self.root.mainloop() this will hold the GUI on screen 
        self.root.geometry('350x600')
        self.root.configure(bg='#bde0fe')
        
        self.login_gui()
        
        self.root.mainloop()
        
        
    def login_gui(self):
        
        self.clear()
        
        heading = Label(self.root,text='NLPApp',bg='#bde0fe',fg='black')
        heading.pack(pady=(30,30))
        # heading.pack() reflect the content on GUI 
        heading.configure(font=('verdana',24,'bold'))
        
        label1 = Label(self.root,text='Enter Email',)
        label1.pack(pady=(10,10))
        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=5)
        
        label2 = Label(self.root,text='Enter Password',)
        label2.pack(pady=(10,10))
        self.password_input = Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=5)
        
        login_btn = Button(self.root,text='Login',width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))
        
        label3 = Label(self.root,text='Not a member?',)
        label3.pack(pady=(20,10))
        
        redirect_btn = Button(self.root,text='Register Now',width=15,height=2, command=self.register_gui)
        redirect_btn.pack(pady=(5,10))
        
    def register_gui(self):
        self.clear()
        
        heading = Label(self.root,text='NLPApp',bg='#bde0fe',fg='black')
        heading.pack(pady=(30,30))
        # heading.pack() reflect the content on GUI 
        heading.configure(font=('verdana',24,'bold'))
        
        label0 = Label(self.root,text='Enter your name',)
        label0.pack(pady=(10,10))
        self.name_input = Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=5)
        
        label1 = Label(self.root,text='Enter Email',)
        label1.pack(pady=(10,10))
        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=5)
        
        label2 = Label(self.root,text='Enter Password',)
        label2.pack(pady=(10,10))
        self.password_input = Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=5)
        
        register_btn = Button(self.root,text='Register',width=30,height=2,command=self.perform_registration)        
        register_btn.pack(pady=(10,10))
        
        label3 = Label(self.root,text='Already a member?',)
        label3.pack(pady=(20,10))
        
        redirect_btn = Button(self.root,text='Login Now',width=15,height=2, command=self.login_gui)
        redirect_btn.pack(pady=(5,10))
        
      
    def perform_registration(self):
        # Fetch data from gui
        name = self.name_input.get()
        email = self.email_input.get()
        password =self.password_input.get()
        
        response = self.dbo.add_data(name,email,password)
        
        if response:
            messagebox.showinfo('Success', 'Registration successful. You can login now')
        else:
            messagebox.showerror('Error', 'Email already exsits')
            
    def perform_login(self):
        
        email = self.email_input.get()
        password = self.password_input.get()
        
        response = self.dbo.search(email, password)
        
        if response:
            messagebox.showinfo('Success', 'Login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Invalid email or password')
            
    def home_gui(self):
        
        self.clear()
        
        heading = Label(self.root,text='NLPApp',bg='#bde0fe',fg='black')
        heading.pack(pady=(30,30))
        # heading.pack() reflect the content on GUI 
        heading.configure(font=('verdana',24,'bold'))
        
        sentiment_btn = Button(self.root,text='Sentiment Analysis',width=30,height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))
        
        ner_btn = Button(self.root,text='Name Entity Recognition',width=30,height=4, command=self.ner_gui)
        ner_btn.pack(pady=(10,10))
        
        emotion_btn = Button(self.root,text='Emotion Detection',width=30,height=4, command=self.emotion_gui)
        emotion_btn.pack(pady=(10,10))
        
        logout_btn = Button(self.root,text='Logout',width=15,height=2, command=self.login_gui)
        logout_btn.pack(pady=(10,10))
        
        
        
        
    def sentiment_gui(self):
        
        self.clear()
        
        heading = Label(self.root,text='NLPApp',bg='#bde0fe',fg='black')
        heading.pack(pady=(30,30))
        # heading.pack() reflect the content on GUI 
        heading.configure(font=('verdana',24,'bold'))
        
        heading2 = Label(self.root,text='Sentimental Analysis',bg='#bde0fe',fg='black')
        heading2.pack(pady=(10,20))
        # heading.pack() reflect the content on GUI 
        heading2.configure(font=('verdana',20))
        
        self.label1 = Label(self.root,text='Enter the text')
        self.label1.pack(pady=(20,20))
        
        self.sentiment_input = Entry(self.root, width = 50,)
        self.sentiment_input.pack(pady=(10,10), ipady=10)
        
        sentiment_btn = Button(self.root, text='Analyze Sentiment',command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))
        
        self.sentiment_result = Label(self.root,text='',bg='#bde0fe',fg='black')
        self.sentiment_result.pack(pady=(20,20))
        heading.configure(font=('verdana', 16))
        
        goback_btn = Button(self.root, text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10, 10))
        
        
    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        res = self.apio.sentiment(text)
        
        # Combine with VADER if desired
        vader_res = self.apio.vader_sentiment(text)
        # self.sentiment_result.config(text=f"{res.output} (±{res.probas})\nVADER: {vader_res}")
        
        # Format pysentimiento probabilities
        pos = res.probas.get("POS", 0) * 100
        neg = res.probas.get("NEG", 0) * 100
        neu = res.probas.get("NEU", 0) * 100
        
         # Format VADER compound score
        vader_comp = vader_res["compound"] * 100
        
        # Build display string
        output_text = (
            f"👍 Positive: {pos:.1f}%\n"
            f"👎 Negative: {neg:.1f}%\n"
            f"😐 Neutral:  {neu:.1f}%\n\n"
            f"🧮 VADER Compound Score: {vader_comp:.1f}%"
        )

        self.sentiment_result.config(text=output_text)
        
        
        
        
        
    def ner_gui(self):
        
        self.clear()
        
        heading = Label(self.root,text='NLPApp',bg='#bde0fe',fg='black')
        heading.pack(pady=(30,30))
        # heading.pack() reflect the content on GUI 
        heading.configure(font=('verdana',24,'bold'))
        
        heading2 = Label(self.root,text='Named Entity Recognisition',bg='#bde0fe',fg='black')
        heading2.pack(pady=(10,20))
        # heading.pack() reflect the content on GUI 
        heading2.configure(font=('verdana',20))
        
        self.label1 = Label(self.root,text='Enter the text')
        self.label1.pack(pady=(20,20))
        
        self.ner_input = Entry(self.root, width = 50,)
        self.ner_input.pack(pady=(10,10), ipady=10)
        
        ner_btn = Button(self.root, text='Analyze NER',command=self.do_ner_analysis)
        ner_btn.pack(pady=(10, 10))
        
        self.ner_result = Text(self.root, bg='#bde0fe', width=50, height=10, wrap="word", fg='black')
        self.ner_result.pack(pady=(20,20))
        heading.configure(font=('verdana', 16))
        
        goback_btn = Button(self.root, text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10, 10))
        
    def do_ner_analysis(self):
        
        text = self.ner_input.get()
        ents = self.apio.ner(text)
        # self.ner_result.config(text=", ".join(f"{t}:{l}" for t, l in ents))
        
        self.ner_result.delete("1.0", END)  # clear previous text
        if ents:
            for entity_text, entity_label in ents:
                self.ner_result.insert(END, f"{entity_text} → {entity_label}\n")
        else:
            self.ner_result.insert(END, "No named entities found.")
            
            
            
    
    def emotion_gui(self):
        
        self.clear()
        
        heading = Label(self.root,text='NLPApp',bg='#bde0fe',fg='black')
        heading.pack(pady=(30,30))
        # heading.pack() reflect the content on GUI 
        heading.configure(font=('verdana',24,'bold'))
        
        heading2 = Label(self.root,text='Emotion Detection',bg='#bde0fe',fg='black')
        heading2.pack(pady=(10,20))
        # heading.pack() reflect the content on GUI 
        heading2.configure(font=('verdana',20))
        
        self.label1 = Label(self.root,text='Enter the text')
        self.label1.pack(pady=(20,20))
        
        self.emotion_input = Entry(self.root, width = 50,)
        self.emotion_input.pack(pady=(10,10), ipady=10)
        
        emotion_btn = Button(self.root, text='Analyze Emotion',command=self.do_emotion_analysis)
        emotion_btn.pack(pady=(10, 10))
        
        self.emotion_result = Label(self.root,text='',bg='#bde0fe',fg='black')
        self.emotion_result.pack(pady=(20,20))
        heading.configure(font=('verdana', 16))
        print(self.emotion_result)
        
        goback_btn = Button(self.root, text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10, 10))
        
    def do_emotion_analysis(self):
        text = self.emotion_input.get()
        res = self.apio.emotion(text)
        output_lines = [f"{emotion.capitalize()}: {score:.2f}" for emotion, score in res.probas.items()]
        formatted_output = "\n".join(output_lines)
        self.emotion_result.config(text=formatted_output)
            
    def clear(self):
        # clear exisiting gui 
        for i in self.root.pack_slaves():
            i.destroy()
        
        
nlp = NLPApp()