!pip install anvil-uplink pandas ydata-profiling


import anvil.server
import anvil.media
import pandas as pd
from ydata_profiling import ProfileReport
from google.colab import files
import os

anvil.server.connect("server_AO7TGVHGPTE6SHK6HPZZBGPD-KUE4QNGIVISXLZJ7")


@anvil.server.callable
def generate_report_from_csv(file):

    
    with anvil.media.TempFile(file) as tmp:
        df = pd.read_csv(tmp)

    
    profile = ProfileReport(
        df,
        title="Data Profiling Report",
        explorative=True
    )

    
    report_path = "/content/report.html"
    profile.to_file(report_path)

    with open(report_path, "rb") as f:
        html_bytes = f.read()

    
    files.download(report_path)

    
    return anvil.BlobMedia(
        "text/html",
        html_bytes,
        name="report.html"
    )


print("Colab connected. Waiting for Anvil calls...")
anvil.server.wait_forever()
