import tkinter as tk
import pyautogui as py
import keyboard as k
import time
import os

def print_pdf():
     folder_path = folderPathEntry.get()
     st = pdfPathEntry.get()
    # Main code here to handle the printing functionality
     if folder_path and st:

        def get_files_in_folder(folder_path):
            file_list = []
            for root, dirs, files in os.walk(folder_path):
                for file_name in files:
                    file_list.append(file_name)
            return file_list

        files = get_files_in_folder(folder_path)
        k.press_and_release('left windows + r')
        time.sleep(2)
        k.write("auto")
        time.sleep(2)
        k.press_and_release('enter')
        time.sleep(6)
        py.moveTo(x=652, y=588)
        time.sleep(1)
        py.click()
        #print("step 1")
        for i in range(1, len(files)):
            # to select files
            #print("step 2")
            py.moveTo(x=37, y=85)
            py.click()
            time.sleep(1)
            py.moveTo(x=500, y=87)
            py.click()
            time.sleep(2)
            #print("step  3")
            k.write(folder_path)
            time.sleep(3)
            k.press_and_release('enter')
            time.sleep(3)
            py.moveTo(x=427, y=552)
            py.click()
            st1 = str(files[i])
            k.write(st1)
            print(i,":",st1)
            k.press_and_release('enter')
            time.sleep(4)
            py.moveTo(x=589, y=91)
            time.sleep(6)
            py.click()
            time.sleep(6)

            py.moveTo(x=37, y=85)
            py.click()
            time.sleep(1)
            py.moveTo(x=500, y=87)
            py.click()
            time.sleep(2)

            k.write(st)
            time.sleep(4)
            k.press_and_release('enter')
            time.sleep(4)
            py.moveTo(x=540, y=495)
            py.click()
            base_name = os.path.splitext(files[i])[0]

            k.write(base_name)
            time.sleep(2)
            k.press_and_release('enter')
            time.sleep(3)
        print("Succesfully Printed",len(files),"Documents.......")
        # print("Printing PDF...")
        # print("Folder Path:", folder_path)
        # print("PDF Path:", pdf_path)

        submitBtn.config(state=tk.DISABLED)  # Disable the "Print PDF" button
       # stopBtn.grid(row=2, column=0, columnspan=2, pady=20)  # Show the "Stop" button


def stop_printing():
    # Add code to stop the printing process here
    print("Printing stopped.")

    submitBtn.config(state=tk.NORMAL)  # Enable the "Print PDF" button
   # stopBtn.grid_forget()  # Hide the "Stop" button


root = tk.Tk()
root.title("Smart Printing System")

header = tk.Label(root, text="Smart Printing System", bg="black", fg="white", font=("Arial", 20), pady=20,padx=120)
header.grid(row=0, column=0, columnspan=2)

container = tk.Frame(root, width=960, bg="#f2f2f2", padx=20, pady=20)
container.grid(row=1, column=0, columnspan=2)

folderPathLabel = tk.Label(container, text="Folder Path:")
folderPathLabel.grid(row=0, column=0, sticky="w")

folderPathEntry = tk.Entry(container, width=50)
folderPathEntry.grid(row=0, column=1, padx=10, pady=5)

pdfPathLabel = tk.Label(container, text="PDF Path:")
pdfPathLabel.grid(row=1, column=0, sticky="w")

pdfPathEntry = tk.Entry(container, width=50)
pdfPathEntry.grid(row=1, column=1, padx=10, pady=5)

submitBtn = tk.Button(container, text="Print PDFs", bg="#4CAF50", fg="white", font=("Arial", 16), padx=20, pady=10,
                      command=print_pdf)
submitBtn.grid(row=2, column=0, columnspan=2, pady=20)


#stopBtn = tk.Button(container, text="Stop", bg="red", fg="white", font=("Arial", 16), padx=20, pady=10,
                   # command=stop_printing)

root.mainloop()
