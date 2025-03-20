#instaloader lib ile instadan veri çekebiliriz
import instaloader
import tkinter as tk 
from tkinter import messagebox #islem bitince uyarı versin diye

def installpost():
    username= entry_username.get()

    try:
        mybot= instaloader.Instaloader #instaloadera bağlanıp nesne oluşturuldu.
        profilim= instaloader.Profile.from_username(mybot.context,username) #context ile hesabı açık olan username verdiğimiz kişinin bilgilerini alırız,verileri aldık aslında burada tutuyoruz
        posts=profilim.get_posts() #postları buraya attık
        ### enumerate hatırla 
        """
        "Enumerate" fonksiyonu, Python'da bir döngü sırasında hem öğenin kendisine hem de bu öğenin dizindeki indeksine ihtiyaç duyulduğunda kullanılır.
          Özellikle "for" döngüsü içinde sıklıkla kullanılır.  "enumerate", genellikle listedeki öğelerin indekslerini takip ederek işlem yapmak istediğinizde işleri kolaylaştırır.
        """
        ##indexi 1den basla
        for index,post in enumerate(posts,1):
            mybot.download_post(post,target=f"Post_{username}/{index}")#indedex degerine göre dosya ismi atandı.
        messagebox.showinfo("basardın","gönderiler indi") 
  
    except Exception as e:
        messagebox.showerror("hata",str(e))

#tkinter ile arayüz oluşturucaz
root= tk.Tk()
root.title("instagram gönderilerini çekiyorum")
root.geometry("300x200")

#kullanıcı adını al
label=tk.Label(root,text="kullanıcı adı")
label.pack(pady=10)
entry_username tk.Entry(root) # su an ismi alıcaz

#indiricez
download_button= tk.Button(root,text="bilgileri indiriyorum",command=installpost) # bu çalıştıında instalpost fonksiyonu tetiklenicek
root.mainloop()