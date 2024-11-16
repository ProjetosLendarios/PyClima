import tkinter as tk
from tkinter import messagebox
import requests
import os

# Configuração da janela principal
root = tk.Tk()
root.title("Previsão Meteorológica - PyClima - Gonçalo Garrido")

# Cores do Python
bg_color = "#306998"  # Azul Python
text_color = "#FFD43B"  # Amarelo Python
button_color = "#FFE873"  # Amarelo claro para botões
button_text_color = "#306998"  # Azul para texto do botão

# Configuração de tamanho e centralização da janela
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg=bg_color)

# Desativar a capacidade de redimensionar a janela
root.resizable(False, False)

# Definir ícone da aplicação
icon_path = os.path.join(os.path.dirname(__file__), "../Docs/icon.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
else:
    messagebox.showwarning("Aviso", "Ícone não encontrado. O programa continuará sem o ícone.")

# Função para obter a previsão meteorológica
def get_weather():
    city = city_entry.get()
    api_key = "1f798f99228596c20ccfda51b9771a86"  # Insira sua chave de API do OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["cod"] == 200:
            city_name = data["name"]
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"].capitalize()
            weather_info = f"Cidade: {city_name}\nTemperatura: {temp}°C\nCondição: {weather_desc}"

            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, weather_info)
        else:
            messagebox.showinfo("Informação", f"Erro: {data['message'].capitalize()}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro", f"Falha ao aceder à API. Detalhes: {e}")

# Interface gráfica
label = tk.Label(root, text="Digite o nome da cidade para ver a previsão:", bg=bg_color, fg=text_color, font=("Helvetica", 12))
label.pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 12))
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Obter Previsão", command=get_weather, bg=button_color, fg=button_text_color, font=("Helvetica", 10, "bold"))
search_button.pack(pady=10)

result_text = tk.Text(root, wrap='word', height=10, bg="#FFF", fg=bg_color, font=("Consolas", 10))
result_text.pack(pady=10)

# Iniciar a aplicação
root.mainloop()
