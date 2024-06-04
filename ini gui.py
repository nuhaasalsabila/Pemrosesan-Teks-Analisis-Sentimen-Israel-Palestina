from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import pandas as pd

class SentimentAnalysisApp:
    def __init__(self, master):
        self.master = master
        master.title("Analisis Sentimen - Israel Palestine Issue")
        master.geometry("1500x940")  
        master.configure(bg='#6a329f') 
        master.resizable(True, True) 

        background_image = Image.open("de.png")  
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = Label(master, image=background_photo)
        background_label.image = background_photo
        background_label.place(relwidth=1, relheight=1)

        self.open_csv_button = Button(master, text="Open CSV", command=self.open_csv_file, width=25, height=4)
        self.open_csv_button.place(relx=0.77, rely=0.50, anchor=CENTER)
        self.csv_data = pd.DataFrame()

    def open_csv_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

        if file_path:
            self.csv_data = pd.read_csv(file_path, delimiter=';')
            self.show_sentiment_analysis_window()

    def show_sentiment_analysis_window(self):
        new_window = Toplevel(self.master)  
        new_window.title("Analisis Sentimen")
        new_window.geometry("1500x700")
        new_window.configure(bg='#ba4e78')
        new_window.resizable(True, True) 

        background_image_analysis = Image.open("huft.png")  
        background_photo_analysis = ImageTk.PhotoImage(background_image_analysis)
        background_label_analysis = Label(new_window, image=background_photo_analysis)
        background_label_analysis.image = background_photo_analysis
        background_label_analysis.place(relwidth=1, relheight=1)

        text_label = Label(new_window, text="Masukkan teks untuk analisis sentimen:")
        text_label.pack(pady=10)

        input_textbox = Text(new_window, height=5, width=30)
        input_textbox.pack(pady=10)
        
        analyze_button = Button(new_window, text="Analyze Sentiment", command=lambda: self.analyze_sentiment(input_textbox.get("1.0", "end-1c")))
        analyze_button.pack(pady=10)
        
    def analyze_sentiment(self, text_to_analyze):
        print(f"Text to analyze: {text_to_analyze}")

        polarity_score = self.get_sentiment_score(text_to_analyze)
        result_window = Toplevel(self.master)
        result_window.title("Hasil Analisis Sentimen")
        result_window.geometry("300x100")
        result_window.configure(bg='#ba4e78')

        score_label = Label(result_window, text=f"Polarity Score: {polarity_score}")
        score_label.pack(pady=10)
    
    def get_sentiment_score(self, text):
        text = text.strip()
        try:
            row = self.csv_data[self.csv_data['text_clean'] == text]
            if not row.empty:
                sentiment_score = row['polarity'].values[0]
                return sentiment_score
            else:
                return "Data tidak ditemukan. Teks: {}".format(text)
        except Exception as e:
            return "Terjadi kesalahan: {}".format(str(e))

root = Tk()
sentiment_app = SentimentAnalysisApp(root)
root.mainloop()
