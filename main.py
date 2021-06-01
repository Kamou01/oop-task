# Easy Ticket
from tkinter import *
from tkinter import messagebox

gui = Tk()
gui.geometry("700x700")
gui.title("Easy tickets")
gui.config(bg="light blue")
variable = StringVar(gui)


class TicketSales:
    variable.set("Select tickets")

    def __init__(self, window):
        # labels for the window
        self.lblCell = Label(window, text="Enter your cellphone number: ", font="Arial 15")
        self.lblCell.place(x=40, y=60)
        self.lblCategory = Label(window, text="Ticket Category: ", font="Arial 15")
        self.lblCategory.place(x=40, y=120)
        self.lblTicket = Label(window, text="Number of Tickets Bought: ", font="Arial 15")
        self.lblTicket.place(x=40, y=180)
        # A label used to display the output
        self.Display = Label(window, bg="yellow", fg="black", font="Arial 15")
        self.Display.place(x=150, y=400, width=400, height=200)

        # entry window
        self.entry1 = Entry(window, bg="yellow")
        self.entry1.place(x=350, y=60, width=200)

        # A menu(using spinbox) to display the variation of tickets available
        self.menuCat = OptionMenu(window, variable, "Soccer", "Movies", "Theater")
        self.menuCat.place(x=350, y=120, width=200)

        # A spinbox to choose an amount of tickets wanted by the buyer
        self.spnbox = Spinbox(window, from_=1, to=100)
        self.spnbox.place(x=400, y=180, width=70, height=30)

        # button for calculating the price
        self.btnCalc = Button(window, text="Calculate Price", font="Arial 15 ", command=self.Calculate)
        self.btnCalc.place(x=60, y=250)

        # clear button to erase any data captured on the window
        self.btnClear = Button(window, text="Clear", font="Arial 15", bg="red", command=self.Clear)
        self.btnClear.place(x=400, y=250, width=100)

    # function to calculate the price
    def Calculate(self):
        number = self.spnbox.get()
        try:
            if variable.get() == "Soccer":
                num = self.entry1.get()
                if len(self.entry1.get()) == 10 or num[0] == 0:
                    # calculation for soccer tickets
                    total = int(self.spnbox.get()) * 40
                    self.Display.config(text="Amount: R" + str(total + (0.14 * total)) + "\n" +
                                             "Tickets reserved for: " + f' {variable.get()} ' + "for " + number + "\n" +
                                             "Tickets purchased by: " + self.entry1.get())
                else:
                    messagebox.showinfo("Error", "Input proper Cell Number!!")
                    self.entry1.delete(0, END)
                    self.spnbox.delete(0, END)
                    self.Display.config(text=" ")
            elif variable.get() == "Movies":
                num = self.entry1.get()
                if len(self.entry1.get()) == 10 or num[0] == 0:
                    total = int(self.spnbox.get()) * 75
                    self.Display.config(text="Amount: R" + str(total + (0.14 * total)) + "\n" +
                                             "Tickets reserved for: " + f' {variable.get()} ' + "for " + number + "\n" +
                                             "Tickets purchased by: " + self.entry1.get())
                else:
                    messagebox.showinfo("Error", "Try again - (Enter a proper cellphone number with 10 digits)!!!!")
                    self.entry1.delete(0, END)
                    self.spnbox.delete(0, END)
                    self.Display.config(text=" ")

            else:
                num = self.entry1.get()
                if len(self.entry1.get()) == 10 or num[0] == 0:
                    total = int(self.spnbox.get()) * 100
                    self.Display.config(text="Amount: R" + str(total + (0.14 * total)) + "\n" +
                                             "Tickets reserved for: " + f' {variable.get()} ' + "for " + number + "\n" +
                                             "Tickets purchased by: " + self.entry1.get())
                else:
                    messagebox.showinfo("Error", "Try again - (Enter a proper cellphone number with 10 digits)!!")
                    self.entry1.delete(0, END)
                    self.spnbox.delete(0, END)
                    self.Display.config(text=" ")

        except ValueError:
            messagebox.showinfo("Error", "make sure all values are entered ")

    def Clear(self):
        self.entry1.delete(0, END)
        self.spnbox.delete(0, END)
        self.Display.config(text=" ")


objectSales = TicketSales(gui)
gui.mainloop()
