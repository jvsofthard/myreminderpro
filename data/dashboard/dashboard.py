from tkinter import Tk, Toplevel, Frame, Button, filedialog, messagebox, ttk
import json
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import Counter
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.lib.pagesizes import letter
import tempfile
import os

def exportar_dashboard_pdf(fig):
    archivo_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
    if archivo_pdf:
        try:
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_img:
                fig.savefig(tmp_img.name)
                tmp_img.close()
                c = pdf_canvas.Canvas(archivo_pdf, pagesize=letter)
                c.setFont("Helvetica-Bold", 14)
                c.drawString(200, 750, "Estadísticas de Recordatorios")
                c.drawImage(tmp_img.name, 50, 300, width=500, height=400)
                c.showPage()
                c.save()
                os.remove(tmp_img.name)
            messagebox.showinfo("✅ Exportado", f"Dashboard guardado como PDF en:\n{archivo_pdf}")
        except Exception as e:
            messagebox.showerror("❌ Error", f"No se pudo exportar:\n{e}")

def imprimir_dashboard(fig):
    try:
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_img:
            fig.savefig(tmp_img.name)
            tmp_img.close()
            os.startfile(tmp_img.name, "print")
            messagebox.showinfo("🖨️ Imprimiendo", "Dashboard enviado a la impresora.")
    except Exception as e:
        messagebox.showerror("❌ Error", f"No se pudo imprimir:\n{e}")

def mostrar_dashboard():
    ventana = Toplevel()
    ventana.title("📊 Estadísticas de Recordatorios")
    ventana.geometry("900x700")

    with open("data/data/recordatorios.json", "r", encoding="utf-8") as archivo:
        recordatorios = json.load(archivo)

    fechas = [r["fecha_hora"].split(" ")[0] for r in recordatorios]
    horas = [r["fecha_hora"].split(" ")[1][:2] for r in recordatorios]
    recurrentes = sum(1 for r in recordatorios if r["recurrente"])
    no_recurrentes = len(recordatorios) - recurrentes

    conteo_fechas = Counter(fechas)
    conteo_horas = Counter(horas)

    fechas_list = list(conteo_fechas.keys())
    cantidades_list = list(conteo_fechas.values())
    horas_list = sorted(conteo_horas.keys())
    cantidades_horas = [conteo_horas[h] for h in horas_list]

    notebook = ttk.Notebook(ventana)
    frame_graficos = Frame(notebook)
    frame_tabla = Frame(notebook)
    notebook.add(frame_graficos, text="📊 Gráficos")
    notebook.add(frame_tabla, text="📋 Tabla")
    notebook.pack(expand=True, fill='both')

    fig, axs = plt.subplots(2, 1, figsize=(8, 6))
    fig.suptitle("Dashboard de Recordatorios", fontsize=16)

    axs[0].bar(fechas_list, cantidades_list, color="#3498db")
    axs[0].set_title("Recordatorios por Fecha")
    axs[0].set_xlabel("Fecha")
    axs[0].set_ylabel("Cantidad")
    for i, v in enumerate(cantidades_list):
        axs[0].text(i, v + 0.1, str(v), ha='center', va='bottom')

    axs[1].bar(horas_list, cantidades_horas, color="#e67e22")
    axs[1].set_title("Recordatorios por Hora del Día")
    axs[1].set_xlabel("Hora")
    axs[1].set_ylabel("Cantidad")
    for i, v in enumerate(cantidades_horas):
        axs[1].text(i, v + 0.1, str(v), ha='center', va='bottom')

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    canvas = FigureCanvasTkAgg(fig, master=frame_graficos)
    canvas.draw()
    canvas.get_tk_widget().pack()

    frame_botones = Frame(ventana)
    frame_botones.pack(pady=10)

    btn_exportar = Button(frame_botones, text="📄 Exportar PDF", command=lambda: exportar_dashboard_pdf(fig), bg="#2ecc71", fg="white", padx=10)
    btn_exportar.pack(side="left", padx=10)

    btn_imprimir = Button(frame_botones, text="🖨️ Imprimir", command=lambda: imprimir_dashboard(fig), bg="#e67e22", fg="white", padx=10)
    btn_imprimir.pack(side="left", padx=10)

    # Tabla de datos
    columnas = ("Título", "Fecha", "Hora", "Recurrente")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center", width=150)
    for r in recordatorios:
        fecha, hora = r["fecha_hora"].split(" ")
        tabla.insert("", "end", values=(r["titulo"].strip(), fecha, hora, "Sí" if r["recurrente"] else "No"))
    tabla.pack(expand=True, fill="both", pady=20)

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    mostrar_dashboard()
    root.mainloop()
