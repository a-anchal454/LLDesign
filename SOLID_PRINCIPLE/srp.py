# follow SRP
class Invoice:
    def Invoice(self,marker,quantity):
        self.marker=marker
        self.quantity=quantity


    def calculateTotal(self):
        price = ((marker.price)*self.quantity)
        print(price)



class InvoiceDao:
    def InvoiceDao(self,invoice):
        self.invoice=invoice

    def saveToDb(self):
        print("save invoice into db") 

    def saveToFile(self):
        print("save invoice into file")  

    def saveToLocal(self):
        print("save to local storage")  




class InvoicePrinter:
    def InvoicePrinter(self,invoice):
        self.invoice=invoice

    def printInvoice(self):
        print("Print the invoice")    

