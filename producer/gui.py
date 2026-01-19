import tkinter as tk
from tkinter import ttk
import threading
from extract import connect_to_api, extract_json
from config import logger

class StockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Stock Market Analysis")
        self.root.geometry("900x600")
        
        # Header
        header = tk.Label(root, text="Stock Market Data", font=("Arial", 16, "bold"))
        header.pack(pady=10)
        
        # Button frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)
        
        self.refresh_btn = tk.Button(button_frame, text="Fetch Stock Data", command=self.fetch_data)
        self.refresh_btn.pack(side=tk.LEFT, padx=5)
        
        self.status_label = tk.Label(button_frame, text="Ready", fg="green")
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        # Treeview for displaying stock data
        columns = ("Symbol", "Date", "Open", "High", "Low", "Close")
        self.tree = ttk.Treeview(root, columns=columns, height=20)
        self.tree.column("#0", width=0, stretch=tk.NO)
        
        for col in columns:
            self.tree.column(col, anchor=tk.CENTER, width=140)
            self.tree.heading(col, text=col)
        
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def fetch_data(self):
        """Fetch data in a separate thread to prevent UI freezing"""
        self.refresh_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Fetching...", fg="orange")
        
        thread = threading.Thread(target=self._fetch_and_display)
        thread.daemon = True
        thread.start()
    
    def _fetch_and_display(self):
        """Fetch data and update GUI"""
        try:
            # Clear existing data
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Fetch data
            json_responses = connect_to_api()
            if json_responses:
                records = extract_json(json_responses)
                
                # Display data
                for record in records[:100]:  # Limit to 100 rows for performance
                    self.tree.insert("", tk.END, values=(
                        record["symbol"],
                        record["date"],
                        f"${record['open']:.2f}",
                        f"${record['high']:.2f}",
                        f"${record['low']:.2f}",
                        f"${record['close']:.2f}"
                    ))
                
                self.status_label.config(text=f"Loaded {len(records)} records", fg="green")
            else:
                self.status_label.config(text="Failed to fetch data", fg="red")
        
        except Exception as e:
            logger.error(f"GUI Error: {e}")
            self.status_label.config(text=f"Error: {str(e)}", fg="red")
        
        finally:
            self.refresh_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = StockGUI(root)
    root.mainloop()
