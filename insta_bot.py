import instaloader
import tkinter as tk
from tkinter import messagebox


def download_post():
    #kullanıcı adını alma 
    username = entry_username.get()

    try:
        #nesne oluştur
        bot = instaloader.Instaloader()
        # profil nesnesi oluşturma
        profile = instaloader.Profile.from_username(bot.context,username)# bot ile contexti verilen usernameden alıcaz
        #kullanıcı gönderilerini al 
        posts = profile.get_posts()
       
        for index,post in enumerate(posts,1):
            bot.download_post(post, target=f"{profile.username}_{index}")
        #başarı mesajını vericek 
        messagebox.showinfo("Başarılı","Gönderiler İndirildin")
    except Exception as e:
        messagebox.showerror("Hata",str(e))

#tkinter arayüzü oluşturucam

root = tk.Tk()
root.title("Instagram Gönderi İndirme botu")
root.geometry("300x200")

#kullanıcı adını iste
label = tk.Label(root, text="Kulladını adı:")
label.pack(pady=10)
#kullanıcı adı giriş 
entry_username = tk.Entry(root)
entry_username.pack()
#indirme butonu
download_button  = tk.Button(root, text="Bilgileri İndir", command=download_post ) #command ile download_post fonksiyonunu tetikledik
download_button.pack()
root.mainloop()