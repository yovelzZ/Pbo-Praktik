import tkinter as tk
from tkinter import ttk, messagebox
import re  # Untuk validasi format tanggal

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x450")
        
        self.widget_create()
        
    def widget_create(self):
        # Judul Aplikasi
        title_label = tk.Label(self.root, text="To-Do List - Catat Tugas Anda", font=("Arial", 18))
        title_label.pack(pady=10)
        
        # Frame Input
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        # Input Nama Tugas
        tk.Label(input_frame, text="Nama Tugas: ").grid(row=0, column=0, padx=5, pady=5)
        self.task_name_entry = tk.Entry(input_frame, width=30)
        self.task_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Input Tenggat Waktu
        tk.Label(input_frame, text="Tenggat Waktu (dd-mm-yyyy): ").grid(row=1, column=0, padx=5, pady=5)
        self.task_deadline_entry = tk.Entry(input_frame, width=30)
        self.task_deadline_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Input Prioritas
        tk.Label(input_frame, text="Prioritas: ").grid(row=2, column=0, padx=5, pady=5)
        self.task_priority_combobox = ttk.Combobox(input_frame, values=["Tinggi", "Sedang", "Rendah"], width=27, state="readonly")
        self.task_priority_combobox.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Mata Kuliah: ").grid(row=3, column=0, padx=5, pady=5)
        self.task_subject_entry = tk.Entry(input_frame, width=30)
        self.task_subject_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Tombol Tambah Tugas
        add_button = tk.Button(self.root, text="Tambah Tugas", command=self.add_task, bg="lightblue")
        add_button.pack(pady=10)
        
        # Daftar Tugas
        self.task_treeview = ttk.Treeview(self.root, columns=("Nama Tugas", "Tenggat Waktu", "Prioritas", "Mata Kuliah", "Status"), show="headings")
        self.task_treeview.heading("Nama Tugas", text="Nama Tugas")
        self.task_treeview.heading("Tenggat Waktu", text="Tenggat Waktu")
        self.task_treeview.heading("Prioritas", text="Prioritas")
        self.task_treeview.heading("Mata Kuliah", text="Mata Kuliah")
        self.task_treeview.heading("Status", text="Status")
        self.task_treeview.column("Nama Tugas", width=200)
        self.task_treeview.column("Tenggat Waktu", width=150)
        self.task_treeview.column("Prioritas", width=100)
        self.task_treeview.column("Mata Kuliah", width=100)
        self.task_treeview.column("Status", width=100)
        self.task_treeview.pack(pady=10)
        
        # Tombol Hapus Tugas
        delete_frame = tk.Frame(self.root)
        delete_frame.pack(pady=5)

        delete_one_button = tk.Button(delete_frame, text="Hapus Tugas Terpilih", command=self.delete_task, bg="salmon")
        delete_one_button.grid(row=0, column=0, padx=5)

        delete_all_button = tk.Button(delete_frame, text="Hapus Semua Tugas", command=self.delete_all_tasks, bg="red", fg="white")
        delete_all_button.grid(row=0, column=1, padx=5)

        # Tombol Tandai Selesai
        mark_done_button = tk.Button(delete_frame, text="Tandai Selesai", command=self.mark_task_done, bg="lightgreen")
        mark_done_button.grid(row=0, column=2, padx=5)
    
    def add_task(self):
        """Menambahkan tugas ke dalam daftar"""
        task_name = self.task_name_entry.get()
        task_deadline = self.task_deadline_entry.get()  # Tenggat waktu dari input Entry
        task_priority = self.task_priority_combobox.get()
        task_subject = self.task_subject_entry.get()
        
        if task_name and task_priority and task_deadline and task_subject:
            # Validasi prioritas
            if task_priority not in ["Tinggi", "Sedang", "Rendah"]:
                messagebox.showerror("Error", "Pilih prioritas dari opsi yang tersedia!")
                return
            
            # Validasi format tenggat waktu (dd-mm-yyyy)
            if not self.is_valid_date(task_deadline):
                messagebox.showerror("Error", "Format tenggat waktu harus dd-mm-yyyy!")
                return
            
            # Menambahkan tugas dengan status "Belum Selesai"
            self.task_treeview.insert("", "end", values=(task_name, task_deadline, task_priority, task_subject, "Belum Selesai"))
            self.task_name_entry.delete(0, tk.END)
            self.task_deadline_entry.delete(0, tk.END)  # Reset tenggat waktu
            self.task_priority_combobox.set("")  # Reset prioritas
            self.task_subject_entry.delete(0, tk.END)  # Reset mata kuliah
        else:
            messagebox.showerror("Error", "Semua field harus diisi!")
    
    def delete_task(self):
        """Menghapus tugas yang dipilih"""
        selected_item = self.task_treeview.selection()
        if selected_item:
            for item in selected_item:
                self.task_treeview.delete(item)
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang ingin dihapus!")
    
    def delete_all_tasks(self):
        """Menghapus semua tugas"""
        if messagebox.askyesno("Konfirmasi", "Anda yakin ingin menghapus semua tugas?"):
            for item in self.task_treeview.get_children():
                self.task_treeview.delete(item)
    
    def is_valid_date(self, date_str):
        """Memvalidasi format tanggal dd-mm-yyyy"""
        date_pattern = r"^\d{2}-\d{2}-\d{4}$"  # Format dd-mm-yyyy
        return re.match(date_pattern, date_str) is not None

    def mark_task_done(self):
        """Menandai tugas yang dipilih sebagai selesai"""
        selected_item = self.task_treeview.selection()
        if selected_item:
            for item in selected_item:
                self.task_treeview.item(item, values=(
                    self.task_treeview.item(item, "values")[0],
                    self.task_treeview.item(item, "values")[1],
                    self.task_treeview.item(item, "values")[2],
                    self.task_treeview.item(item, "values")[3],
                    "Selesai"  # Menandai status tugas
                ))
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang ingin ditandai sebagai selesai!")

if __name__ == '__main__':
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
