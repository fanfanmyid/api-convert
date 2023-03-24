from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse # Add to Top
import pandas as pd
from io import BytesIO # Add to Top of File

app = FastAPI()

@app.get("")
def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    # df.to_excel("update_new.xlsx")
    file.file.close()
    buffer = BytesIO()
    with pd.ExcelWriter(buffer) as writer:
        df.to_excel(writer, index=False)
    return{"Hai":"HelloWorld"}


@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    # df.to_excel("update_new.xlsx")
    file.file.close()
    buffer = BytesIO()
    with pd.ExcelWriter(buffer) as writer:
        df.to_excel(writer, index=False)
    return StreamingResponse(
        BytesIO(buffer.getvalue()),
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        headers={"Content-Disposition": f"attachment; filename=data.xlsx"}
)
