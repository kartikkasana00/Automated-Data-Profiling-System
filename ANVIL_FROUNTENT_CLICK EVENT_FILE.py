from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.media


class Form1(Form1Template):

  def __init__(self, **properties):
    self.init_components(**properties)


  def CONFORM_click(self, **event_args):

   
    if self.file_loader_1.file is None:
      alert("Please upload a CSV file first")
      return

     
    Notification("Generating report, please wait...").show()

    try:
      
      report = anvil.server.call(
        "generate_report_from_csv",
        self.file_loader_1.file
      )

      
      anvil.media.download(report)
      

    except Exception as e:
      alert(f"Error occurred:\n{e}")
